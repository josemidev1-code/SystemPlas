// SYSTEM PLAST: vídeos EOAT en formato vertical. Cada uno se reproduce solo mientras está en pantalla
// (los vídeos no son texto: nada queda oculto), con su botón de pausa. Con movimiento reducido no arranca
// ninguno solo: se ven quietos y se reproducen al pulsar.
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const PAUSE = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M4 3h3v10H4zM9 3h3v10H9z"/></svg>';
const PLAY = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3l8 5-8 5z"/></svg>';
document.querySelectorAll('.reel').forEach((reel) => {
  const v = reel.querySelector('video'), b = reel.querySelector('[data-reel-btn]');
  if (!v || !b) return;
  const name = v.getAttribute('aria-label') || 'vídeo';
  let held = reduce; // pausado por la persona (o por movimiento reducido)
  const show = () => {
    const on = !v.paused;
    b.innerHTML = on ? PAUSE : PLAY;
    b.setAttribute('aria-pressed', String(!on));
    b.setAttribute('aria-label', `${on ? 'Pausar' : 'Reproducir'}: ${name}`);
    reel.classList.toggle('is-playing', on);
  };
  v.addEventListener('play', show); v.addEventListener('pause', show); show();
  b.addEventListener('click', () => { if (v.paused) { held = false; v.play().catch(() => {}); } else { held = true; v.pause(); } });
  if (!reduce && 'IntersectionObserver' in window) {
    new IntersectionObserver((es) => es.forEach((e) => {
      if (e.isIntersecting && !held) v.play().catch(() => {}); else if (!e.isIntersecting) v.pause();
    }), { threshold: 0.4 }).observe(v);
  }
});
