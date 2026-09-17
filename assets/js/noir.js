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

    // The observer's first pass runs before webfonts settle the layout, so
    // anything already on screen is revealed explicitly. A visitor who never
    // scrolls still sees a finished page.
    var sweep = function () {
      var h = window.innerHeight || document.documentElement.clientHeight;
      targets.forEach(function (t) {
        if (t.classList.contains('is-in')) return;
        var r = t.getBoundingClientRect();
        if (r.top < h * 0.94 && r.bottom > 0) {
          t.classList.add('is-in');
          io.unobserve(t);
        }
      });
    };
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
     Inquiry wizard
     ---------------------------------------------------------------------- */
  function wizard() {
    var form = $('#inquiry-form');
    if (!form) return;

    var panels = $$('.step-panel', form);
    var dots = $$('.progress__dot');
    var bar = $('.progress__bar i');
    var backBtn = $('.wizard-back', form);
    var nextBtn = $('.wizard-next', form);
    var live = $('#wizard-live');
    var done = $('.inquiry-done');
    var index = 0;

    var show = function (i, announce) {
      index = Math.max(0, Math.min(panels.length - 1, i));
      panels.forEach(function (p, n) { p.classList.toggle('is-active', n === index); });
      dots.forEach(function (d, n) {
        d.classList.toggle('is-active', n === index);
        d.classList.toggle('is-done', n < index);
      });
      if (bar) bar.style.width = (((index + 1) / panels.length) * 100) + '%';
      if (backBtn) backBtn.style.visibility = index === 0 ? 'hidden' : 'visible';
      if (nextBtn) {
        var last = index === panels.length - 1;
        $('.wizard-next__label', nextBtn).textContent = last ? 'Send inquiry' : 'Continue';
      }
      if (announce && live) {
        live.textContent = 'Step ' + (index + 1) + ' of ' + panels.length;
      }
      var focusable = $('input:not([type="radio"]), textarea, input[type="radio"]', panels[index]);
      if (focusable && announce) window.setTimeout(function () { focusable.focus({ preventScroll: true }); }, 220);
    };

    var validate = function (panel) {
      var ok = true;

      // Required choice groups
      var group = panel.getAttribute('data-requires-choice');
      if (group) {
        var chosen = form.querySelector('input[name="' + group + '"]:checked');
        var err = $('.field__err[data-for="' + group + '"]', panel);
        if (!chosen) {
          ok = false;
          if (err) err.style.display = 'block';
        } else if (err) {
          err.style.display = 'none';
        }
      }

      // Required text inputs
      $$('[data-required]', panel).forEach(function (input) {
        var field = input.closest('.field');
        var value = input.value.trim();
        var valid = value.length > 0;
        if (valid && input.type === 'email') {
          valid = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(value);
        }
        if (field) field.classList.toggle('has-error', !valid);
        if (!valid) ok = false;
      });

      // Consent
      var consent = $('.consent input[required]', panel);
      if (consent && !consent.checked) {
        ok = false;
        var cErr = $('.field__err[data-for="consent"]', panel);
        if (cErr) cErr.style.display = 'block';
      }

      if (!ok && live) live.textContent = 'Please complete the highlighted fields.';
      return ok;
    };

    if (nextBtn) {
      nextBtn.addEventListener('click', function () {
        if (!validate(panels[index])) return;
        if (index < panels.length - 1) { show(index + 1, true); return; }
        submit();
      });
    }
    if (backBtn) {
      backBtn.addEventListener('click', function () { show(index - 1, true); });
    }

    // Selecting a card advances the qualifying steps
    $$('.option input[type="radio"]', form).forEach(function (input) {
      input.addEventListener('change', function () {
        var panel = input.closest('.step-panel');
        if (!panel || !panel.hasAttribute('data-autoadvance')) return;
        window.setTimeout(function () {
          if (panels.indexOf(panel) === index && index < panels.length - 1) show(index + 1, true);
        }, 340);
      });
    });

    form.addEventListener('keydown', function (e) {
      if (e.key !== 'Enter') return;
      var t = e.target;
      if (t.tagName === 'TEXTAREA') return;
      e.preventDefault();
      if (nextBtn) nextBtn.click();
    });

    // Clear error state as the visitor types
    $$('input, textarea', form).forEach(function (input) {
      input.addEventListener('input', function () {
        var field = input.closest('.field');
        if (field) field.classList.remove('has-error');
      });
    });

    function submit() {
      var endpoint = form.getAttribute('data-endpoint');
      var data = new FormData(form);
      var finish = function () {
        panels.forEach(function (p) { p.classList.remove('is-active'); });
        dots.forEach(function (d) { d.classList.remove('is-active'); d.classList.add('is-done'); });
        if (bar) bar.style.width = '100%';
        var wrap = $('.wizard-shell');
        if (wrap) wrap.style.display = 'none';
        if (done) done.classList.add('is-active');
        if (live) live.textContent = 'Inquiry sent. We reply within one business day.';
        done.setAttribute('tabindex', '-1');
        done.focus({ preventScroll: true });
      };

      if (!endpoint) { finish(); return; }

      nextBtn.setAttribute('disabled', 'disabled');
      $('.wizard-next__label', nextBtn).textContent = 'Sending…';

      fetch(endpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
        .then(function (res) {
          if (!res.ok) throw new Error('Request failed');
          finish();
        })
        .catch(function () {
          nextBtn.removeAttribute('disabled');
          $('.wizard-next__label', nextBtn).textContent = 'Send inquiry';
          if (live) live.textContent = 'Something went wrong. Please email studio@noirechelon.com.';
          var fallback = $('.wizard-error');
          if (fallback) fallback.hidden = false;
        });
    }

    form.addEventListener('submit', function (e) { e.preventDefault(); });
    show(0, false);
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
    wizard();
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
