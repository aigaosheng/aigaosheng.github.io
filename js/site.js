/* Site behaviour, in plain JavaScript.
 *
 * Replaces jQuery 2.1.3, bootstrap.min.js 3.3.2 and hux-blog.min.js. Both
 * libraries had published XSS advisories, and between them they only ever did
 * the four small jobs below: Bootstrap's own plugins (tooltip, collapse,
 * modal ...) were never initialised anywhere on the site.
 */
(function () {
  'use strict';

  function wrap(el, className) {
    var box = document.createElement('div');
    box.className = className;
    el.parentNode.insertBefore(box, el);
    box.appendChild(el);
  }

  // Tables scroll sideways inside their own box instead of widening the page.
  function responsiveTables() {
    document.querySelectorAll('table').forEach(function (table) {
      if (!table.parentNode.classList.contains('table-responsive')) {
        wrap(table, 'table-responsive');
      }
      table.classList.add('table');
    });
  }

  // YouTube and Vimeo embeds keep a 16:9 shape at any width.
  function responsiveVideos() {
    document.querySelectorAll('iframe[src*="youtube.com"], iframe[src*="vimeo.com"]').forEach(function (frame) {
      wrap(frame, 'embed-responsive embed-responsive-16by9');
      frame.classList.add('embed-responsive-item');
    });
  }

  // Desktop only: the navbar hides while scrolling down and slides back in on
  // scroll-up. The .is-fixed / .is-visible styles live in less/hux-blog.less.
  function scrollUpNavbar() {
    var nav = document.querySelector('.navbar-custom');
    if (!nav || window.innerWidth <= 1170) return;
    var headerHeight = nav.offsetHeight;
    var previousTop = 0;
    var ticking = false;

    function update() {
      var currentTop = window.pageYOffset;
      if (currentTop < previousTop) {
        if (currentTop > 0 && nav.classList.contains('is-fixed')) {
          nav.classList.add('is-visible');
        } else {
          nav.classList.remove('is-visible', 'is-fixed');
        }
      } else {
        nav.classList.remove('is-visible');
        if (currentTop > headerHeight) nav.classList.add('is-fixed');
      }
      previousTop = currentTop;
      ticking = false;
    }

    window.addEventListener('scroll', function () {
      if (!ticking) {
        ticking = true;
        window.requestAnimationFrame(update);
      }
    }, { passive: true });
  }

  // /tags/: shade each tag from light to dark by how many posts carry it.
  // Same colours as the old jquery.tagcloud.js call (#bbbbee to #0085a1).
  function tagCloud() {
    var tags = document.querySelectorAll('#tag_cloud a[rel]');
    if (!tags.length) return;
    var start = [0xbb, 0xbb, 0xee];
    var end = [0x00, 0x85, 0xa1];
    var weights = Array.prototype.map.call(tags, function (a) {
      return Number(a.getAttribute('rel')) || 0;
    });
    var low = Math.min.apply(null, weights);
    var range = (Math.max.apply(null, weights) - low) || 1;
    tags.forEach(function (a, i) {
      var t = (weights[i] - low) / range;
      var rgb = start.map(function (s, k) { return Math.round(s + (end[k] - s) * t); });
      a.style.backgroundColor = 'rgb(' + rgb.join(',') + ')';
    });
  }

  function init() {
    responsiveTables();
    responsiveVideos();
    scrollUpNavbar();
    tagCloud();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
