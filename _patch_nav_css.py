
f = r"d:\Documents\Z_PORTFOLIO\style.css"
with open(f, "r", encoding="utf-8") as fh:
    css = fh.read()

# Find nav section start/end
NAV_START_MARKER = "/* ─────────────────────────────────────────────────────────────\r\n   NAVIGATION"
NAV_END_MARKER   = "/* ─────────────────────────────────────────────────────────────\r\n   HERO"
if NAV_START_MARKER not in css:
    NAV_START_MARKER = NAV_START_MARKER.replace("\r\n", "\n")
    NAV_END_MARKER   = NAV_END_MARKER.replace("\r\n", "\n")

s = css.find(NAV_START_MARKER)
e = css.find(NAV_END_MARKER)
print(f"Nav CSS block: {s} → {e}")

NEW_NAV_CSS = """/* =============================================================
   NAVIGATION  — Redesigned v2 (glassmorphism + active pill)
   ============================================================= */

/* ── Base nav ─────────────────────────────────────────────── */
.nav {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 1000;
  padding: 20px 0;
  transition:
    padding 0.4s var(--ease-out),
    background 0.4s var(--ease-out),
    box-shadow 0.4s ease,
    transform 0.4s var(--ease-spring);
}

/* Transparent at top → glass on scroll */
.nav.scrolled {
  padding: 12px 0;
  background: rgba(4,4,12,0.82);
  backdrop-filter: blur(28px) saturate(200%);
  -webkit-backdrop-filter: blur(28px) saturate(200%);
  box-shadow:
    0 1px 0 rgba(255,255,255,0.06),
    0 8px 40px rgba(0,0,0,0.5);
}

/* Auto-hide on scroll down */
.nav.nav--hidden {
  transform: translateY(-100%);
}

/* ── Inner layout ──────────────────────────────────────────── */
.nav-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--s8);
  display: flex;
  align-items: center;
  gap: var(--s5);
}

/* ── Logo ──────────────────────────────────────────────────── */
.nav-logo {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-right: auto;
  text-decoration: none;
  flex-shrink: 0;
}

.logo-mark {
  display: flex;
  align-items: center;
  gap: 5px;
}

.logo-text {
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 900;
  background: var(--grad-text);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  letter-spacing: -0.04em;
}

.logo-dot {
  width: 7px; height: 7px;
  background: var(--cyan-light);
  border-radius: 50%;
  box-shadow: 0 0 10px var(--cyan-light);
  animation: dotPulse 2.5s ease-in-out infinite;
  flex-shrink: 0;
}

@keyframes dotPulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50%       { opacity: 0.35; transform: scale(0.55); }
}

.logo-name {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 500;
  color: var(--text-muted);
  letter-spacing: 0.03em;
  display: none; /* only shown on wider screens */
}

@media (min-width: 820px) {
  .logo-name { display: block; }
}

/* ── Desktop nav links ─────────────────────────────────────── */
.nav-links {
  display: flex;
  align-items: center;
  gap: 2px;
  list-style: none;
}

.nav-link {
  position: relative;
  font-family: var(--font-mono);
  font-size: 0.83rem;
  font-weight: 500;
  color: var(--text-muted);
  padding: 7px 14px;
  border-radius: var(--radius-full);
  transition: color 0.25s ease, background 0.25s ease;
  letter-spacing: 0.025em;
  white-space: nowrap;
}

/* Underline slide indicator */
.nav-link::after {
  content: '';
  position: absolute;
  bottom: 3px; left: 50%;
  width: 0; height: 2px;
  background: var(--grad-text);
  border-radius: 1px;
  transform: translateX(-50%);
  transition: width 0.3s var(--ease-spring);
}

.nav-link:hover {
  color: var(--text-primary);
  background: rgba(255,255,255,0.05);
}

.nav-link:hover::after {
  width: 60%;
}

.nav-link.nav-active {
  color: var(--text-primary);
}

.nav-link.nav-active::after {
  width: 70%;
  background: linear-gradient(90deg, var(--violet-bright), var(--cyan-light));
}

/* ── CTA button ────────────────────────────────────────────── */
.nav-cta {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-family: var(--font-mono);
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--violet-bright);
  border: 1px solid rgba(192,132,252,0.3);
  padding: 9px 20px;
  border-radius: var(--radius-full);
  background: rgba(109,40,217,0.1);
  transition: all 0.3s var(--ease-spring);
  letter-spacing: 0.03em;
  white-space: nowrap;
  flex-shrink: 0;
}

.nav-cta svg {
  transition: transform 0.3s var(--ease-spring);
}

.nav-cta:hover {
  background: rgba(109,40,217,0.22);
  border-color: var(--violet-bright);
  color: #fff;
  box-shadow: 0 0 28px rgba(109,40,217,0.4), inset 0 0 12px rgba(192,132,252,0.1);
  transform: translateY(-1px);
}

.nav-cta:hover svg {
  transform: translateX(3px);
}

/* ── Hamburger button ──────────────────────────────────────── */
.hamburger {
  display: none;
  flex-direction: column;
  justify-content: center;
  align-items: flex-end;
  gap: 5px;
  width: 36px;
  height: 36px;
  padding: 4px;
  background: rgba(255,255,255,0.05);
  border: 1px solid var(--border);
  border-radius: 10px;
  cursor: pointer;
  transition: background 0.2s ease, border-color 0.2s ease;
  flex-shrink: 0;
}

.hamburger:hover {
  background: rgba(255,255,255,0.09);
  border-color: var(--border-medium);
}

.ham-line {
  display: block;
  height: 1.5px;
  background: var(--text-primary);
  border-radius: 2px;
  transition: transform 0.35s var(--ease-spring), opacity 0.25s ease, width 0.3s ease;
}

.ham-line--top { width: 18px; }
.ham-line--mid { width: 22px; }
.ham-line--bot { width: 14px; }

/* Morph to X */
.hamburger.is-open .ham-line--top {
  width: 20px;
  transform: translateY(6.5px) rotate(45deg);
}
.hamburger.is-open .ham-line--mid {
  opacity: 0;
  transform: scaleX(0);
}
.hamburger.is-open .ham-line--bot {
  width: 20px;
  transform: translateY(-6.5px) rotate(-45deg);
}

/* ── Fullscreen mobile overlay ─────────────────────────────── */
.mobile-overlay {
  position: fixed;
  inset: 0;
  z-index: 990;
  display: flex;
  align-items: stretch;
  pointer-events: none;
  visibility: hidden;
  transition: visibility 0s 0.45s;
}

.mobile-overlay.is-open {
  pointer-events: auto;
  visibility: visible;
  transition: visibility 0s 0s;
}

.mob-overlay-bg {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.5);
  backdrop-filter: blur(4px);
  opacity: 0;
  transition: opacity 0.35s ease;
}

.mobile-overlay.is-open .mob-overlay-bg {
  opacity: 1;
}

.mob-content {
  position: absolute;
  top: 0; right: 0;
  width: min(400px, 92vw);
  height: 100vh;
  background: rgba(6,6,16,0.97);
  backdrop-filter: blur(40px) saturate(180%);
  border-left: 1px solid rgba(255,255,255,0.07);
  display: flex;
  flex-direction: column;
  padding: 0 0 40px;
  transform: translateX(100%);
  transition: transform 0.45s var(--ease-spring);
  box-shadow: -20px 0 80px rgba(0,0,0,0.7);
}

.mobile-overlay.is-open .mob-content {
  transform: translateX(0);
}

/* Header row */
.mob-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 28px;
  border-bottom: 1px solid rgba(255,255,255,0.06);
  margin-bottom: 20px;
}

.mob-logo { gap: 6px; }

.mob-close {
  font-size: 1.6rem;
  width: 36px; height: 36px;
  display: flex; align-items: center; justify-content: center;
  color: var(--text-muted);
  background: rgba(255,255,255,0.05);
  border: 1px solid var(--border);
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s ease;
  line-height: 1;
  padding: 0;
}

.mob-close:hover {
  color: var(--text-primary);
  background: rgba(255,255,255,0.1);
}

/* Nav list */
.mob-nav {
  flex: 1;
  padding: 12px 20px;
  overflow-y: auto;
}

.mob-nav ul { list-style: none; display: flex; flex-direction: column; gap: 4px; }

.mob-link {
  display: flex;
  align-items: center;
  gap: 14px;
  font-family: var(--font-display);
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-muted);
  padding: 16px 12px;
  border-radius: var(--radius-lg);
  letter-spacing: -0.025em;
  transition: all 0.25s ease;
  opacity: 0;
  transform: translateX(24px);
}

/* Stagger animation when open */
.mobile-overlay.is-open .mob-link {
  opacity: 1;
  transform: translateX(0);
}

.mobile-overlay.is-open .mob-link:nth-child(1) { transition: all 0.4s ease 0.12s; }
.mobile-overlay.is-open .mob-link:nth-child(2) { transition: all 0.4s ease 0.18s; }
.mobile-overlay.is-open .mob-link:nth-child(3) { transition: all 0.4s ease 0.24s; }
.mobile-overlay.is-open .mob-link:nth-child(4) { transition: all 0.4s ease 0.30s; }
.mobile-overlay.is-open .mob-link:nth-child(5) { transition: all 0.4s ease 0.36s; }

.mob-link::before {
  content: attr(data-mob);
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  color: var(--violet-bright);
  opacity: 0.5;
  min-width: 20px;
  counter-increment: mob-counter;
}

.mob-link:hover {
  color: var(--text-primary);
  background: rgba(255,255,255,0.05);
  padding-left: 20px;
}

/* Footer */
.mob-footer {
  padding: 20px 28px 0;
  border-top: 1px solid rgba(255,255,255,0.06);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 12px;
  opacity: 0;
  transition: opacity 0.35s ease 0.4s;
}

.mobile-overlay.is-open .mob-footer {
  opacity: 1;
}

.mob-cta {
  width: 100%;
  justify-content: center;
}

.mob-tagline {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--text-muted);
  letter-spacing: 0.05em;
}

/* ── Responsive show/hide ──────────────────────────────────── */
@media (max-width: 768px) {
  .nav-links, .nav-cta { display: none; }
  .hamburger { display: flex; }
  .logo-name { display: none; }
}

@media (min-width: 769px) {
  .hamburger { display: none; }
  .mobile-overlay { display: none; }
}

"""

new_css = css[:s] + NEW_NAV_CSS + css[e:]
with open(f, "w", encoding="utf-8") as fh:
    fh.write(new_css)

print(f"Nav CSS replaced. New length: {len(new_css)}")
