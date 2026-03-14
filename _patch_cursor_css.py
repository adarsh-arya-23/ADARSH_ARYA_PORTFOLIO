
# Upgrades the custom cursor: CSS overhaul + JS full rewrite
import re

# ─── CSS PATCH ────────────────────────────────────────────────
css_file = r"d:\Documents\Z_PORTFOLIO\style.css"
with open(css_file, "r", encoding="utf-8") as fh:
    css = fh.read()

OLD_CURSOR_CSS = """.cursor {
    position: fixed;
    width: 10px;
    height: 10px;
    background: var(--violet-light);
    border-radius: 50%;
    pointer-events: none;
    z-index: 9999;
    transform: translate(-50%, -50%);
    transition: width 0.2s var(--ease-out), height 0.2s var(--ease-out), background 0.2s;
    mix-blend-mode: screen;
}

.cursor-trail {
    position: fixed;
    width: 36px;
    height: 36px;
    border: 1.5px solid rgba(168, 85, 247, 0.4);
    border-radius: 50%;
    pointer-events: none;
    z-index: 9998;
    transform: translate(-50%, -50%);
    transition: left 0.12s var(--ease-out), top 0.12s var(--ease-out),
        width 0.25s var(--ease-out), height 0.25s var(--ease-out),
        border-color 0.25s;
}

body:has(a:hover) .cursor,
body:has(button:hover) .cursor {
    width: 20px;
    height: 20px;
    background: var(--cyan);
}

body:has(a:hover) .cursor-trail,
body:has(button:hover) .cursor-trail {
    width: 56px;
    height: 56px;
    border-color: rgba(6, 182, 212, 0.35);
}

@media (max-width: 768px) {

    .cursor,
    .cursor-trail {
        display: none;
    }

    body {
        cursor: auto;
    }

    button {
        cursor: pointer;
    }
}"""

NEW_CURSOR_CSS = """/* =============================================================
   CUSTOM CURSOR  v2 — Magnetic dot + lagging ring + states
   ============================================================= */

/* Hide system cursor globally (desktop only) */
@media (pointer: fine) {
  html, body, a, button, [role="button"],
  input, textarea, select { cursor: none !important; }
}

/* ── Dot (snaps to exact mouse position) ────────────────────── */
.cursor {
  position: fixed;
  top: 0; left: 0;
  width: 8px; height: 8px;
  border-radius: 50%;
  pointer-events: none;
  z-index: 10000;
  background: #fff;
  transform: translate(-50%, -50%);
  mix-blend-mode: difference;
  will-change: transform, width, height;
  transition:
    width  0.25s cubic-bezier(0.23,1,0.32,1),
    height 0.25s cubic-bezier(0.23,1,0.32,1),
    opacity 0.3s ease;
}

/* ── Ring (lags behind mouse) ───────────────────────────────── */
.cursor-trail {
  position: fixed;
  top: 0; left: 0;
  width: 38px; height: 38px;
  border-radius: 50%;
  pointer-events: none;
  z-index: 9999;
  border: 1px solid rgba(167,139,250,0.55);
  background: transparent;
  transform: translate(-50%, -50%);
  will-change: transform, width, height, border-color, background;
  transition:
    width  0.45s cubic-bezier(0.23,1,0.32,1),
    height 0.45s cubic-bezier(0.23,1,0.32,1),
    border-color 0.35s ease,
    background 0.35s ease,
    opacity 0.3s ease;
}

/* Inner glow spot on the ring */
.cursor-trail::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(167,139,250,0.12) 0%, transparent 70%);
  opacity: 0;
  transition: opacity 0.3s ease;
}

/* ── STATE: hovering link / button ─────────────────────────── */
.cursor--hover .cursor {
  width: 12px; height: 12px;
}
.cursor--hover .cursor-trail {
  width: 56px; height: 56px;
  border-color: rgba(34,211,238,0.6);
  background: rgba(34,211,238,0.04);
}
.cursor--hover .cursor-trail::before { opacity: 1; }

/* ── STATE: on a primary button (CTA) ─────────────────────── */
.cursor--cta .cursor {
  width: 14px; height: 14px;
  background: rgb(255,255,255);
}
.cursor--cta .cursor-trail {
  width: 68px; height: 68px;
  border-color: rgba(109,40,217,0.7);
  background: rgba(109,40,217,0.08);
  box-shadow: 0 0 24px rgba(109,40,217,0.2);
}

/* ── STATE: on text / input ─────────────────────────────────── */
.cursor--text .cursor {
  width: 2px; height: 24px;
  border-radius: 1px;
  animate: none;
}
.cursor--text .cursor-trail {
  width: 2px; height: 24px;
  border-radius: 1px;
  opacity: 0;
}

/* ── STATE: clicking (mousedown) ─────────────────────────────── */
.cursor--click .cursor {
  width: 5px; height: 5px;
  opacity: 0.6;
}
.cursor--click .cursor-trail {
  width: 28px; height: 28px;
}

/* ── Click ripple ─────────────────────────────────────────── */
.cursor-ripple {
  position: fixed;
  top: 0; left: 0;
  width: 12px; height: 12px;
  border-radius: 50%;
  border: 1.5px solid rgba(167,139,250,0.8);
  pointer-events: none;
  z-index: 9998;
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
  animation: rippleOut 0.55s cubic-bezier(0.23,1,0.32,1) forwards;
}

@keyframes rippleOut {
  to {
    transform: translate(-50%, -50%) scale(4.5);
    opacity: 0;
    border-color: rgba(34,211,238,0);
  }
}

/* ── Mobile: restore default cursor ────────────────────────── */
@media (pointer: coarse), (max-width: 768px) {
  .cursor, .cursor-trail {
    display: none;
  }
  html, body, a, button {
    cursor: auto !important;
  }
  button { cursor: pointer !important; }
}"""

if OLD_CURSOR_CSS in css:
    css = css.replace(OLD_CURSOR_CSS, NEW_CURSOR_CSS)
    print("CSS cursor block replaced OK")
else:
    # Try to find and replace the section by markers
    start = css.find("/* ─────────────────────────────────────────────────────────────\r\n   CUSTOM CURSOR")
    if start == -1:
        start = css.find("/* ─────────────────────────────────────────────────────────────\n   CUSTOM CURSOR")
    end = css.find("/* ─────────────────────────────────────────────────────────────\r\n   SCROLLBAR")
    if end == -1:
        end = css.find("/* ─────────────────────────────────────────────────────────────\n   SCROLLBAR")
    if start != -1 and end != -1:
        css = css[:start] + NEW_CURSOR_CSS + "\n\n" + css[end:]
        print("CSS cursor replaced by marker")
    else:
        print("ERROR: could not find cursor CSS block")

with open(css_file, "w", encoding="utf-8") as fh:
    fh.write(css)

print("CSS done")
