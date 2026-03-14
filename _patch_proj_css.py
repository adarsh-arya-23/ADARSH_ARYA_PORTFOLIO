
# Appends all new project-section CSS to style.css
f = r"d:\Documents\Z_PORTFOLIO\style.css"

NEW_CSS = """

/* =============================================================
   PROJECTS V2  — Complete Showcase CSS
   ============================================================= */

/* ── Section header layout ─────────────────────────────────── */
.projects-header {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 40px;
}

/* ── Filter tabs ────────────────────────────────────────────── */
.proj-filters {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 48px;
}

.proj-filter {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 600;
  padding: 8px 18px;
  border-radius: var(--radius-full);
  border: 1px solid var(--border);
  background: transparent;
  color: var(--text-muted);
  cursor: pointer;
  transition: all 0.25s ease;
  letter-spacing: 0.04em;
}

.proj-filter:hover {
  border-color: var(--border-medium);
  color: var(--text-secondary);
  background: rgba(255,255,255,0.04);
}

.proj-filter.active {
  background: linear-gradient(135deg, var(--violet), var(--cyan-light));
  border-color: transparent;
  color: #fff;
  box-shadow: 0 4px 16px rgba(109,40,217,0.4);
}

/* ── Projects grid ──────────────────────────────────────────── */
.projects-grid-v2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 28px;
  margin-bottom: 48px;
}

/* Featured card spans full width */
.proj-card--featured {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: 55% 1fr;
  gap: 0;
}

/* ── Card base ─────────────────────────────────────────────── */
.proj-card {
  background: rgba(255,255,255,0.025);
  border: 1px solid var(--border);
  border-radius: var(--radius-xl);
  overflow: hidden;
  transition:
    transform 0.4s var(--ease-spring),
    box-shadow 0.4s ease,
    border-color 0.3s ease;
  display: flex;
  flex-direction: column;
  position: relative;
}

.proj-card::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: var(--radius-xl);
  background: linear-gradient(135deg, rgba(109,40,217,0.06) 0%, transparent 50%);
  opacity: 0;
  transition: opacity 0.35s ease;
  pointer-events: none;
  z-index: 0;
}

.proj-card:hover {
  transform: translateY(-6px);
  border-color: rgba(167,139,250,0.25);
  box-shadow:
    0 24px 60px rgba(0,0,0,0.5),
    0 0 0 1px rgba(167,139,250,0.15),
    0 0 40px rgba(109,40,217,0.08);
}

.proj-card:hover::before {
  opacity: 1;
}

/* Featured card: no column override needed on inner items */
.proj-card--featured .proj-img-wrap { border-radius: 0; }

/* ── Image / visual area ────────────────────────────────────── */
.proj-img-wrap {
  position: relative;
  overflow: hidden;
  aspect-ratio: 16/9;
  flex-shrink: 0;
}

.proj-card--featured .proj-img-wrap {
  aspect-ratio: auto;
  height: 100%;
  min-height: 340px;
}

.proj-img {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.5s ease;
}

.proj-card:hover .proj-img {
  transform: scale(1.03);
}

/* Glow overlay */
.proj-img-glow {
  position: absolute;
  bottom: -40px;
  left: 50%;
  transform: translateX(-50%);
  width: 60%;
  height: 80px;
  background: var(--g, #7c3aed);
  border-radius: 50%;
  filter: blur(40px);
  opacity: 0.25;
  pointer-events: none;
  transition: opacity 0.4s ease;
}

.proj-card:hover .proj-img-glow {
  opacity: 0.5;
}

/* ── Hover overlay with buttons ─────────────────────────────── */
.proj-hover-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.65);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 5;
}

.proj-card:hover .proj-hover-overlay {
  opacity: 1;
}

.proj-overlay-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-mono);
  font-size: 0.82rem;
  font-weight: 600;
  padding: 10px 20px;
  border-radius: var(--radius-full);
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.2);
  color: #fff;
  backdrop-filter: blur(8px);
  transition: all 0.2s ease;
  transform: translateY(8px);
  transition: transform 0.3s var(--ease-spring), background 0.2s ease, opacity 0.3s ease;
  opacity: 0;
}

.proj-card:hover .proj-overlay-btn {
  opacity: 1;
  transform: translateY(0);
}

.proj-card:hover .proj-overlay-btn:nth-child(2) {
  transition-delay: 0.05s;
}

.proj-overlay-btn:hover {
  background: rgba(255,255,255,0.22);
}

.proj-overlay-btn--ghost {
  background: rgba(0,0,0,0.3);
}

/* ── Info panel ─────────────────────────────────────────────── */
.proj-info {
  padding: 28px 28px 24px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  flex: 1;
  position: relative;
  z-index: 1;
}

/* Meta row */
.proj-meta {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}

.proj-category {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--violet-light);
  background: rgba(109,40,217,0.12);
  padding: 3px 10px;
  border-radius: var(--radius-full);
  border: 1px solid rgba(109,40,217,0.25);
}

.proj-year {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--text-muted);
}

.proj-status {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 3px 9px;
  border-radius: var(--radius-full);
}

.proj-status--live {
  background: rgba(5,150,105,0.12);
  color: var(--green-light);
  border: 1px solid rgba(52,211,153,0.25);
}

.proj-status--build {
  background: rgba(217,119,6,0.12);
  color: #fcd34d;
  border: 1px solid rgba(217,119,6,0.25);
}

/* Title */
.proj-title {
  font-family: var(--font-display);
  font-size: 1.45rem;
  font-weight: 800;
  color: var(--text-primary);
  line-height: 1.2;
  letter-spacing: -0.025em;
  margin: 0;
}

.proj-title-accent {
  background: var(--grad-text);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* Description */
.proj-desc {
  font-size: 0.92rem;
  color: var(--text-secondary);
  line-height: 1.75;
  margin: 0;
}

/* Tags */
.proj-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.proj-tag {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--text-muted);
  background: rgba(255,255,255,0.04);
  border: 1px solid var(--border);
  padding: 4px 11px;
  border-radius: var(--radius-full);
  transition: all 0.2s ease;
  letter-spacing: 0.03em;
}

.proj-card:hover .proj-tag {
  border-color: var(--border-medium);
  color: var(--text-secondary);
}

/* Links */
.proj-links {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: auto;
}

.proj-link-btn {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-family: var(--font-mono);
  font-size: 0.8rem;
  font-weight: 600;
  padding: 9px 18px;
  border-radius: var(--radius-full);
  background: linear-gradient(135deg, var(--violet), var(--cyan-light));
  color: #fff;
  transition: all 0.25s var(--ease-spring);
  letter-spacing: 0.03em;
  box-shadow: 0 4px 14px rgba(109,40,217,0.3);
}

.proj-link-btn:hover {
  transform: translateY(-2px) scale(1.04);
  box-shadow: 0 8px 24px rgba(109,40,217,0.5);
}

.proj-link-btn--ghost {
  background: transparent;
  border: 1px solid var(--border-medium);
  color: var(--text-secondary);
  box-shadow: none;
}

.proj-link-btn--ghost:hover {
  background: rgba(255,255,255,0.05);
  color: var(--text-primary);
  border-color: rgba(255,255,255,0.25);
  box-shadow: none;
}

/* SVG icon sizing in buttons */
.proj-link-btn svg,
.proj-overlay-btn svg {
  width: 14px;
  height: 14px;
}

/* ── Browser mockup ─────────────────────────────────────────── */
.proj-browser {
  width: 88%;
  background: rgba(10,10,20,0.9);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0,0,0,0.7);
}

.proj-browser-bar {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 12px;
  background: rgba(255,255,255,0.04);
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

.pb-dot {
  width: 10px; height: 10px;
  border-radius: 50%;
}

.pb-url {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  color: var(--text-muted);
  margin-left: 8px;
  background: rgba(255,255,255,0.06);
  padding: 2px 10px;
  border-radius: 4px;
}

.proj-browser-screen {
  display: flex;
  height: 200px;
}

.pb-sidebar {
  width: 40px;
  background: rgba(255,255,255,0.03);
  border-right: 1px solid rgba(255,255,255,0.05);
  padding: 12px 8px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.pb-nav-item {
  height: 6px;
  border-radius: 3px;
  background: rgba(255,255,255,0.1);
}

.pb-nav-item.active {
  background: linear-gradient(90deg, var(--violet), var(--cyan-light));
}

.pb-body {
  flex: 1;
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.pb-stat-row {
  display: flex;
  gap: 8px;
}

.pb-stat {
  flex: 1;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 6px;
  padding: 8px;
  text-align: center;
}

.pb-stat-num {
  font-family: var(--font-mono);
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--c, #fff);
}

.pb-stat-lbl {
  font-size: 0.55rem;
  color: var(--text-muted);
  margin-top: 2px;
}

.pb-chart {
  display: flex;
  align-items: flex-end;
  gap: 4px;
  height: 50px;
}

.pb-bar {
  flex: 1;
  height: var(--h, 50%);
  background: var(--c, #7c3aed);
  border-radius: 3px 3px 0 0;
  opacity: 0.7;
  transition: opacity 0.3s ease;
}

.proj-card:hover .pb-bar { opacity: 1; }

.pb-heatmap {
  display: flex;
  gap: 3px;
}

.pb-heat {
  flex: 1;
  height: 12px;
  border-radius: 2px;
  background: var(--violet);
  opacity: var(--op, 0.3);
}

/* ── Code mockup ─────────────────────────────────────────────── */
.proj-code-mockup {
  width: 88%;
  background: rgba(5,5,15,0.95);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0,0,0,0.7);
  font-family: var(--font-mono);
}

.pcm-header {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 12px;
  background: rgba(255,255,255,0.04);
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

.pcm-dot { width: 10px; height: 10px; border-radius: 50%; }

.pcm-title {
  font-size: 0.65rem;
  color: var(--text-muted);
  margin-left: 6px;
}

.pcm-body {
  padding: 12px 14px;
  font-size: 0.7rem;
  line-height: 1.8;
}

.pcm-line { display: block; color: rgba(255,255,255,0.5); }
.pcm-kw   { color: #c084fc; }
.pcm-cls  { color: #93c5fd; }
.pcm-fn   { color: #67e8f9; }
.pcm-kw   { color: #c084fc; }
.pcm-num  { color: #a3e635; }

.pcm-result {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  font-size: 0.65rem;
  border-top: 1px solid rgba(255,255,255,0.06);
}

.pcm-result svg { width: 12px; height: 12px; }

.pcm-result--pass {
  color: #34d399;
  background: rgba(5,150,105,0.08);
}

/* ── AI mockup ───────────────────────────────────────────────── */
.proj-ai-mockup {
  width: 75%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
}

.pam-frame {
  position: relative;
  width: 110px;
  height: 110px;
  border: 2px solid rgba(5,150,105,0.5);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.pam-corner {
  position: absolute;
  width: 14px;
  height: 14px;
  border-color: #10b981;
  border-style: solid;
}
.pam-corner--tl { top: -2px; left: -2px; border-width: 3px 0 0 3px; border-radius: 3px 0 0 0; }
.pam-corner--tr { top: -2px; right: -2px; border-width: 3px 3px 0 0; border-radius: 0 3px 0 0; }
.pam-corner--bl { bottom: -2px; left: -2px; border-width: 0 0 3px 3px; border-radius: 0 0 0 3px; }
.pam-corner--br { bottom: -2px; right: -2px; border-width: 0 3px 3px 0; border-radius: 0 0 3px 0; }

.pam-face {
  display: flex;
  gap: 18px;
  align-items: center;
}

.pam-eye {
  width: 18px;
  height: 18px;
  border: 2px solid #10b981;
  border-radius: 50%;
  position: relative;
}

.pam-eye::after {
  content: '';
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 6px; height: 6px;
  background: #10b981;
  border-radius: 50%;
}

.pam-scan {
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, #10b981, transparent);
  animation: scanDown 2s ease-in-out infinite;
  box-shadow: 0 0 8px #10b981;
}

@keyframes scanDown {
  0%   { top: 0; opacity: 1; }
  100% { top: 100%; opacity: 0; }
}

.pam-status {
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  color: #34d399;
  background: rgba(5,150,105,0.12);
  border: 1px solid rgba(52,211,153,0.25);
  padding: 5px 12px;
  border-radius: var(--radius-full);
}

.pam-dot {
  width: 6px; height: 6px;
  border-radius: 50%;
  background: #34d399;
  animation: badgePulse 2s infinite;
}

.pam-bar {
  width: 100%;
  height: 4px;
  background: rgba(255,255,255,0.08);
  border-radius: 2px;
  overflow: hidden;
}

.pam-progress {
  height: 100%;
  width: 72%;
  background: linear-gradient(90deg, #059669, #34d399);
  border-radius: 2px;
  animation: progressPulse 3s ease-in-out infinite;
}

@keyframes progressPulse {
  0%, 100% { width: 65%; }
  50%       { width: 85%; }
}

/* ── SaaS landing mockup ─────────────────────────────────────── */
.proj-saas-mockup {
  width: 88%;
  background: rgba(10,5,25,0.9);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0,0,0,0.7);
}

.psm-topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 14px;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

.psm-logo {
  width: 24px; height: 8px;
  background: linear-gradient(90deg, var(--violet), var(--cyan-light));
  border-radius: 4px;
}

.psm-nav { display: flex; align-items: center; gap: 8px; }

.psm-nav-item {
  width: 30px; height: 5px;
  background: rgba(255,255,255,0.1);
  border-radius: 3px;
}

.psm-btn {
  width: 40px; height: 16px;
  background: linear-gradient(135deg, var(--violet), var(--cyan-light));
  border-radius: 8px;
  opacity: 0.8;
}

.psm-hero {
  padding: 20px 14px 14px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.psm-headline {
  width: 70%; height: 10px;
  background: rgba(255,255,255,0.15);
  border-radius: 5px;
}

.psm-sub {
  width: 50%; height: 6px;
  background: rgba(255,255,255,0.07);
  border-radius: 3px;
}

.psm-ctas { display: flex; gap: 8px; }

.psm-cta {
  height: 20px; width: 70px;
  background: rgba(255,255,255,0.07);
  border-radius: 10px;
}

.psm-cta--primary {
  background: linear-gradient(135deg, var(--violet), var(--cyan-light));
  opacity: 0.7;
}

.psm-preview {
  width: 100%; height: 50px;
  background: linear-gradient(135deg, rgba(109,40,217,0.15) 0%, rgba(34,211,238,0.08) 100%);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 8px;
}

/* ── Responsive ─────────────────────────────────────────────── */
@media (max-width: 900px) {
  .projects-grid-v2 {
    grid-template-columns: 1fr;
  }

  .proj-card--featured {
    grid-column: 1;
    grid-template-columns: 1fr;
  }

  .proj-card--featured .proj-img-wrap {
    height: auto;
    min-height: 0;
    aspect-ratio: 16/9;
  }
}

@media (max-width: 600px) {
  .proj-info {
    padding: 20px 18px;
  }

  .proj-title {
    font-size: 1.2rem;
  }

  .proj-filters {
    gap: 8px;
  }

  .proj-filter {
    font-size: 0.72rem;
    padding: 7px 14px;
  }
}
"""

with open(f, "a", encoding="utf-8") as fh:
    fh.write(NEW_CSS)

print("CSS appended successfully")
