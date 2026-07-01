/* ============================================================
   TESSERAE SORTIS - SITE CONFIGURATION
   BASE_PATH tells nav.js where to fetch header.html and nav.html
   and where to root all relative nav links.

   Mirrors the /L1/ pattern. Preferences are namespaced under
   the "ts-" localStorage prefix so they don't collide with L1.
   ============================================================ */

const SiteConfig = {
  BASE_PATH: '/TS/',
  CDN_BASE:  'https://pub-e0f96c01318c4755b491bf481c530eb1.r2.dev',
  SITE_NAME: 'Tesserae Sortis',
  SITE_URL:  'https://silentbardgames.com',
};

/* Helper - use this everywhere you need an image URL:
   img("foo.jpg")  →  full CDN URL */
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
   Saves choices to localStorage under the "ts-" prefix.
   Applies data attributes to <html> so CSS can respond.

   Keys and their accepted values:
     ts-theme         default | dark | high-contrast | plain
     ts-fontsize      normal  | large | xl
     ts-navbg         on      | off
     ts-reducemotion  off     | on
     ts-rails         on      | off          (show side panels at all)
     ts-railside      left    | right        (which panel survives the squeeze)
     ts-railmode      symmetric | independent (resize: one centered handle vs two)

   CSS targets: html[data-theme="dark"] { ... } etc.
   See /resources/onesrd.css and /TS/style.css for the rules.
   ============================================================ */

const TSPrefs = {

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
    return localStorage.getItem('ts-' + key) ?? this.DEFAULTS[key];
  },

  /* Write one preference and apply it immediately. */
  set(key, value) {
    localStorage.setItem('ts-' + key, value);
    this._apply(key, value);
  },

  /* Remove all preferences and revert to defaults. */
  reset() {
    Object.keys(this.DEFAULTS).forEach(key => {
      localStorage.removeItem('ts-' + key);
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

}; // end TSPrefs

/* Apply preferences as early as possible to minimise flash. */
TSPrefs.applyAll();
