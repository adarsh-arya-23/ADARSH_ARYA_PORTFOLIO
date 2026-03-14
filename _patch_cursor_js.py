
# Upgrades the initCursor JS function with the full premium implementation
js_file = r"d:\Documents\Z_PORTFOLIO\main.js"
with open(js_file, "r", encoding="utf-8") as fh:
    js = fh.read()

OLD_CURSOR_JS = """/* ══════════════════════════════════════════════════════════
   2. CUSTOM CURSOR
══════════════════════════════════════════════════════════ */
function initCursor() {
    const cursor = document.getElementById('cursor');
    const cursorTrail = document.getElementById('cursorTrail');
    if (!cursor || !cursorTrail) return;

    let mx = -200, my = -200, tx = -200, ty = -200;

    document.addEventListener('mousemove', e => {
        mx = e.clientX; my = e.clientY;
        cursor.style.left = mx + 'px';
        cursor.style.top = my + 'px';
    });

    (function animateTrail() {
        tx += (mx - tx) * 0.1;
        ty += (my - ty) * 0.1;
        cursorTrail.style.left = tx + 'px';
        cursorTrail.style.top = ty + 'px';
        requestAnimationFrame(animateTrail);
    })();

    document.addEventListener('mouseleave', () => {
        cursor.style.opacity = cursorTrail.style.opacity = '0';
    });
    document.addEventListener('mouseenter', () => {
        cursor.style.opacity = cursorTrail.style.opacity = '1';
    });

    // Expand on interactive elements
    const interactive = 'a, button, [data-magnetic], .stack-card, .project-link, .nav-link';
    document.querySelectorAll(interactive).forEach(el => {
        el.addEventListener('mouseenter', () => {
            cursor.style.transform = 'translate(-50%,-50%) scale(2.2)';
            cursorTrail.style.width = '52px';
            cursorTrail.style.height = '52px';
        });
        el.addEventListener('mouseleave', () => {
            cursor.style.transform = 'translate(-50%,-50%) scale(1)';
            cursorTrail.style.width = '36px';
            cursorTrail.style.height = '36px';
        });
    });
}"""

NEW_CURSOR_JS = """/* ══════════════════════════════════════════════════════════
   2. CUSTOM CURSOR — v2 Premium
      Dot snaps instantly; ring lags with lerp.
      Context-aware states: default / hover / cta / text / click.
      Click spawns a ripple element.
══════════════════════════════════════════════════════════ */
function initCursor() {
    // Touch / coarse-pointer devices — skip entirely
    if (window.matchMedia('(pointer: coarse)').matches) return;

    const dot   = document.getElementById('cursor');
    const ring  = document.getElementById('cursorTrail');
    if (!dot || !ring) return;

    // ── State ────────────────────────────────────────────────
    let mx = -300, my = -300; // raw mouse (dot follows)
    let rx = -300, ry = -300; // ring target (lerped)
    let rafId;
    let curState = '';          // current named state on <body>

    // ── Smooth ring lerp loop ─────────────────────────────────
    function lerp(a, b, t) { return a + (b - a) * t; }

    function animLoop() {
        rx = lerp(rx, mx, 0.11);
        ry = lerp(ry, my, 0.11);

        dot.style.transform  = `translate(calc(${mx}px - 50%), calc(${my}px - 50%))`;
        ring.style.transform = `translate(calc(${rx}px - 50%), calc(${ry}px - 50%))`;

        rafId = requestAnimationFrame(animLoop);
    }
    rafId = requestAnimationFrame(animLoop);

    // ── Mouse tracking ────────────────────────────────────────
    document.addEventListener('mousemove', e => {
        mx = e.clientX;
        my = e.clientY;
    }, { passive: true });

    document.addEventListener('mouseleave', () => {
        dot.style.opacity = ring.style.opacity = '0';
    });
    document.addEventListener('mouseenter', () => {
        dot.style.opacity = ring.style.opacity = '1';
    });

    // ── State management ──────────────────────────────────────
    function setState(state) {
        if (curState === state) return;
        // Remove all cursor--* classes from body
        document.body.classList.remove(
            'cursor--hover', 'cursor--cta', 'cursor--text', 'cursor--click'
        );
        if (state) document.body.classList.add('cursor--' + state);
        curState = state;
    }

    // ── Click: shrink dot + spawn ripple ─────────────────────
    document.addEventListener('mousedown', () => {
        setState('click');
        spawnRipple(mx, my);
    });
    document.addEventListener('mouseup', () => setState(''));

    function spawnRipple(x, y) {
        const r = document.createElement('div');
        r.className = 'cursor-ripple';
        r.style.left = x + 'px';
        r.style.top  = y + 'px';
        document.body.appendChild(r);
        r.addEventListener('animationend', () => r.remove());
    }

    // ── Element detection via event delegation ────────────────
    const CTA_SEL    = '.btn-primary, .nav-cta, .proj-link-btn, .mob-cta';
    const HOVER_SEL  = 'a, button, .stack-card, .proj-card, .nav-link, ' +
                       '.proj-filter, .proj-overlay-btn, .hamburger, ' +
                       '.mob-link, .mob-close, .timeline-item';
    const TEXT_SEL   = 'input, textarea, [contenteditable]';

    function getState(el) {
        if (!el || el === document.body || el === document.documentElement) return '';
        if (el.closest(TEXT_SEL))   return 'text';
        if (el.closest(CTA_SEL))    return 'cta';
        if (el.closest(HOVER_SEL))  return 'hover';
        return '';
    }

    document.addEventListener('mouseover', e => {
        // Only recalc if not clicking
        if (curState !== 'click') setState(getState(e.target));
    }, { passive: true });

    document.addEventListener('mouseout', e => {
        if (!e.relatedTarget && curState !== 'click') setState('');
        else if (curState !== 'click') setState(getState(e.relatedTarget));
    }, { passive: true });

    // ── Magnetic pull on CTA buttons ─────────────────────────
    document.querySelectorAll(CTA_SEL).forEach(btn => {
        btn.addEventListener('mousemove', e => {
            const r  = btn.getBoundingClientRect();
            const cx = r.left + r.width  / 2;
            const cy = r.top  + r.height / 2;
            const dx = (e.clientX - cx) * 0.28;
            const dy = (e.clientY - cy) * 0.28;
            btn.style.transform = `translate(${dx}px, ${dy}px)`;
        });
        btn.addEventListener('mouseleave', () => {
            btn.style.transform = '';
        });
    });
}"""

if OLD_CURSOR_JS in js:
    js = js.replace(OLD_CURSOR_JS, NEW_CURSOR_JS)
    print("JS cursor block replaced OK")
else:
    print("ERROR: JS cursor block not found — check spacing")

with open(js_file, "w", encoding="utf-8") as fh:
    fh.write(js)
print("JS done")
