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
