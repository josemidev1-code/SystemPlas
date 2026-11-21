// SYSTEM PLAST: lo propio de la web (el resto lo hacen system.js, motion.js y layout.js del kit)

// Vídeo de la portada: botón de pausa y reposo con movimiento reducido
const video = document.querySelector('.hero video.hero__bg, video[data-bg-video]');
const pause = document.querySelector('[data-video-pause]');
if (video && pause) {
  const ICON_PAUSE = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M4 3h3v10H4zM9 3h3v10H9z"/></svg>';
  const ICON_PLAY = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3l8 5-8 5z"/></svg>';
  const set = (paused) => {
    pause.innerHTML = paused ? ICON_PLAY : ICON_PAUSE;
    pause.setAttribute('aria-pressed', String(paused));
    pause.setAttribute('aria-label', paused ? 'Reproducir el vídeo' : 'Pausar el vídeo');
  };
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) { video.removeAttribute('autoplay'); video.pause(); set(true); }
  else set(false);
  pause.addEventListener('click', () => {
    if (video.paused) { video.play(); set(false); } else { video.pause(); set(true); }
  });
}

const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)');

// Galería de la ficha de producto: la imagen nueva se carga antes y entra con un enfoque suave
const main = document.querySelector('[data-gallery-main]');
let swapId = 0;
document.querySelectorAll('[data-gallery-thumb]').forEach((b) => {
  b.addEventListener('click', async () => {
    document.querySelectorAll('[data-gallery-thumb]').forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
    if (!main || main.getAttribute('src') === b.dataset.src) return;
    const id = ++swapId;
    const next = new Image();
    next.src = b.dataset.src;
    try { await next.decode(); } catch (e) { /* se muestra igualmente */ }
    if (id !== swapId) return; // otro clic llegó antes
    main.removeAttribute('srcset');
    main.src = b.dataset.src;
    if (!reduceMotion.matches && main.animate) {
      main.animate(
        [{ opacity: 0, filter: 'blur(8px)', scale: '.97' }, { opacity: 1, filter: 'blur(0)', scale: '1' }],
        { duration: 420, easing: 'cubic-bezier(.16, 1, .3, 1)' }
      );
    }
  });
});

// Paso entre páginas: la foto del producto viaja de su tarjeta a la galería de su ficha (y vuelve).
// Aquí se nombra la foto de la página que se va; la de la que llega la nombra el script del <head> (build.py).
// Solo se nombra una imagen por página y solo mientras dura la transición.
const PHOTO = 'product-photo';
const samePage = (a, b) => { try { const x = new URL(a, location.href), y = new URL(b, location.href); return x.origin === y.origin && x.pathname.replace(/\/index\.html$/, '/') === y.pathname.replace(/\/index\.html$/, '/'); } catch (e) { return false; } };
const cardPhotoFor = (url) => {
  for (const a of document.querySelectorAll('a.card[href]')) {
    if (samePage(a.href, url)) { const img = a.querySelector('.frame__img, img'); if (img && img.getBoundingClientRect().height) return img; }
  }
  return null;
};
const inView = (el) => { const r = el.getBoundingClientRect(); return r.bottom > 0 && r.top < innerHeight; };
const name = (el, vt) => {
  if (!el || !inView(el)) return;
  el.style.viewTransitionName = PHOTO;
  const clear = () => { el.style.viewTransitionName = ''; };
  vt.finished.then(clear, clear);
};
addEventListener('pageswap', (e) => {
  if (!e.viewTransition || reduceMotion.matches || !e.activation) return;
  const to = e.activation.entry && e.activation.entry.url;
  if (to) name(cardPhotoFor(to) || main, e.viewTransition);
});

// Formulario de contacto: rellena producto y categoría si se llega desde una ficha (?producto=...&cat=...)
const form = document.querySelector('#contact-form');
if (form) {
  const q = new URLSearchParams(location.search);
  const cat = q.get('cat');
  const prod = q.get('producto');
  const sel = form.querySelector('#f-cat');
  if (cat && sel) [...sel.options].forEach((o) => { if (o.text === cat) sel.value = o.value; });
  if (prod) form.querySelector('#f-msg').value = `Me interesa recibir presupuesto de: ${prod}.\n\n`;
}

