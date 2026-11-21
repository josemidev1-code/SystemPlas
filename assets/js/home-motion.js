// SYSTEM PLAST, portada: decoración y cifras al entrar en pantalla. No oculta texto: los emblemas son
// decorativos (aria-hidden) y las cifras siempre muestran un número.
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)');
// Portada: dos momentos al entrar en pantalla, una sola vez. Sin script, o con movimiento reducido,
// todo está ya en su estado final (las cifras y los emblemas se ven desde el principio).
if (!reduceMotion.matches && 'IntersectionObserver' in window) {
  const once = (els, run, opts = { threshold: 0.35 }) => {
    const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { io.unobserve(e.target); run(e.target); } }), opts);
    els.forEach((el) => io.observe(el));
  };
  // las cifras cuentan hasta su valor (ease-out, 1,1 s)
  const counts = [...document.querySelectorAll('[data-count]')];
  if (counts.length) {
    const fmt = (el, v) => `${el.dataset.prefix || ''}${v}${el.dataset.suffix || ''}`;
    counts.forEach((el) => { el.style.minWidth = `${el.offsetWidth}px`; el.textContent = fmt(el, 0); });
    once([document.querySelector('.stats')], () => {
      const t0 = performance.now(), dur = 1100;
      const tick = (t) => {
        const k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 4);
        counts.forEach((el) => { el.textContent = fmt(el, Math.round(+el.dataset.count * e)); });
        if (k < 1) requestAnimationFrame(tick); else counts.forEach((el) => { el.textContent = fmt(el, el.dataset.count); });
      };
      requestAnimationFrame(tick);
    });
  }
  // los emblemas de servicio se trazan: el marco se revela de arriba abajo y el pictograma llega después
  const svc = document.querySelector('.svc');
  if (svc) {
    svc.classList.add('is-armed');
    once([svc], (el) => el.classList.add('is-in'), { threshold: 0.25 });
  }
}
