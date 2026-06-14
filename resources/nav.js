// nav.js — shared OneSRD navigation loader
// Reads BASE_PATH from SiteConfig (defined in each game's config.js).
// Fetches header.html and nav.html from the game's BASE_PATH,
// injects them into #site-header and #drawer respectively.
(function () {

  const BASE   = (typeof SiteConfig !== 'undefined' && SiteConfig.BASE_PATH) || '/';
  const CDN    = (typeof SiteConfig !== 'undefined' && SiteConfig.CDN_BASE)  || '';

  const headerEl = document.getElementById('site-header');
  const drawer   = document.getElementById('drawer');
  const overlay  = document.getElementById('overlay');
  const body     = document.body;

  /* ---- Drawer open/close ---- */
  function openDrawer() {
    drawer.classList.add('open');
    drawer.setAttribute('aria-hidden', 'false');
    const btn = document.getElementById('menu-btn');
    if (btn) { btn.classList.add('open'); btn.setAttribute('aria-expanded', 'true'); }
    if (overlay) overlay.classList.add('visible');
    body.classList.add('drawer-open');
  }

  function closeDrawer() {
    drawer.classList.remove('open');
    drawer.setAttribute('aria-hidden', 'true');
    const btn = document.getElementById('menu-btn');
    if (btn) { btn.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }
    if (overlay) overlay.classList.remove('visible');
    body.classList.remove('drawer-open');
  }

  function initDrawerEvents() {
    // Menu button and global events are bound elsewhere to avoid duplicates.
    const closeBtn = drawer.querySelector('.drawer-close-btn');
    if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
    drawer.querySelectorAll('.nav-item').forEach(link => {
      link.addEventListener('click', () => { if (window.innerWidth < 900) closeDrawer(); });
    });
  }

  /* ---- Active link highlighting ---- */
  function setActiveLink() {
    const path = window.location.pathname.replace(/\/$/, '') || '/';
    drawer.querySelectorAll('.nav-item').forEach(link => {
      const href = link.getAttribute('href');
      if (!href) return;
      const linkPath = href.split('#')[0];
      if (linkPath === path || (path === BASE.replace(/\/$/, '') && linkPath === BASE + 'index.html')) {
        link.classList.add('active');
        const group = link.closest('.nav-group');
        if (group) group.setAttribute('open', '');
      }
    });
  }

  /* ---- Rewrite relative nav hrefs to BASE_PATH-absolute ---- */
  function rewriteNavLinks() {
    drawer.querySelectorAll('a[href]').forEach(link => {
      const href = link.getAttribute('href');
      // Rewrite only relative (non-absolute, non-hash) links
      if (href && !href.startsWith('http') && !href.startsWith('/') && !href.startsWith('#')) {
        link.setAttribute('href', BASE + href);
      }
    });
  }

  /* ---- Resolve CDN image data-src attributes ---- */
  function resolveImgSrcs(root) {
    if (CDN) {
      root.querySelectorAll('img[data-src]').forEach(el => {
        el.src = CDN + '/' + el.dataset.src;
        el.removeAttribute('data-src');
      });
    }
  }

  /* ---- Load header.html into #site-header ---- */
  function loadHeader() {
    if (!headerEl) return Promise.resolve();
    return fetch(BASE + 'header.html')
      .then(r => r.text())
      .then(html => {
        headerEl.innerHTML = html;
        resolveImgSrcs(headerEl);
        // Re-bind menu button after header injects it
        initMenuBtn();
      })
      .catch(err => console.warn('header.html failed to load:', err));
  }

  /* ---- Bind just the menu button (called after header loads) ---- */
  function initMenuBtn() {
    const btn = document.getElementById('menu-btn');
    if (!btn) return;
    btn.addEventListener('click', () =>
      drawer.classList.contains('open') ? closeDrawer() : openDrawer()
    );
  }

  /* ---- Load nav.html into #drawer ---- */
  function loadNav() {
    if (!drawer) return Promise.resolve();
    return fetch(BASE + 'nav.html')
      .then(r => r.text())
      .then(html => {
        drawer.innerHTML = html;
        rewriteNavLinks();
        setActiveLink();
        resolveImgSrcs(drawer);
        initDrawerEvents();
      })
      .catch(err => {
        console.warn('nav.html failed to load:', err);
        initDrawerEvents();
      });
  }

  /* ---- Kick everything off in parallel ---- */
  loadHeader();
  loadNav();

  /* ---- Overlay click always works regardless of load state ---- */
  if (overlay) overlay.addEventListener('click', closeDrawer);
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && drawer && drawer.classList.contains('open')) closeDrawer();
  });

})();
