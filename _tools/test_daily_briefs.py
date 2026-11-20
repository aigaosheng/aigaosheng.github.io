import contextlib
import io
import os
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from _tools import daily_briefs


EDITION_DATE = "2026-11-20"
SLUG = "payments"


def make_brief(stories):
    headings = "\n".join(f"### {i}. 🤖 **Story {i}**" for i in range(1, stories + 1))
    return f"---\npermalink: /{SLUG}-brief-{EDITION_DATE}/\n---\n\n{headings}\n"


class RunTopicTargetTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.posts = os.path.join(self.temp_dir.name, "posts")
        self.logs = os.path.join(self.temp_dir.name, "logs")
        os.mkdir(self.posts)
        self.args = SimpleNamespace(
            force=False,
            dry_run=False,
            publish_time="20:00",
            retries=1,
            allow_empty=False,
            target_stories=3,
            provider="claude",
            model=None,
            effort="high",
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def run_with_replies(self, replies):
        output = io.StringIO()
        path = os.path.join(self.posts, f"{EDITION_DATE}-{SLUG}.md")
        with contextlib.ExitStack() as stack:
            stack.enter_context(patch.object(daily_briefs, "POSTS", self.posts))
            stack.enter_context(patch.object(daily_briefs, "LOGS", self.logs))
            stack.enter_context(patch.object(daily_briefs, "already_covered", return_value="none"))
            generate = stack.enter_context(
                patch.object(daily_briefs, "generate", side_effect=replies))
            stack.enter_context(contextlib.redirect_stdout(output))
            result = daily_briefs.run_topic(
                "Payments", "research prompt", {"payments": SLUG},
                EDITION_DATE, "2026-11-19 20:00 SGT", self.args)
        return result, path, generate, output.getvalue()

    def test_short_first_attempt_retries_with_expansion_and_reaches_target(self):
        result, path, generate, output = self.run_with_replies(
            [make_brief(2), make_brief(3)])

        self.assertEqual(result, "done")
        self.assertEqual(generate.call_count, 2)
        retry_prompt = generate.call_args_list[1].args[0]
        self.assertIn("broader search", retry_prompt)
        self.assertIn("Story 1", retry_prompt)
        with open(path, encoding="utf-8") as f:
            saved = f.read()
        self.assertEqual(daily_briefs.story_count(saved), 3)
        self.assertNotIn("below target", output)

    def test_saves_best_verified_brief_if_target_still_not_met(self):
        result, path, generate, output = self.run_with_replies(
            [make_brief(2), make_brief(1)])

        self.assertEqual(result, "short")
        self.assertEqual(generate.call_count, 2)
        with open(path, encoding="utf-8") as f:
            saved = f.read()
        self.assertEqual(daily_briefs.story_count(saved), 2)
        self.assertIn("below target 3", output)


if __name__ == "__main__":
    unittest.main()
