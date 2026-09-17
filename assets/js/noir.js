/* ==========================================================================
   NOIR ECHELON — Interface behaviour
   No dependencies. Transform/opacity only. Degrades gracefully.
   ========================================================================== */
(function () {
  'use strict';

  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  var finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');
  var lowPower = (navigator.hardwareConcurrency || 8) <= 4;

  /* ----------------------------------------------------------------------
     Loader — 1.4s maximum, once per session, never for reduced motion
     ---------------------------------------------------------------------- */
  function loader() {
    var el = $('.loader');
    if (!el) return;

    var seen = false;
    try { seen = sessionStorage.getItem('ne_seen') === '1'; } catch (e) {}

    if (seen || reduced.matches) {
      el.parentNode.removeChild(el);
      document.documentElement.classList.add('is-ready');
      return;
    }

    try { sessionStorage.setItem('ne_seen', '1'); } catch (e) {}

    var dismiss = function () {
      el.classList.add('is-done');
      document.documentElement.classList.add('is-ready');
      window.setTimeout(function () {
        if (el.parentNode) el.parentNode.removeChild(el);
      }, 700);
    };
    window.setTimeout(dismiss, 1400);
    el.addEventListener('click', dismiss);
    window.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') dismiss();
    }, { once: true });
  }

  /* ----------------------------------------------------------------------
     Scroll reveal
     ---------------------------------------------------------------------- */
  function reveals() {
    var targets = $$('[data-reveal], .rule, .eyebrow, .reveal-group');
    if (!targets.length) return;

    if (!('IntersectionObserver' in window) || reduced.matches) {
      targets.forEach(function (t) { t.classList.add('is-in'); });
      return;
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in');
        io.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.08 });

    targets.forEach(function (t) {
      // Stagger children of a declared group
      if (t.hasAttribute('data-stagger')) {
        var step = parseInt(t.getAttribute('data-stagger'), 10) || 90;
        $$('[data-reveal], .reveal-line', t).forEach(function (child, i) {
          child.style.setProperty('--d', (i * step) + 'ms');
        });
      }
      io.observe(t);
    });

    // The observer is the fast path, but it cannot be relied on alone: its
    // first pass runs before webfonts settle the layout, and it has proved
    // unreliable for elements scrolled into view in one jump. This sweep is
    // the guarantee — throttled to a frame, skipping anything already shown,
    // and it removes itself once every target has been revealed.
    var pending = targets.slice();
    var ticking = false;

    var sweep = function () {
      var h = window.innerHeight || document.documentElement.clientHeight;
      var still = [];
      for (var i = 0; i < pending.length; i++) {
        var t = pending[i];
        if (t.classList.contains('is-in')) continue;
        var r = t.getBoundingClientRect();
        if (r.top < h * 0.94 && r.bottom > 0) {
          t.classList.add('is-in');
          io.unobserve(t);
        } else {
          still.push(t);
        }
      }
      pending = still;
      if (!pending.length) {
        window.removeEventListener('scroll', onScroll);
        window.removeEventListener('resize', onScroll);
      }
      ticking = false;
    };

    var onScroll = function () {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(sweep);
    };

    window.addEventListener('scroll', onScroll, { passive: true });
    document.addEventListener('scroll', onScroll, { passive: true, capture: true });
    window.addEventListener('resize', onScroll);
    window.addEventListener('orientationchange', onScroll);
    window.addEventListener('load', sweep);
    window.setTimeout(sweep, 500);
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(sweep).catch(function () {});
    }
  }

  /* ----------------------------------------------------------------------
     Header — condense on scroll, retreat on scroll-down
     ---------------------------------------------------------------------- */
  function header() {
    var head = $('.site-head');
    if (!head) return;
    var last = window.pageYOffset;
    var ticking = false;

    var update = function () {
      var y = window.pageYOffset;
      head.classList.toggle('is-stuck', y > 24);
      var menuOpen = document.body.classList.contains('menu-open');
      if (!menuOpen && y > 240 && y > last + 4) head.classList.add('is-hidden');
      else if (y < last - 4 || y <= 240) head.classList.remove('is-hidden');
      last = y;
      ticking = false;
    };

    window.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(update);
    }, { passive: true });
    update();
  }

  /* ----------------------------------------------------------------------
     Fullscreen menu
     ---------------------------------------------------------------------- */
  function menu() {
    var btn = $('.menu-btn');
    var panel = $('.menu');
    if (!btn || !panel) return;
    var lastFocus = null;

    var setOpen = function (open) {
      btn.setAttribute('aria-expanded', String(open));
      panel.classList.toggle('is-open', open);
      panel.setAttribute('aria-hidden', String(!open));
      document.body.classList.toggle('is-locked', open);
      document.body.classList.toggle('menu-open', open);
      $('.menu-btn__label', btn).textContent = open ? 'Close' : 'Menu';
      if (open) {
        lastFocus = document.activeElement;
        var first = $('.menu__link', panel);
        if (first) window.setTimeout(function () { first.focus(); }, 320);
      } else if (lastFocus) {
        lastFocus.focus();
      }
    };

    btn.addEventListener('click', function () {
      setOpen(btn.getAttribute('aria-expanded') !== 'true');
    });

    $$('a', panel).forEach(function (a) {
      a.addEventListener('click', function () { setOpen(false); });
    });

    document.addEventListener('keydown', function (e) {
      if (!panel.classList.contains('is-open')) return;
      if (e.key === 'Escape') { setOpen(false); return; }
      if (e.key !== 'Tab') return;
      var items = $$('a, button', panel).filter(function (n) { return n.offsetParent !== null; });
      if (!items.length) return;
      var first = items[0], lastItem = items[items.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); lastItem.focus(); }
      else if (!e.shiftKey && document.activeElement === lastItem) { e.preventDefault(); first.focus(); }
    });
  }

  /* ----------------------------------------------------------------------
     Cursor — desktop, fine pointer, motion allowed
     ---------------------------------------------------------------------- */
  function cursor() {
    if (!finePointer.matches || reduced.matches) return;

    var dot = document.createElement('div');
    dot.className = 'cursor';
    var ring = document.createElement('div');
    ring.className = 'cursor-ring';
    ring.innerHTML = '<span>View</span>';
    document.body.appendChild(dot);
    document.body.appendChild(ring);
    document.body.classList.add('has-cursor', 'cursor-hidden');

    var mx = window.innerWidth / 2, my = window.innerHeight / 2;
    var rx = mx, ry = my, raf;

    var loop = function () {
      rx += (mx - rx) * 0.16;
      ry += (my - ry) * 0.16;
      dot.style.transform = 'translate3d(' + mx + 'px,' + my + 'px,0) translate(-50%,-50%)';
      ring.style.transform = 'translate3d(' + rx + 'px,' + ry + 'px,0) translate(-50%,-50%)';
      raf = window.requestAnimationFrame(loop);
    };
    raf = window.requestAnimationFrame(loop);

    var awoken = false;
    document.addEventListener('mousemove', function (e) {
      mx = e.clientX; my = e.clientY;
      if (!awoken) {
        awoken = true;
        rx = mx; ry = my;
        document.body.classList.remove('cursor-hidden');
      }
    }, { passive: true });
    document.addEventListener('mouseleave', function () { document.body.classList.add('cursor-hidden'); });
    document.addEventListener('mouseenter', function () {
      if (awoken) document.body.classList.remove('cursor-hidden');
    });

    var bind = function (sel, cls) {
      $$(sel).forEach(function (el) {
        el.addEventListener('mouseenter', function () { document.body.classList.add(cls); });
        el.addEventListener('mouseleave', function () { document.body.classList.remove(cls); });
      });
    };
    bind('a, button, input, textarea, label, .acc__btn', 'cursor-link');
    bind('[data-cursor="view"]', 'cursor-view');
  }

  /* ----------------------------------------------------------------------
     Magnetic buttons
     ---------------------------------------------------------------------- */
  function magnetic() {
    if (!finePointer.matches || reduced.matches || lowPower) return;
    $$('[data-magnetic]').forEach(function (el) {
      var strength = parseFloat(el.getAttribute('data-magnetic')) || 0.22;
      var frame = null;

      el.addEventListener('mousemove', function (e) {
        if (frame) return;
        frame = window.requestAnimationFrame(function () {
          var r = el.getBoundingClientRect();
          var x = (e.clientX - (r.left + r.width / 2)) * strength;
          var y = (e.clientY - (r.top + r.height / 2)) * strength;
          el.style.transform = 'translate3d(' + x.toFixed(2) + 'px,' + y.toFixed(2) + 'px,0)';
          frame = null;
        });
      });

      el.addEventListener('mouseleave', function () {
        el.style.transition = 'transform 620ms cubic-bezier(0.22,1,0.36,1)';
        el.style.transform = '';
        window.setTimeout(function () { el.style.transition = ''; }, 640);
      });
      el.addEventListener('mouseenter', function () { el.style.transition = ''; });
    });
  }

  /* ----------------------------------------------------------------------
     Depth — extremely restrained parallax on marked elements
     ---------------------------------------------------------------------- */
  function depth() {
    var items = $$('[data-depth]');
    if (!items.length || reduced.matches || lowPower) return;
    var ticking = false;

    var update = function () {
      var y = window.pageYOffset;
      items.forEach(function (el) {
        var f = parseFloat(el.getAttribute('data-depth')) || 0.08;
        var top = el.getBoundingClientRect().top + y;
        var shift = (y - top) * f;
        var base = el.getAttribute('data-depth-center') === 'true' ? ' translate(-50%,-50%)' : '';
        el.style.transform = 'translate3d(0,' + shift.toFixed(1) + 'px,0)' + base;
      });
      ticking = false;
    };

    window.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(update);
    }, { passive: true });
    update();
  }

  /* ----------------------------------------------------------------------
     Accordion
     ---------------------------------------------------------------------- */
  function accordion() {
    $$('.acc').forEach(function (acc) {
      var buttons = $$('.acc__btn', acc);
      buttons.forEach(function (btn) {
        btn.addEventListener('click', function () {
          var panel = document.getElementById(btn.getAttribute('aria-controls'));
          var open = btn.getAttribute('aria-expanded') === 'true';
          buttons.forEach(function (other) {
            if (other === btn) return;
            other.setAttribute('aria-expanded', 'false');
            var p = document.getElementById(other.getAttribute('aria-controls'));
            if (p) p.classList.remove('is-open');
          });
          btn.setAttribute('aria-expanded', String(!open));
          if (panel) panel.classList.toggle('is-open', !open);
        });
      });
    });
  }

  /* ----------------------------------------------------------------------
     Scroll-scrubbed brand reveal
     The video never plays on its own: how far you have scrolled through the
     track IS the playhead. Loaded only when the section is close, skipped
     entirely for reduced motion, saver connections and absent video support.
     ---------------------------------------------------------------------- */
  function reel() {
    var root = $('[data-reel]');
    if (!root) return;

    var video = $('.reel__video', root);
    var track = $('.reel__track', root);
    var meter = $('.reel__meter i', root);
    if (!video || !track) return;

    var saveData = !!(navigator.connection && navigator.connection.saveData);
    var canPlay = !!video.canPlayType && video.canPlayType('video/mp4') !== '';

    if (reduced.matches || saveData || !canPlay) {
      root.classList.add('is-static');
      return;
    }

    // Pick the file that suits this viewport and this decoder: VP9 where it is
    // supported (smaller), H.264 everywhere else.
    var webm = video.canPlayType('video/webm; codecs="vp9"') !== '';
    // Three tiers, chosen by how many device pixels the frame will actually
    // occupy — a retina laptop asks for more than a phone in portrait.
    var css = window.innerWidth || 0;
    var device = css * (window.devicePixelRatio || 1);
    // Phones take the small cut whatever their pixel ratio claims: the frame is
    // never more than ~600px wide there, and the saving is most of a megabyte.
    var tier = css <= 600 ? '-small' : (device >= 1800 ? '-large' : '');
    var attr = (webm ? 'data-webm' : 'data-src') + tier;
    var source = video.getAttribute(attr) ||
                 video.getAttribute(webm ? 'data-webm' : 'data-src') ||
                 video.getAttribute('data-src');

    var loaded = false;
    var ready = false;
    var duration = 0;

    var load = function () {
      if (loaded) return;
      loaded = true;
      video.preload = 'auto';
      video.src = source;
      video.load();
      // iOS commonly ignores preload and fetches nothing until play() is
      // called, so nudge it: start muted playback, then immediately pause.
      var kick = video.play();
      if (kick && kick.then) {
        kick.then(function () { video.pause(); }).catch(function () {});
      }
    };

    video.addEventListener('loadedmetadata', function () {
      duration = video.duration || 0;
      ready = duration > 0;
      video.pause();
      draw();
    });

    var maybeLoad = function () {
      if (loaded) return;
      var rect = track.getBoundingClientRect();
      var h = window.innerHeight || 0;
      // Within one and a half screens of the stage: fetch it now
      if (rect.top < h * 1.5 && rect.bottom > -h * 0.5) load();
    };

    // Some mobile browsers will not decode until the element has been touched
    var unlock = function () {
      var p = video.play();
      if (p && p.then) { p.then(function () { video.pause(); }).catch(function () {}); }
      window.removeEventListener('touchstart', unlock);
      window.removeEventListener('pointerdown', unlock);
    };
    window.addEventListener('touchstart', unlock, { once: true, passive: true });
    window.addEventListener('pointerdown', unlock, { once: true });

    var target = 0;
    var current = 0;
    var raf = null;

    var progress = function () {
      var rect = track.getBoundingClientRect();
      var scrollable = rect.height - (window.innerHeight || 0);
      if (scrollable <= 0) return 0;
      var p = -rect.top / scrollable;
      return p < 0 ? 0 : (p > 1 ? 1 : p);
    };

    var phase = function (p) {
      return p < 0.26 ? 'start' : (p < 0.78 ? 'mid' : 'end');
    };

    var stalled = 0;
    var frozen = false;

    var tick = function () {
      // Ease toward the scroll position so flicks feel like film, not a jump cut
      current += (target - current) * 0.16;
      if (ready && Math.abs(current - video.currentTime) > 1 / 48) {
        try { video.currentTime = current; } catch (e) {}
        // Asking for a second or more of playhead and getting nothing back
        // means this browser or host cannot seek; fall back gracefully.
        if (!frozen && current > 1 && video.currentTime < 0.25) {
          if (++stalled > 90) {
            frozen = true;
            root.classList.add('is-frozen');
          }
        } else if (video.currentTime > 0.25) {
          stalled = 0;
        }
      }
      if (Math.abs(target - current) > 0.004) {
        raf = window.requestAnimationFrame(tick);
      } else {
        current = target;
        raf = null;
      }
    };

    var draw = function () {
      maybeLoad();
      var p = progress();
      if (meter) meter.style.width = (p * 100).toFixed(2) + '%';
      var ph = phase(p);
      if (root.getAttribute('data-phase') !== ph) root.setAttribute('data-phase', ph);
      if (!ready) return;
      target = p * duration;
      if (!raf) raf = window.requestAnimationFrame(tick);
    };

    var ticking = false;
    var onScroll = function () {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(function () { draw(); ticking = false; });
    };

    window.addEventListener('scroll', onScroll, { passive: true });
    document.addEventListener('scroll', onScroll, { passive: true, capture: true });
    window.addEventListener('resize', onScroll);
    window.addEventListener('orientationchange', onScroll);
    draw();
  }

  /* ----------------------------------------------------------------------
     Single-screen inquiry
     Posts to an endpoint when one is configured. Until then it composes the
     inquiry as an email and copies it, so the form is useful before launch
     rather than quietly doing nothing.
     ---------------------------------------------------------------------- */
  function enquiry() {
    $$('.enquiry-form').forEach(function (form) {
      var status = $('.enquiry__status', form);
      var button = $('.enquiry-send', form);
      var label = $('.enquiry-send__label', button);

      // Selects read as placeholder text until something is chosen
      $$('select', form).forEach(function (sel) {
        var sync = function () { sel.classList.toggle('has-value', !!sel.value); };
        sel.addEventListener('change', sync);
        sync();
      });

      $$('input, textarea, select', form).forEach(function (input) {
        input.addEventListener('input', function () {
          var field = input.closest('.field--line');
          if (field) field.classList.remove('has-error');
        });
      });

      var say = function (message, state) {
        if (!status) return;
        status.textContent = message;
        status.setAttribute('data-state', state || 'info');
      };

      var validate = function () {
        var ok = true;
        var first = null;
        $$('[data-required]', form).forEach(function (input) {
          var value = input.value.trim();
          var valid = value.length > 0;
          if (valid && input.type === 'email') {
            valid = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(value);
          }
          var field = input.closest('.field--line');
          if (field) field.classList.toggle('has-error', !valid);
          if (!valid) { ok = false; if (!first) first = input; }
        });
        if (!ok) {
          say('Please complete the highlighted fields.', 'error');
          if (first) first.focus({ preventScroll: false });
        }
        return ok;
      };

      var transcript = function () {
        var lines = [];
        $$('input, textarea, select', form).forEach(function (input) {
          if (!input.name || !input.value.trim()) return;
          var field = input.closest('.field--line');
          var name = field && $('label', field) ? $('label', field).textContent.trim() : input.name;
          lines.push(name + ': ' + input.value.trim());
        });
        return lines.join('\n');
      };

      form.addEventListener('submit', function (e) {
        e.preventDefault();
        if (!validate()) return;

        var endpoint = form.getAttribute('data-endpoint');
        var body = transcript();
        var company = (form.querySelector('[name="company"]') || {}).value || '';
        var subject = 'Project inquiry' + (company ? ' — ' + company.trim() : '');

        if (endpoint) {
          button.setAttribute('disabled', 'disabled');
          label.textContent = 'Sending…';
          say('Sending your inquiry…');
          fetch(endpoint, {
            method: 'POST',
            body: new FormData(form),
            headers: { Accept: 'application/json' }
          }).then(function (res) {
            if (!res.ok) throw new Error('failed');
            form.reset();
            $$('select', form).forEach(function (s) { s.classList.remove('has-value'); });
            label.textContent = 'Inquiry sent';
            say('Received — a senior person replies within one business day.');
          }).catch(function () {
            button.removeAttribute('disabled');
            label.textContent = 'Send inquiry';
            say('That did not send. Email ' + (form.getAttribute('data-mailto') || '') + ' instead.', 'error');
          });
          return;
        }

        // No endpoint yet: hand the visitor a ready-to-send email.
        var to = form.getAttribute('data-mailto') || '';
        var href = 'mailto:' + to +
          '?subject=' + encodeURIComponent(subject) +
          '&body=' + encodeURIComponent(body);

        var opened = false;
        try { window.location.href = href; opened = true; } catch (err) {}

        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(body).then(function () {
            say(opened
              ? 'Your email app should open with this inquiry ready to send — a copy is on your clipboard.'
              : 'Your inquiry is copied to the clipboard. Paste it into an email to ' + to + '.');
          }).catch(function () {
            say('Your email app should open with this inquiry ready to send.');
          });
        } else {
          say('Your email app should open with this inquiry ready to send.');
        }
      });
    });
  }

  /* ----------------------------------------------------------------------
     Misc
     ---------------------------------------------------------------------- */
  function year() {
    $$('[data-year]').forEach(function (el) {
      el.textContent = String(new Date().getFullYear());
    });
  }

  function boot() {
    loader();
    header();
    menu();
    reveals();
    accordion();
    enquiry();
    reel();
    year();
    depth();
    magnetic();
    cursor();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
