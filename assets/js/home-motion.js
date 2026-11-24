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
  // los dibujos (líneas de producto y servicios) aparecen uno tras otro, subiendo sobre su sombra
  const sets = [...document.querySelectorAll('.emb-set')];
  sets.forEach((el) => el.classList.add('is-armed'));
  once(sets, (el) => el.classList.add('is-in'), { threshold: 0.25 });
}

// Portada: el registro del robot escribe una línea nueva cada 2,2 s con la hora real (decorativo, aria-hidden).
// Con movimiento reducido se queda con las cuatro líneas escritas en el HTML.
const log = document.querySelector('[data-hud-log] ol');
if (log && !reduceMotion.matches) {
  const steps = ['Ciclo {n} · inicio', 'Bajada al molde · Z 412 mm', 'Vacío correcto · −0,82 bar', 'Pieza extraída del molde', 'Depósito en cinta', 'Ciclo completado · 6,2 s'];
  let k = 0, n = 419;
  const two = (v) => String(v).padStart(2, '0');
  const tick = () => {
    if (document.hidden) return;
    const d = new Date(), li = document.createElement('li'), t = document.createElement('time');
    t.textContent = `${two(d.getHours())}:${two(d.getMinutes())}:${two(d.getSeconds())}`;
    li.append(t, ` ${steps[k].replace('{n}', String(n).padStart(4, '0'))}`);
    li.className = 'is-new';
    log.append(li);
    while (log.children.length > 4) log.firstElementChild.remove();
    k = (k + 1) % steps.length; if (k === 0) n++;
  };
  setInterval(tick, 2200);
}
