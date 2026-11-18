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

// Galería de la ficha de producto
const main = document.querySelector('[data-gallery-main]');
document.querySelectorAll('[data-gallery-thumb]').forEach((b) => {
  b.addEventListener('click', () => {
    main.src = b.dataset.src;
    document.querySelectorAll('[data-gallery-thumb]').forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
  });
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

// Índice del catálogo en portada: marca la línea que se está viendo (sin JS, los enlaces funcionan igual)
const index = document.querySelector('.cat-index');
if (index && 'IntersectionObserver' in window) {
  const links = new Map([...index.querySelectorAll('a[href^="#"]')].map((a) => [a.hash.slice(1), a]));
  const seen = new Map();
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => seen.set(e.target.id, e.isIntersecting));
    const current = [...links.keys()].find((id) => seen.get(id));
    links.forEach((a, id) => (id === current ? a.setAttribute('aria-current', 'true') : a.removeAttribute('aria-current')));
  }, { rootMargin: '-45% 0px -50% 0px' });
  links.forEach((_, id) => { const s = document.getElementById(id); if (s) io.observe(s); });
}

// En el móvil el índice se desplaza en horizontal: la línea activa queda siempre a la vista
if (index) {
  const bar = index.querySelector('.wrap');
  new MutationObserver(() => {
    const a = index.querySelector('a[aria-current]');
    if (a && bar.scrollWidth > bar.clientWidth) bar.scrollTo({ left: a.offsetLeft - 24, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
  }).observe(index, { subtree: true, attributeFilter: ['aria-current'] });
}
