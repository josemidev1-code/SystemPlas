// Catálogo 3D: inyectora genérica (CC0) como escenario y accesorios System Plast montados en sus nodos.
// Datos: <script type="application/json" id="cat3d-data"> generado por build.py desde data/accesorios3d.json.
// Si falta el GLB de un accesorio se dibuja un volumen translúcido en su lugar ("modelo en preparación").
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';

const root = document.querySelector('[data-cat3d]');
const data = JSON.parse(document.getElementById('cat3d-data').textContent);
const stage = root.querySelector('[data-cat3d-stage]');
const statusEl = root.querySelector('[data-cat3d-status]');
const panel = root.querySelector('[data-cat3d-panel]');
const listBtns = [...root.querySelectorAll('[data-cat3d-item]')];
const resetBtn = root.querySelector('[data-cat3d-reset]');

const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
const coarse = matchMedia('(pointer: coarse)').matches;
const qualityEl = root.querySelector('[data-cat3d-quality]');
const QUALITY_KEY = 'systemplast-cat3d-quality';
let choice = 'auto';
try { choice = new URLSearchParams(location.search).get('calidad') || localStorage.getItem(QUALITY_KEY) || 'auto'; } catch {}
if (!['auto', 'static', 'medium', 'high'].includes(choice)) choice = 'auto';
qualityEl.value = choice;
qualityEl.addEventListener('change', () => { try { localStorage.setItem(QUALITY_KEY, qualityEl.value); } catch {} const url = new URL(location.href); url.searchParams.set('calidad', qualityEl.value); location.assign(url); });
const memory = navigator.deviceMemory || 8;
const cores = navigator.hardwareConcurrency || 4;
let quality = choice === 'auto' ? (navigator.connection?.saveData || memory <= 2 ? 'static' : coarse || memory <= 4 || cores <= 4 ? 'medium' : 'high') : choice;
root.dataset.cat3dQuality = quality;
const api = window.__cat3d = { ready: false, error: null, selected: null, accesorios: {}, contexts: 0 };

const ACCENT = new THREE.Color(getComputedStyle(root).getPropertyValue('--p-accent').trim() || '#037c75');
const css = n => getComputedStyle(stage).getPropertyValue(n).trim();

function webglOk() {
  try { const c = document.createElement('canvas'); const gl = c.getContext('webgl2'); if (!gl) return false; gl.getExtension('WEBGL_lose_context')?.loseContext(); return true; } catch (e) { return false; }
}

function setStatus(t, kind = '') { statusEl.textContent = t; statusEl.dataset.kind = kind; }

// ---------------------------------------------------------------------------------------------------
// Arranque diferido: Three.js y los GLB solo se cargan cuando la escena entra en pantalla
// ---------------------------------------------------------------------------------------------------
if (quality === 'static' || !webglOk()) {
  root.dataset.cat3dState = 'fallback';
  setStatus('Vista estática: consulte las fichas de los accesorios o seleccione una calidad 3D.', 'warn');
} else {
  if (!('IntersectionObserver' in window)) init().catch(fail);
  else { const io = new IntersectionObserver(es => { if (es.some(e => e.isIntersecting)) { io.disconnect(); init().catch(fail); } }, { rootMargin: '300px' });
  io.observe(stage); }
}

function fail(e) {
  console.error(e);
  api.ready = false;
  api.error = String(e && e.message || e);
  root.dataset.cat3dState = 'fallback';
  setStatus('No se ha podido cargar la máquina 3D. Se muestra una imagen fija.', 'warn');
}

async function init() {
  root.dataset.cat3dState = 'loading';
  setStatus('Cargando la máquina…');

  const renderer = new THREE.WebGLRenderer({ antialias: quality === 'high', alpha: false, powerPreference: quality === 'high' ? 'high-performance' : 'low-power' });
  api.contexts++;
  renderer.setPixelRatio(Math.min(devicePixelRatio || 1, quality === 'high' ? 2 : 1));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.05;
  renderer.shadowMap.enabled = quality === 'high';
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  const canvas = renderer.domElement;
  canvas.className = 'cat3d__canvas';
  canvas.setAttribute('role', 'img');
  canvas.setAttribute('aria-label', 'Inyectora en 3D con los accesorios System Plast montados. Use la lista para seleccionarlos.');
  stage.append(canvas);
  canvas.addEventListener('webglcontextlost', e => { e.preventDefault(); fail(new Error('Contexto WebGL perdido')); });

  const scene = new THREE.Scene();
  const bg = new THREE.Color(css('--cat3d-bg') || '#e5e7e7');
  scene.background = bg;
  if (quality === 'high') { const pmrem = new THREE.PMREMGenerator(renderer); const room = new RoomEnvironment(); scene.environment = pmrem.fromScene(room, 0.04).texture; room.dispose(); pmrem.dispose(); }

  const sun = new THREE.DirectionalLight(0xffffff, 1.5);
  sun.position.set(2.5, 6, 3.5);
  sun.castShadow = renderer.shadowMap.enabled;
  sun.shadow.mapSize.set(1024, 1024);
  Object.assign(sun.shadow.camera, { left: -3.2, right: 3.2, top: 3, bottom: -3, near: 1, far: 14 });
  sun.shadow.bias = -0.0005;
  scene.add(sun, new THREE.HemisphereLight(0xffffff, 0x9aa1a4, quality === 'high' ? 0.35 : 1.5));

  const floor = new THREE.Mesh(new THREE.CircleGeometry(7, 48), new THREE.ShadowMaterial({ opacity: 0.16 }));
  floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true; scene.add(floor);

  const camera = new THREE.PerspectiveCamera(34, 1, 0.05, 60);
  const controls = new OrbitControls(camera, canvas);
  Object.assign(controls, { enableDamping: !reduced, dampingFactor: 0.08, minDistance: 0.6, maxDistance: 9, maxPolarAngle: Math.PI * 0.49, screenSpacePanning: true });

  // ---- render bajo demanda -------------------------------------------------------------------------
  let needs = true, raf = 0, lastFrame = 0, slowFrames = 0;
  const request = () => { needs = true; if (!raf) raf = requestAnimationFrame(frame); };
  function frame(t) {
    raf = 0;
    const moving = tween && stepTween(t);
    const damp = controls.update();
    if (root.dataset.cat3dState === 'fallback') return;
    if (needs || moving || damp) {
      if (choice === 'auto' && lastFrame && t - lastFrame < 250) {
        slowFrames = t - lastFrame > 48 ? slowFrames + 1 : Math.max(0, slowFrames - 1);
        if (slowFrames >= 12) {
          slowFrames = 0;
          if (quality === 'high') { quality = 'medium'; root.dataset.cat3dQuality = quality; renderer.setPixelRatio(1); renderer.shadowMap.enabled = false; sun.castShadow = false; resize(); }
          else { fail(new Error('Rendimiento 3D insuficiente')); renderer.dispose(); return; }
        }
      }
      lastFrame = t; renderer.render(scene, camera); needs = false;
    }
    if (moving || damp) raf = requestAnimationFrame(frame);
  }
  controls.addEventListener('change', request);

  function resize() {
    const w = stage.clientWidth, h = stage.clientHeight;
    if (!w || !h) return;
    renderer.setSize(w, h, false);
    camera.aspect = w / h; camera.updateProjectionMatrix();
    request();
  }
  new ResizeObserver(resize).observe(stage);

  // ---- vistas y transiciones de cámara ------------------------------------------------------------
  let tween = null;
  function viewFor(name) {
    const v = data.vistas[name] || data.vistas.general;
    const pos = new THREE.Vector3(...v.pos), target = new THREE.Vector3(...v.target);
    const k = camera.aspect < 1.25 ? Math.min(1.9, 1.25 / camera.aspect) : 1; // marco estrecho: alejar
    pos.sub(target).multiplyScalar(k).add(target);
    return { pos, target };
  }
  function goTo(name, instant = reduced) {
    const to = viewFor(name);
    if (instant) { camera.position.copy(to.pos); controls.target.copy(to.target); tween = null; controls.update(); request(); return; }
    tween = { t0: performance.now(), dur: 750, p0: camera.position.clone(), q0: controls.target.clone(), ...to };
    request();
  }
  function stepTween(t) {
    const k = Math.min(1, (t - tween.t0) / tween.dur), e = k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2;
    camera.position.lerpVectors(tween.p0, tween.pos, e); controls.target.lerpVectors(tween.q0, tween.target, e);
    if (k >= 1) tween = null;
    return true;
  }

  // ---- máquina ------------------------------------------------------------------------------------
  const loader = new GLTFLoader().setMeshoptDecoder(MeshoptDecoder);
  const gltf = await loader.loadAsync(data.maquina.glb);
  const machine = gltf.scene;
  machine.traverse(o => {
    if (!o.isMesh) return;
    o.castShadow = o.receiveShadow = renderer.shadowMap.enabled;
    // vidrio con transmisión = una pasada de render más; un transparente simple se ve igual a esta escala
    if (o.material && o.material.name === 'glass') {
      o.material = new THREE.MeshStandardMaterial({ color: 0xdfe8ec, metalness: 0, roughness: 0.1, transparent: true, opacity: 0.2, depthWrite: false, side: THREE.DoubleSide, name: 'glass' });
      o.castShadow = false;
    }
  });
  scene.add(machine);
  scene.add(robotScenery(machine));
  resize();
  goTo('general', true);

  // ---- accesorios ---------------------------------------------------------------------------------
  const pickables = [];
  const groups = {};   // id -> { holders: [Group], extras: [Object3D], variant, placeholder }
  for (const acc of data.accesorios) {
    groups[acc.id] = { holders: [], extras: [], variant: null, placeholder: false };
    for (const m of acc.montajes) {
      const node = machine.getObjectByName(m);
      if (!node) { console.warn('cat3d: falta el nodo', m); continue; }
      const h = new THREE.Group(); h.name = 'ACC_' + acc.id; h.userData.accId = acc.id;
      if (acc.ajuste.desplazamiento) h.position.set(...acc.ajuste.desplazamiento);
      node.add(h); groups[acc.id].holders.push(h); pickables.push(h);
    }
    if (acc.extras && acc.extras.includes('carro')) {
      const c = hrsCart(); c.userData.accId = acc.id; machine.getObjectByName(acc.montajes[0]).add(c); groups[acc.id].extras.push(c); pickables.push(c);
    }
    if (acc.extras && acc.extras.includes('cable')) {
      const c = hrsCable(machine); if (c) { c.userData.accId = acc.id; scene.add(c); groups[acc.id].extras.push(c); pickables.push(c); }
    }
  }

  // Las variantes verificadas y las aproximaciones explícitas se montan en coordenadas locales.
  // Las restantes conservan un volumen provisional.
  async function loadVariant(acc, variant) {
    const g = groups[acc.id];
    g.variant = variant.id;
    let model = null;
    if ((variant.disponible && variant.validado) || (variant.disponible && variant.aproximacion)) {
      try { model = (await loader.loadAsync(variant.glb)).scene; } catch (e) { console.warn('cat3d: no se pudo cargar', variant.glb, e); model = null; }
    }
    if (g.variant !== variant.id) return; // se cambió de variante mientras cargaba
    g.placeholder = !model;
    for (const h of g.holders) {
      h.clear();
      const obj = model ? model.clone(true) : placeholder(acc);
      obj.traverse(o => { if (o.isMesh) { o.castShadow = renderer.shadowMap.enabled && !g.placeholder; o.material = o.material.clone(); } });
      h.add(obj);
    }
    const estado = model ? (variant.validado ? 'glb' : 'aproximacion') : variant.disponible ? 'sin-validar' : 'pendiente';
    api.accesorios[acc.id] = { variante: variant.id, modelo: estado, instancias: g.holders.length };
    syncPanel(); request();
  }

  function placeholder(acc) {
    const [x, y, z] = acc.ajuste.caja;
    const mat = new THREE.MeshStandardMaterial({ color: ACCENT, transparent: true, opacity: 0.32, roughness: 0.6, metalness: 0, depthWrite: false });
    const edge = new THREE.LineBasicMaterial({ color: ACCENT, transparent: true, opacity: 0.9 });
    const g = new THREE.Group(); g.userData.placeholder = true;
    let geo;
    if (acc.ajuste.tipo === 'anillo') {
      const ro = y / 2, ri = (acc.ajuste.diametro_int || y * 0.75) / 2 + 0.004, hw = x / 2;
      geo = new THREE.LatheGeometry([new THREE.Vector2(ri, -hw), new THREE.Vector2(ro, -hw), new THREE.Vector2(ro, hw), new THREE.Vector2(ri, hw), new THREE.Vector2(ri, -hw)], 40);
      geo.rotateZ(-Math.PI / 2);
    } else {
      geo = new THREE.BoxGeometry(x, y, z);
      if (acc.ajuste.apoyo === 'base') geo.translate(0, y / 2, 0);
    }
    g.add(new THREE.Mesh(geo, mat));
    g.add(new THREE.LineSegments(new THREE.EdgesGeometry(geo, 30), edge));
    return g;
  }

  await Promise.all(data.accesorios.map(a => loadVariant(a, a.variantes[0])));

  // ---- selección -----------------------------------------------------------------------------------
  const ray = new THREE.Raycaster(), ndc = new THREE.Vector2();
  let hoverId = null;
  function pick(ev) {
    const r = canvas.getBoundingClientRect();
    ndc.set(((ev.clientX - r.left) / r.width) * 2 - 1, -((ev.clientY - r.top) / r.height) * 2 + 1);
    ray.setFromCamera(ndc, camera);
    const hit = ray.intersectObjects(pickables, true).find(h => h.object.visible && (h.object.isMesh));
    if (!hit) return null;
    for (let o = hit.object; o; o = o.parent) if (o.userData.accId) return o.userData.accId;
    return null;
  }
  function tint(id, level) { // 0 nada, 1 hover, 2 seleccionado
    const g = groups[id]; if (!g) return;
    for (const o of [...g.holders, ...g.extras]) o.traverse(m => {
      if (!m.isMesh || !m.material) return;
      const mat = m.material;
      if (mat.emissive) { mat.emissive.copy(ACCENT); mat.emissiveIntensity = [0, 0.18, 0.35][level]; }
      if (m.parent && m.parent.userData.placeholder && mat.opacity !== undefined && mat.transparent && !m.isLineSegments) mat.opacity = [0.32, 0.45, 0.6][level];
    });
  }
  function refreshTints() { for (const id in groups) tint(id, id === api.selected ? 2 : id === hoverId ? 1 : 0); request(); }

  let down = null;
  canvas.addEventListener('pointerdown', e => { down = { x: e.clientX, y: e.clientY, t: performance.now() }; });
  canvas.addEventListener('pointerup', e => {
    if (!down) return;
    const moved = Math.hypot(e.clientX - down.x, e.clientY - down.y), dt = performance.now() - down.t; down = null;
    if (moved > 6 || dt > 600) return;
    const id = pick(e);
    if (id) select(id); else if (api.selected) select(null);
  });
  if (!coarse) canvas.addEventListener('pointermove', e => {
    if (e.buttons) return;
    const id = pick(e);
    if (id !== hoverId) { hoverId = id; canvas.style.cursor = id ? 'pointer' : ''; refreshTints(); }
  });
  canvas.addEventListener('pointerleave', () => { if (hoverId) { hoverId = null; canvas.style.cursor = ''; refreshTints(); } });

  function select(id) {
    api.selected = id;
    const acc = data.accesorios.find(a => a.id === id);
    goTo(acc ? acc.vista : 'general');
    for (const b of listBtns) b.setAttribute('aria-pressed', String(b.dataset.cat3dItem === id));
    refreshTints(); syncPanel();
  }

  function syncPanel() {
    const acc = data.accesorios.find(a => a.id === api.selected);
    panel.hidden = !acc;
    resetBtn.hidden = !acc;
    for (const b of listBtns) {
      const st = api.accesorios[b.dataset.cat3dItem];
      const chip = b.querySelector('[data-cat3d-chip]');
      if (chip && st) chip.textContent = st.modelo === 'glb' ? '' : st.modelo === 'aproximacion' ? 'Modelo orientativo' : st.modelo === 'sin-validar' ? 'Modelo en validación' : 'Modelo en preparación';
    }
    if (!acc) return;
    const g = groups[acc.id], v = acc.variantes.find(x => x.id === g.variant) || acc.variantes[0];
    panel.querySelector('[data-cat3d-name]').textContent = acc.nombre;
    panel.querySelector('[data-cat3d-variant]').textContent = v.nombre;
    panel.querySelector('[data-cat3d-text]').textContent = v.texto || '';
    const pendEl = panel.querySelector('[data-cat3d-pending]');
    pendEl.hidden = !g.placeholder && !v.aproximacion;
    pendEl.textContent = v.aproximacion && !g.placeholder ? "Representación orientativa: dimensiones y encaje pendientes de validación industrial. " + (v.aviso || "") : v.disponible && !v.validado
      ? 'Modelo 3D en validación: hasta comprobar su encaje en la máquina, el volumen marca su posición y su tamaño aproximado.'
      : 'Modelo 3D en preparación: el volumen marca su posición y su tamaño aproximado.';
    const link = panel.querySelector('[data-cat3d-link]'); link.href = v.url; link.querySelector('span').textContent = v.enlace;
    panel.querySelector('[data-cat3d-quote]').href = v.presupuesto;
    const vs = panel.querySelector('[data-cat3d-variants]');
    const refocus = vs.contains(document.activeElement);
    vs.hidden = acc.variantes.length < 2;
    vs.replaceChildren(...acc.variantes.map(x => {
      const b = document.createElement('button');
      b.type = 'button'; b.className = 'cat3d__chipbtn'; b.textContent = x.nombre;
      b.setAttribute('aria-pressed', String(x.id === g.variant));
      b.addEventListener('click', () => { if (x.id !== g.variant) loadVariant(acc, x).then(() => refreshTints()); });
      return b;
    }));
    if (refocus) vs.querySelector('[aria-pressed="true"]')?.focus();
  }

  for (const b of listBtns) b.addEventListener('click', () => {
    select(b.dataset.cat3dItem === api.selected ? null : b.dataset.cat3dItem);
    // en una columna la lista queda bajo la escena: llevarla a la vista para ver el cambio de cámara
    const r = stage.getBoundingClientRect();
    if (r.bottom > innerHeight || r.top < 0) stage.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'start' });
  });
  resetBtn.addEventListener('click', () => select(null));
  root.addEventListener('keydown', e => { if (e.key === 'Escape' && api.selected) select(null); });
  document.addEventListener('visibilitychange', () => { if (!document.hidden) request(); });

  root.dataset.cat3dState = 'ready';
  const pend = Object.values(api.accesorios).filter(a => !['glb', 'aproximacion'].includes(a.modelo)).length;
  setStatus(pend ? `Máquina lista. ${pend} de ${data.accesorios.length} accesorios se muestran como volumen mientras preparamos su modelo.` : 'Máquina y accesorios listos. Los modelos orientativos no están certificados dimensionalmente.');
  api.ready = true; api.quality = () => quality;
  api.select = select;
  api.info = () => ({ calls: renderer.info.render.calls, triangles: renderer.info.render.triangles, textures: renderer.info.memory.textures, geometries: renderer.info.memory.geometries });
  api.renderNow = () => renderer.render(scene, camera);
  // para pruebas: caja en mundo (m) de cada montaje de un accesorio
  api.bounds = id => (groups[id] ? groups[id].holders : []).map(h => { const b = new THREE.Box3().setFromObject(h); return { min: b.min.toArray().map(v => +v.toFixed(3)), max: b.max.toArray().map(v => +v.toFixed(3)) }; });
  // para pruebas: punto de pantalla (CSS px) del primer montaje de un accesorio
  api.screenPoint = id => {
    const h = groups[id] && groups[id].holders[0]; if (!h) return null;
    const v = h.getWorldPosition(new THREE.Vector3()).project(camera), r = canvas.getBoundingClientRect();
    return { x: r.left + (v.x + 1) / 2 * r.width, y: r.top + (1 - v.y) / 2 * r.height };
  };
  request();
}

// ---------------------------------------------------------------------------------------------------
// Escenario: robot cartesiano genérico (no es producto), carro y cable del HRS
// ---------------------------------------------------------------------------------------------------
function boxFrom(min, max, mat) {
  const s = max.map((v, i) => v - min[i]);
  const m = new THREE.Mesh(new THREE.BoxGeometry(...s), mat);
  m.position.set(...min.map((v, i) => v + s[i] / 2));
  m.castShadow = m.receiveShadow = true;
  return m;
}
function robotScenery() {
  const body = new THREE.MeshStandardMaterial({ color: 0xc9ced0, metalness: 0.3, roughness: 0.45 });
  const dark = new THREE.MeshStandardMaterial({ color: 0x2b3033, metalness: 0.4, roughness: 0.5 });
  const g = new THREE.Group(); g.name = 'Robot genérico (escenario)';
  g.add(boxFrom([-0.27, 1.51, 0.0], [-0.13, 1.72, 0.2], dark));      // pedestal sobre el plato fijo
  g.add(boxFrom([-0.27, 1.72, -1.7], [-0.13, 1.86, 0.25], body));     // viga transversal (Z)
  g.add(boxFrom([-0.70, 1.86, -0.06], [-0.13, 1.94, 0.06], body));    // brazo de avance (X)
  g.add(boxFrom([-0.69, 1.25, -0.04], [-0.61, 1.94, 0.04], dark));    // brazo vertical hasta el EOAT
  return g;
}
function hrsCart() {
  const frame = new THREE.MeshStandardMaterial({ color: 0x3a4044, metalness: 0.5, roughness: 0.45 });
  const g = new THREE.Group(); g.name = 'Carro HRS';
  g.add(boxFrom([-0.25, 0.77, -0.25], [0.25, 0.8, 0.25], frame));
  g.add(boxFrom([-0.25, 0.12, -0.25], [0.25, 0.14, 0.25], frame));
  for (const [x, z] of [[-1, -1], [1, -1], [-1, 1], [1, 1]]) {
    g.add(boxFrom([x * 0.23 - 0.015, 0.06, z * 0.23 - 0.015], [x * 0.23 + 0.015, 0.77, z * 0.23 + 0.015], frame));
    const w = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 0.025, 16), new THREE.MeshStandardMaterial({ color: 0x16191b, roughness: 0.8 }));
    w.rotation.x = Math.PI / 2; w.position.set(x * 0.23, 0.03, z * 0.23); g.add(w);
  }
  return g;
}
function hrsCable(machine) {
  const n = machine.getObjectByName('RUTA_CABLE_HRS');
  const ruta = n && n.userData && n.userData.ruta;
  if (!ruta) return null;
  const curve = new THREE.CatmullRomCurve3(ruta.map(p => new THREE.Vector3(...p)), false, 'catmullrom', 0.15);
  const m = new THREE.Mesh(new THREE.TubeGeometry(curve, 96, (n.userData.diametro_visual_m || 0.024) / 2, 10), new THREE.MeshStandardMaterial({ color: 0x23282a, roughness: 0.7 }));
  m.name = 'Cable HRS'; m.castShadow = true;
  return m;
}
