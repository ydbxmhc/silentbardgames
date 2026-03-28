// nav.js — fetches /nav.html, injects into #drawer, sets active state
(function () {

  const menuBtn = document.getElementById('menu-btn');
  const drawer  = document.getElementById('drawer');
  const overlay = document.getElementById('overlay');
  const body    = document.body;

  function openDrawer() {
    drawer.classList.add('open');
    drawer.setAttribute('aria-hidden', 'false');
    menuBtn.classList.add('open');
    menuBtn.setAttribute('aria-expanded', 'true');
    overlay.classList.add('visible');
    body.classList.add('drawer-open');
  }

  function closeDrawer() {
    drawer.classList.remove('open');
    drawer.setAttribute('aria-hidden', 'true');
    menuBtn.classList.remove('open');
    menuBtn.setAttribute('aria-expanded', 'false');
    overlay.classList.remove('visible');
    body.classList.remove('drawer-open');
  }

  function initDrawerEvents() {
    if (menuBtn) {
      menuBtn.addEventListener('click', () =>
        drawer.classList.contains('open') ? closeDrawer() : openDrawer()
      );
    }
    if (overlay) overlay.addEventListener('click', closeDrawer);

    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && drawer.classList.contains('open')) closeDrawer();
    });

    drawer.querySelectorAll('.nav-item').forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth < 900) closeDrawer();
      });
    });
  }

  function setActiveLink() {
    const path = window.location.pathname.replace(/\/$/, '') || '/index.html';
    drawer.querySelectorAll('.nav-item').forEach(link => {
      const href = link.getAttribute('href');
      if (!href) return;
      const linkPath = href.split('#')[0];
      if (linkPath === path || (path === '/' && linkPath === '/index.html')) {
        link.classList.add('active');
        const group = link.closest('.nav-group');
        if (group) group.setAttribute('open', '');
      }
    });
  }

  function resolveImgSrcs() {
    if (typeof SiteConfig !== 'undefined') {
      drawer.querySelectorAll('img[data-src]').forEach(el => {
        el.src = SiteConfig.CDN_BASE + '/' + el.dataset.src;
        el.removeAttribute('data-src');
      });
    }
  }

  fetch('/nav.html')
    .then(r => r.text())
    .then(html => {
      drawer.innerHTML = html;
      setActiveLink();
      resolveImgSrcs();
      initDrawerEvents();
    })
    .catch(err => {
      console.warn('nav.html failed to load:', err);
      initDrawerEvents();
    });

})();
