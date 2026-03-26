// Shared drawer navigation script
// config.js must be loaded before this file

(function() {
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

  if (menuBtn) {
    menuBtn.addEventListener('click', () =>
      drawer.classList.contains('open') ? closeDrawer() : openDrawer()
    );
  }
  if (overlay) overlay.addEventListener('click', closeDrawer);

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && drawer && drawer.classList.contains('open')) closeDrawer();
  });

  // Close on nav link click (mobile)
  if (drawer) {
    drawer.querySelectorAll('.nav-item').forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth < 900) closeDrawer();
      });
    });
  }

  // Auto-open nav-group for active page
  document.querySelectorAll('.nav-group').forEach(group => {
    if (group.querySelector('.active')) group.setAttribute('open', '');
  });
})();
