/* ============================================================
   LEVEL ONE RPG — SITE CONFIGURATION
   BASE_PATH tells nav.js where to fetch header.html and nav.html
   and where to root all relative nav links.

   Change CDN_BASE here to update all image references sitewide.
   When moving to a custom domain, update this one line:
     https://pub-e0f96c01318c4755b491bf481c530eb1.r2.dev
     → https://assets.silentbardgames.com
   ============================================================ */

const SiteConfig = {
  BASE_PATH: '/L1/',
  CDN_BASE:  'https://pub-e0f96c01318c4755b491bf481c530eb1.r2.dev',
  SITE_NAME: 'Level One RPG',
  SITE_URL:  'https://silentbardgames.com',
};

/* Helper — use this everywhere you need an image URL:
   img("roles/warrior.jpg")  →  full CDN URL */
function img(path) {
  return `${SiteConfig.CDN_BASE}/${path}`;
}

/* Auto-resolve any <img> with data-src attribute.
   Use data-src="filename.jpg" in HTML; this fills in the CDN URL on load. */
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('img[data-src]').forEach(el => {
    el.src = img(el.dataset.src);
    el.removeAttribute('data-src');
  });
});

/* ============================================================
   USER PREFERENCES
   Saves choices to localStorage under the "l1-" prefix.
   Applies data attributes to <html> so CSS can respond.

   Keys and their accepted values:
     l1-theme         default | dark | high-contrast | plain
     l1-fontsize      normal  | large | xl
     l1-navbg         on      | off
     l1-reducemotion  off     | on
     l1-rails         on      | off          (show side panels at all)
     l1-railside      left    | right        (which panel survives the squeeze)
     l1-railmode      symmetric | independent (resize: one centered handle vs two)

   CSS targets: html[data-theme="dark"] { ... } etc.
   See /resources/onesrd.css and /L1/style.css for the rules.
   ============================================================ */

const L1Prefs = {

  DEFAULTS: {
    theme:        'default',
    fontsize:     'normal',
    navbg:        'on',
    reducemotion: 'off',
    rails:        'on',
    railside:     'left',
    railmode:     'symmetric',
  },

  /* Read one preference (falls back to default if not set). */
  get(key) {
    return localStorage.getItem('l1-' + key) ?? this.DEFAULTS[key];
  },

  /* Write one preference and apply it immediately. */
  set(key, value) {
    localStorage.setItem('l1-' + key, value);
    this._apply(key, value);
  },

  /* Remove all preferences and revert to defaults. */
  reset() {
    Object.keys(this.DEFAULTS).forEach(key => {
      localStorage.removeItem('l1-' + key);
      this._apply(key, this.DEFAULTS[key]);
    });
  },

  /* Apply a single key as a data attribute on <html>. */
  _apply(key, value) {
    document.documentElement.setAttribute('data-' + key, value);
  },

  /* Apply all saved (or default) preferences at once. */
  applyAll() {
    Object.keys(this.DEFAULTS).forEach(key => {
      this._apply(key, this.get(key));
    });
  },

}; // end L1Prefs

/* Apply preferences as early as possible to minimise flash. */
L1Prefs.applyAll();
