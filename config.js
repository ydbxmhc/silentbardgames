/* ============================================================
   LEVEL ONE RPG — SITE CONFIGURATION
   Change CDN_BASE here to update all image references sitewide.
   When moving to a custom domain, update this one line:
     https://pub-e0f96c01318c4755b491bf481c530eb1.r2.dev
     → https://assets.silentbardgames.com
   ============================================================ */

const SiteConfig = {
  CDN_BASE: "https://pub-e0f96c01318c4755b491bf481c530eb1.r2.dev",
  SITE_NAME: "Level One RPG",
  SITE_URL: "https://silentbardgames.com",
};

/* Helper — use this everywhere you need an image URL:
   img(filename)  →  full CDN URL

   Example:
     <img src="" data-src="roles/warrior.jpg" class="cdn-img">
   Or in JS:
     document.querySelector('img').src = img("roles/warrior.jpg");
*/
function img(path) {
  return `${SiteConfig.CDN_BASE}/${path}`;
}

/* Auto-resolve any <img> with data-src attribute.
   Use data-src="filename.jpg" instead of src="" in HTML,
   and this script will fill in the full CDN URL on load. */
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("img[data-src]").forEach(el => {
    el.src = img(el.dataset.src);
    el.removeAttribute("data-src");
  });
});
