#!/usr/bin/env python3
"""Shrink the WordPress-export images in wdpress/assets and fix the links to them.

    python3 _tools/resize_wdpress.py            # resize, rename, rewrite links
    python3 _tools/resize_wdpress.py --dry-run  # report only, change nothing

Needs Pillow. Safe to run again: files already at or under the size limit, with
clean names, are left alone, so nothing is re-compressed twice.

What it fixes
-------------
The WordPress export saved images straight off the CDN, query string and all,
so files are named like "img_3861.jpg?w=1024" or "x.jpg?resize=1080%252C1080".
Most are full-resolution phone photos, 3-6 MB each, ~394 MB in total.

The imported posts in wdpress/_posts link to them as
"{{site.baseurl}}/assets/YYYY/MM/<name>?w=1024". That is wrong twice: the files
live under /wdpress/assets/, not /assets/, and a browser reads everything after
"?" as a query string, so even the right directory would not match a file
whose name contains "?w=1024". Every one of these images was a 404.

This script:
  1. strips the "?..." suffix from each file name. Where WordPress saved more
     than one size of the same image, the largest is kept;
  2. scales anything larger than MAX_EDGE down to it (JPEG quality 82,
     progressive). Images already small enough are only renamed, never
     re-encoded;
  3. rewrites the links in wdpress/ (outside assets/) to
     "{{site.baseurl}}/wdpress/assets/YYYY/MM/<clean name>".
"""

import argparse
import os
import re
import sys
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
WDPRESS = ROOT / "wdpress"
ASSETS = WDPRESS / "assets"
MAX_EDGE = 1600
JPEG_QUALITY = 82

LINK = re.compile(
    r"\{\{\s*site\.baseurl\s*\}\}/assets/(\d{4}/\d{2}/[^\"'\s)<>?]+)(\?[^\"'\s)<>]*)?"
)


def clean_name(path):
    return path.with_name(path.name.split("?", 1)[0])


def pixel_area(path):
    with Image.open(path) as im:
        return im.width * im.height


def shrink_images(dry_run):
    groups = {}
    for path in sorted(ASSETS.rglob("*")):
        if path.is_file():
            groups.setdefault(clean_name(path), []).append(path)

    before = after = resized = renamed = dropped = 0
    for target, sources in sorted(groups.items()):
        keep = max(sources, key=pixel_area)
        before += sum(p.stat().st_size for p in sources)
        for extra in sources:
            if extra != keep:
                dropped += 1
                if not dry_run:
                    extra.unlink()

        with Image.open(keep) as im:
            fmt = im.format
            too_big = max(im.size) > MAX_EDGE
            if too_big:
                im = ImageOps.exif_transpose(im)
                im.thumbnail((MAX_EDGE, MAX_EDGE), Image.LANCZOS)
                resized += 1
                if not dry_run:
                    tmp = target.with_name(target.name + ".tmp")
                    if fmt == "JPEG":
                        im.convert("RGB").save(tmp, "JPEG", quality=JPEG_QUALITY,
                                               optimize=True, progressive=True)
                    else:
                        im.save(tmp, fmt, optimize=True)
        if keep != target:
            renamed += 1
        if dry_run:
            continue
        if too_big:
            if keep != target:
                keep.unlink()
            os.replace(tmp, target)
        elif keep != target:
            os.replace(keep, target)
        after += target.stat().st_size

    print(f"images: {len(groups)} kept, {dropped} duplicate sizes dropped, "
          f"{resized} resized, {renamed} renamed")
    if not dry_run:
        print(f"bytes:  {before / 1e6:.1f} MB -> {after / 1e6:.1f} MB")
    return {p.relative_to(ASSETS).as_posix() for p in groups}


def rewrite_links(available, dry_run):
    changed_files = links = missing = 0
    for path in sorted(WDPRESS.rglob("*")):
        if not path.is_file() or ASSETS in path.parents or path.suffix not in {".html", ".md"}:
            continue
        text = path.read_text(encoding="utf-8")

        def fix(m):
            nonlocal links, missing
            rel = m.group(1)
            if rel not in available:
                missing += 1
                print(f"  no file for {path.relative_to(ROOT)}: {m.group(0)[:100]}",
                      file=sys.stderr)
                return m.group(0)
            links += 1
            return "{{site.baseurl}}/wdpress/assets/" + rel

        new = LINK.sub(fix, text)
        if new != text:
            changed_files += 1
            if not dry_run:
                path.write_text(new, encoding="utf-8")
    print(f"links:  {links} rewritten in {changed_files} files, {missing} with no file")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--dry-run", action="store_true", help="report only")
    args = parser.parse_args()
    available = shrink_images(args.dry_run)
    rewrite_links(available, args.dry_run)


if __name__ == "__main__":
    main()
