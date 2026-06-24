// rails.js — OneSRD gutter rails (side panels)
// Adds optional left/right panels in the empty margins of the centered reading
// column, on viewports wide enough to spare the room. A panel can show the
// Table of Contents, the Settings controls, a promo, or random art, and each
// side's choice persists across pages.
//
// Loads AFTER config.js (SiteConfig, L1Prefs) and nav.js. Injects its own
// markup, so pages need no per-page rail HTML -- only this script tag.
(function () {
  'use strict';

  if (window.__oneSRDRailsInit) return;   // guard against double-load
  window.__oneSRDRailsInit = true;

  const BASE = (typeof SiteConfig !== 'undefined' && SiteConfig.BASE_PATH) || '/';
  const CDN  = (typeof SiteConfig !== 'undefined' && SiteConfig.CDN_BASE)  || '';

  const main = document.getElementById('main');
  if (!main) return;
  const content = main.querySelector('.content-wrap');
  if (!content) return;

  // Global on/off + single-panel side come from L1Prefs (the Settings page).
  const pref = (k, d) => (typeof L1Prefs !== 'undefined' && L1Prefs.get(k) != null)
    ? L1Prefs.get(k) : (localStorage.getItem('l1-' + k) || d);
  if (pref('rails', 'on') === 'off') return;

  let SOURCES = [], ART = [], DEFAULTS = { left: null, right: null };

  const resolve = src => /^(https?:|\/)/.test(src) ? src : BASE + src;
  const artUrl  = name => CDN ? CDN + '/' + name : name;
  const mod     = i => ((i % SOURCES.length) + SOURCES.length) % SOURCES.length;
  const indexOf = id => Math.max(0, SOURCES.findIndex(s => s.id === id));

  // Resolve data-src CDN images inside injected fragments (the nav.js pattern).
  function resolveImgs(scope) {
    scope.querySelectorAll('img[data-src]').forEach(el => {
      el.src = artUrl(el.dataset.src);
      el.removeAttribute('data-src');
    });
  }

  /* ---- per-rail persistence ---- */
  function loadState(side, fallbackId) {
    try {
      const s = JSON.parse(localStorage.getItem('l1-rail-' + side));
      if (s && s.id) return s;
    } catch (e) { /* ignore malformed */ }
    return { id: fallbackId, pinned: false, open: true };
  }
  function saveState(rail) {
    const s = SOURCES[mod(rail.index)];
    localStorage.setItem('l1-rail-' + rail.side, JSON.stringify({
      id: s ? s.id : null, pinned: rail.pinned, open: rail.open,
    }));
  }

  /* ---- pull element(s) out of a fetched page; the nav.js link-rewrite trick ---- */
  function extract(text, selector, opts) {
    const doc = new DOMParser().parseFromString(text, 'text/html');
    const nodes = [...doc.querySelectorAll(selector)];
    if (!nodes.length) return '<div class="rail-error">Nothing matched ' + selector + '.</div>';
    nodes.forEach(node => {
      if (opts.rewrite) node.querySelectorAll('a[href]').forEach(a => {
        const href = a.getAttribute('href');
        if (href && !/^(https?:|\/|#|mailto:)/.test(href)) a.setAttribute('href', BASE + href);
      });
      if (opts.stripIds) node.querySelectorAll('[id]').forEach(e => e.removeAttribute('id'));
    });
    return nodes.map(n => n.outerHTML).join('');
  }

  /* ---- bind injected Settings controls to the real L1Prefs (parity + persist) ---- */
  function wireSettings(scope) {
    if (typeof L1Prefs === 'undefined') return;
    scope.querySelectorAll('input[name="theme"]').forEach(r => {
      r.checked = (r.value === L1Prefs.get('theme'));
      r.addEventListener('change', () => { if (r.checked) L1Prefs.set('theme', r.value); });
    });
    scope.querySelectorAll('input[name="fontsize"]').forEach(r => {
      r.checked = (r.value === L1Prefs.get('fontsize'));
      r.addEventListener('change', () => { if (r.checked) L1Prefs.set('fontsize', r.value); });
    });
    scope.querySelectorAll('input[name="railside"]').forEach(r => {
      r.checked = (r.value === L1Prefs.get('railside'));
      r.addEventListener('change', () => { if (r.checked) L1Prefs.set('railside', r.value); });
    });
    scope.querySelectorAll('input[name="railmode"]').forEach(r => {
      r.checked = (r.value === L1Prefs.get('railmode'));
      r.addEventListener('change', () => { if (r.checked) L1Prefs.set('railmode', r.value); });
    });
    scope.querySelectorAll('.settings-group').forEach(g => {
      const head = (g.querySelector('h2') || {}).textContent || '';
      const cb = g.querySelector('input[type="checkbox"]');
      if (!cb) return;
      const key = /motion/i.test(head) ? 'reducemotion'
                : /navigation/i.test(head) ? 'navbg'
                : /side panel/i.test(head) ? 'rails' : null;
      if (!key) return;
      cb.checked = (L1Prefs.get(key) === 'on');
      cb.addEventListener('change', () => L1Prefs.set(key, cb.checked ? 'on' : 'off'));
    });
  }

  /* ---- render one rail ---- */
  function render(rail) {
    const s = SOURCES[mod(rail.index)];
    const cap = '<figcaption class="rail-cap">' + s.label + '</figcaption>';

    if (s.kind === 'art' || s.kind === 'random') {
      const name = s.kind === 'art' ? s.src : ART[Math.floor(Math.random() * ART.length)];
      rail.fig.innerHTML = '<img class="rail-art" src="' + artUrl(name) + '" alt="' + (s.alt || '') + '">' + cap;
      saveState(rail);
      return;
    }
    rail.fig.innerHTML = '<div class="rail-loading">Loading&hellip;</div>' + cap;
    fetch(resolve(s.src))
      .then(r => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.text(); })
      .then(text => {
        const html = s.extract
          ? extract(text, s.extract, { rewrite: !!s.rewrite, stripIds: s.wire === 'settings' })
          : text;
        rail.fig.innerHTML = '<div class="rail-host' + (s.extract ? ' rail-wide' : '') + '">' + html + '</div>' + cap;
        resolveImgs(rail.fig);
        if (s.wire === 'settings') wireSettings(rail.fig);
      })
      .catch(err => {
        rail.fig.innerHTML = '<div class="rail-error">Could not load this panel.<br><small>' + err + '</small></div>' + cap;
      });
    saveState(rail);
  }

  /* ---- build a rail element + its controls ---- */
  function railMarkup(side) {
    return '<aside class="rail rail-' + side + '" data-open="true" aria-label="' + side + ' panel">' +
      '<div class="rail-inner">' +
        '<div class="rail-controls">' +
          '<button class="rc-pin"   type="button" title="Pin (protect from Push promo)" aria-pressed="false">&#9733;</button>' +
          '<button class="rc-open"  type="button" title="Show this panel">+</button>' +
          '<button class="rc-prev"  type="button" title="Previous source">&lt;</button>' +
          '<button class="rc-next"  type="button" title="Next source">&gt;</button>' +
          '<button class="rc-close" type="button" title="Hide this panel">&minus;</button>' +
        '</div>' +
        '<figure></figure>' +
      '</div></aside>';
  }

  function buildRail(side, fallbackId) {
    const wrap = document.createElement('div');
    wrap.innerHTML = railMarkup(side);
    const el = wrap.firstChild;
    const st = loadState(side, fallbackId);
    const rail = {
      side, el,
      fig: el.querySelector('figure'),
      index: indexOf(st.id),
      pinned: !!st.pinned,
      open: st.open !== false,
    };
    el.setAttribute('data-open', rail.open ? 'true' : 'false');
    const pin = el.querySelector('.rc-pin');
    pin.classList.toggle('pinned', rail.pinned);
    pin.setAttribute('aria-pressed', rail.pinned ? 'true' : 'false');

    el.querySelector('.rc-prev').addEventListener('click',  () => { rail.index = mod(rail.index - 1); render(rail); });
    el.querySelector('.rc-next').addEventListener('click',  () => { rail.index = mod(rail.index + 1); render(rail); });
    el.querySelector('.rc-close').addEventListener('click', () => { rail.open = false; el.setAttribute('data-open', 'false'); saveState(rail); });
    el.querySelector('.rc-open').addEventListener('click',  () => { rail.open = true;  el.setAttribute('data-open', 'true');  saveState(rail); });
    pin.addEventListener('click', () => {
      rail.pinned = !rail.pinned;
      pin.classList.toggle('pinned', rail.pinned);
      pin.setAttribute('aria-pressed', rail.pinned ? 'true' : 'false');
      saveState(rail);
    });
    return rail;
  }

  /* ---- Drag-to-resize handles (State 2 only). In symmetric mode both handles
     resize the centered column; in independent mode each sizes its own rail.
     Widths persist per mode; double-click a handle to reset it. ---- */
  function setupResize(layout, content) {
    const root = document.documentElement;
    const leftRail  = layout.querySelector('.rail-left');
    const rightRail = layout.querySelector('.rail-right');
    const MIN_CONTENT = 520, MIN_RAIL = 180, CONTENT_FLOOR = 380, EDGE = 80;

    const hL = document.createElement('div');
    hL.className = 'rail-resize rail-resize-left';
    hL.dataset.side = 'left';
    const hR = document.createElement('div');
    hR.className = 'rail-resize rail-resize-right';
    hR.dataset.side = 'right';
    layout.appendChild(hL);
    layout.appendChild(hR);

    function reposition() {
      const lr = layout.getBoundingClientRect();
      const cr = content.getBoundingClientRect();
      if (!cr.width) return;
      hL.style.left = (cr.left - lr.left) + 'px';
      hR.style.left = (cr.right - lr.left) + 'px';
    }

    function drag(x, side) {
      const mode = root.getAttribute('data-railmode') || 'symmetric';
      const vw = document.documentElement.clientWidth;
      if (mode === 'symmetric') {
        let w = 2 * Math.abs(x - vw / 2);
        w = Math.max(MIN_CONTENT, Math.min(w, vw - 2 * MIN_RAIL - EDGE));
        layout.style.setProperty('--content-w', Math.round(w) + 'px');
      } else if (side === 'left') {
        const other = parseFloat(getComputedStyle(layout).getPropertyValue('--rail-right-w')) || 240;
        let w = x - leftRail.getBoundingClientRect().left;
        w = Math.max(MIN_RAIL, Math.min(w, vw - other - CONTENT_FLOOR - EDGE));
        layout.style.setProperty('--rail-left-w', Math.round(w) + 'px');
      } else {
        const other = parseFloat(getComputedStyle(layout).getPropertyValue('--rail-left-w')) || 240;
        let w = rightRail.getBoundingClientRect().right - x;
        w = Math.max(MIN_RAIL, Math.min(w, vw - other - CONTENT_FLOOR - EDGE));
        layout.style.setProperty('--rail-right-w', Math.round(w) + 'px');
      }
      reposition();
    }

    function save() {
      const mode = root.getAttribute('data-railmode') || 'symmetric';
      const cs = getComputedStyle(layout);
      if (mode === 'symmetric') {
        const v = parseInt(cs.getPropertyValue('--content-w'), 10);
        if (v) localStorage.setItem('l1-content-width', v);
      } else {
        const l = parseInt(cs.getPropertyValue('--rail-left-w'), 10);
        const r = parseInt(cs.getPropertyValue('--rail-right-w'), 10);
        if (l) localStorage.setItem('l1-rail-left-width', l);
        if (r) localStorage.setItem('l1-rail-right-width', r);
      }
    }

    function onDown(e) {
      const h = e.currentTarget, side = h.dataset.side;
      e.preventDefault();
      h.setPointerCapture(e.pointerId);
      h.classList.add('dragging');
      document.body.classList.add('rails-resizing');
      const move = ev => drag(ev.clientX, side);
      const up = () => {
        h.classList.remove('dragging');
        document.body.classList.remove('rails-resizing');
        h.removeEventListener('pointermove', move);
        h.removeEventListener('pointerup', up);
        save();
      };
      h.addEventListener('pointermove', move);
      h.addEventListener('pointerup', up);
    }

    function reset(e) {
      const side = e.currentTarget.dataset.side;
      const mode = root.getAttribute('data-railmode') || 'symmetric';
      if (mode === 'symmetric') {
        layout.style.removeProperty('--content-w');
        localStorage.removeItem('l1-content-width');
      } else if (side === 'left') {
        layout.style.removeProperty('--rail-left-w');
        localStorage.removeItem('l1-rail-left-width');
      } else {
        layout.style.removeProperty('--rail-right-w');
        localStorage.removeItem('l1-rail-right-width');
      }
      reposition();
    }

    [hL, hR].forEach(h => {
      h.title = 'Drag to resize -- double-click to reset';
      h.addEventListener('pointerdown', onDown);
      h.addEventListener('dblclick', reset);
    });

    new ResizeObserver(reposition).observe(content);
    window.addEventListener('resize', reposition);
    reposition();
  }

  function init() {
    const layout = document.createElement('div');
    layout.className = 'reading-layout';
    layout.setAttribute('data-rails', 'on');
    layout.setAttribute('data-side', pref('railside', 'left'));

    // Apply any saved drag-resized widths (each resize mode keeps its own).
    const savedCW = localStorage.getItem('l1-content-width');
    if (savedCW) layout.style.setProperty('--content-w', savedCW + 'px');
    const savedLW = localStorage.getItem('l1-rail-left-width');
    if (savedLW) layout.style.setProperty('--rail-left-w', savedLW + 'px');
    const savedRW = localStorage.getItem('l1-rail-right-width');
    if (savedRW) layout.style.setProperty('--rail-right-w', savedRW + 'px');

    content.parentNode.insertBefore(layout, content);
    const left = buildRail('left', DEFAULTS.left);
    layout.appendChild(left.el);
    layout.appendChild(content);
    const right = buildRail('right', DEFAULTS.right);
    layout.appendChild(right.el);
    const rails = [left, right];
    rails.forEach(render);
    setupResize(layout, content);

    // Exposed for a future owner control / auto-rotation: retarget every
    // un-pinned, open rail to a random promo source.
    window.OneSRDRails = {
      pushPromo() {
        const promo = SOURCES.map((s, i) => s.promo ? i : -1).filter(i => i >= 0);
        if (!promo.length) return;
        rails.forEach(rail => {
          if (rail.pinned || !rail.open) return;
          rail.index = promo[Math.floor(Math.random() * promo.length)];
          render(rail);
        });
      }
    };
  }

  fetch(resolve('panels.json'))
    .then(r => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
    .then(cfg => {
      SOURCES  = cfg.sources || [];
      ART      = cfg.art || [];
      DEFAULTS = cfg.defaults || {};
      if (SOURCES.length) init();
    })
    .catch(err => console.warn('rails: panels.json failed to load:', err));

})();
