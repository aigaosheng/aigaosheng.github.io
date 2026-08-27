/* Builds the in-post table of contents from the rendered headings.
 *
 * The theme's own .side-catalog was decorative: hux-blog.js only positioned the
 * box on scroll, and the Liquid that was supposed to fill it looped over
 * site.categories (empty on every post). The markup this fills lives in
 * _layouts/post.html and starts with the `hidden` attribute, so a post with too
 * few headings shows nothing at all rather than an empty box.
 */
(function () {
  'use strict';

  function slugify(text, used) {
    var base = text.toLowerCase()
      .replace(/[^\w一-鿿]+/g, '-')
      .replace(/^-+|-+$/g, '') || 'section';
    var id = base, n = 2;
    while (used[id]) { id = base + '-' + n++; }
    used[id] = true;
    return id;
  }

  function build() {
    var toc = document.getElementById('post-toc');
    var container = document.querySelector('.post-container');
    if (!toc || !container) { return; }

    var list = toc.querySelector('ol');
    var headings = container.querySelectorAll('h2, h3');
    var used = {}, entries = 0;

    Array.prototype.forEach.call(headings, function (h) {
      if (toc.contains(h)) { return; }
      var text = (h.textContent || '').trim();
      if (!text) { return; }
      // The stories in a brief are H3s under a single "Top Stories" H2, which
      // carries no information of its own.
      if (h.tagName === 'H2' && /^top stories$/i.test(text)) { return; }

      if (!h.id) { h.id = slugify(text, used); } else { used[h.id] = true; }

      var li = document.createElement('li');
      if (h.tagName === 'H3') { li.className = 'toc-h3'; }
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.textContent = text;
      li.appendChild(a);
      list.appendChild(li);
      entries++;
    });

    // Not worth a box for one or two headings.
    if (entries >= 3) { toc.removeAttribute('hidden'); }
  }

  function copyLink() {
    var link = document.querySelector('.js-copy-link');
    if (!link) { return; }

    var original = link.textContent;
    var resetTimer = null;

    function flash(message) {
      link.textContent = message;
      clearTimeout(resetTimer);
      resetTimer = setTimeout(function () { link.textContent = original; }, 1800);
    }

    function legacyCopy(url) {
      // navigator.clipboard needs a secure context and a focused document, so
      // this runs both as the old-browser path and as the rejection path.
      var ta = document.createElement('textarea');
      ta.value = url;
      ta.setAttribute('readonly', '');
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      var ok = false;
      try { ok = document.execCommand('copy'); } catch (err) { ok = false; }
      document.body.removeChild(ta);
      flash(ok ? 'Link copied' : 'Press Ctrl/Cmd+C');
      return ok;
    }

    link.addEventListener('click', function (e) {
      e.preventDefault();
      var url = link.getAttribute('data-url');
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(
          function () { flash('Link copied'); },
          function () { legacyCopy(url); }
        );
      } else {
        legacyCopy(url);
      }
    });
  }

  function init() { build(); copyLink(); }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
