/* ─────────────────────────────────────────────────────────────
   PORTFOLIO — main.js  (Enhanced Animations)
   Systems: preloader · cursor · canvas particles · nav · scroll reveal ·
            counter · stack filter · hamburger · form ·
            parallax · smooth scroll · card tilt · typing ·
            magnetic buttons · scroll progress · page entry ·
            ripple · floating icons · active nav · cert filter ·
            cert modal · resume dropdown + modal
───────────────────────────────────────────────────────────── */

'use strict';

// ─── Init ────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
    lucide.createIcons();

    initPreloader();           // Premium loading screen (fires first)
    initThemeToggle();         // Dark / Light theme toggle
    initCursor();              // Custom cursor — dot + lagging ring + states + ripple + magnetic
    initCanvas();              // Hero particle field
    initScrollProgress();      // Top progress bar
    initNav();                 // Sticky nav + active links
    initReveal();              // IntersectionObserver scroll reveals
    initSectionChoreography(); // Per-section staggered children
    initCounter();             // Number roll-up
    initStackFilter();         // Tech stack tab filter
    initHamburger();           // Mobile menu
    initForm();                // Contact form + micro-interactions
    initParallax();            // Aurora blob parallax + mouse
    initSmoothScroll();        // Anchor smooth scroll
    initCardTilt();            // 3-D card tilt on project cards + cert cards
    initProjectFilter();       // Project category filter
    initCertFilter();          // Certifications category filter  ← NEW
    initCertModal();           // Certificate image lightbox modal
    initResumeDropdown();      // Resume dropdown + PDF viewer modal
    initTyping();              // Hero role typewriter
    initBackToTop();           // Back-to-top FAB
    initProjSections();        // Organise cards into Featured / WIP / All-Others sections
    initProjectImages();       // Real project screenshots with lazy-load + theme crossfade
});

/* ══════════════════════════════════════════════════════════
   1. PRELOADER — elegant branded loading screen
══════════════════════════════════════════════════════════ */
function initPreloader() {
    const preloader = document.getElementById('preloader');
    const bar = document.getElementById('plBar');
    if (!preloader || !bar) return;

    const DURATION = 1500;
    const EXIT_HOLD = 120;
    let startTime = null;

    function easeInOut(t) {
        return t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
    }

    function tick(ts) {
        if (!startTime) startTime = ts;
        const elapsed = ts - startTime;
        const raw = Math.min(elapsed / DURATION, 1);
        const pct = easeInOut(raw) * 100;

        bar.style.width = pct.toFixed(2) + '%';

        if (raw < 1) {
            requestAnimationFrame(tick);
        } else {
            setTimeout(dismiss, EXIT_HOLD);
        }
    }

    function dismiss() {
        preloader.classList.add('pl-done');
        preloader.addEventListener('transitionend', () => {
            preloader.remove();
        }, { once: true });
    }

    requestAnimationFrame(tick);
}


/* ══════════════════════════════════════════════════════════
   2. CUSTOM CURSOR — v2 Premium
══════════════════════════════════════════════════════════ */
function initCursor() {
    if (window.matchMedia('(pointer: coarse)').matches) return;

    const dot = document.getElementById('cursor');
    const ring = document.getElementById('cursorTrail');
    if (!dot || !ring) return;

    let mx = -300, my = -300;
    let rx = -300, ry = -300;
    let rafId;
    let curState = '';

    function lerp(a, b, t) { return a + (b - a) * t; }

    function animLoop() {
        rx = lerp(rx, mx, 0.11);
        ry = lerp(ry, my, 0.11);
        dot.style.transform = `translate(calc(${mx}px - 50%), calc(${my}px - 50%))`;
        ring.style.transform = `translate(calc(${rx}px - 50%), calc(${ry}px - 50%))`;
        rafId = requestAnimationFrame(animLoop);
    }
    rafId = requestAnimationFrame(animLoop);

    document.addEventListener('mousemove', e => { mx = e.clientX; my = e.clientY; }, { passive: true });
    document.addEventListener('mouseleave', () => { dot.style.opacity = ring.style.opacity = '0'; });
    document.addEventListener('mouseenter', () => { dot.style.opacity = ring.style.opacity = '1'; });

    function setState(state) {
        if (curState === state) return;
        document.body.classList.remove('cursor--hover', 'cursor--cta', 'cursor--text', 'cursor--click');
        if (state) document.body.classList.add('cursor--' + state);
        curState = state;
    }

    document.addEventListener('mousedown', () => { setState('click'); spawnRipple(mx, my); });
    document.addEventListener('mouseup', () => setState(''));

    function spawnRipple(x, y) {
        const r = document.createElement('div');
        r.className = 'cursor-ripple';
        r.style.left = x + 'px';
        r.style.top = y + 'px';
        document.body.appendChild(r);
        r.addEventListener('animationend', () => r.remove());
    }

    const CTA_SEL = '.btn-primary, .nav-cta, .proj-link-btn, .mob-cta';
    const HOVER_SEL = 'a, button, .stack-card, .proj-card, .cert-card, .nav-link, ' +
        '.proj-filter, .cert-filter, .proj-overlay-btn, .hamburger, ' +
        '.mob-link, .mob-close, .timeline-item';
    const TEXT_SEL = 'input, textarea, [contenteditable]';

    function getState(el) {
        if (!el || el === document.body || el === document.documentElement) return '';
        if (el.closest(TEXT_SEL)) return 'text';
        if (el.closest(CTA_SEL)) return 'cta';
        if (el.closest(HOVER_SEL)) return 'hover';
        return '';
    }

    document.addEventListener('mouseover', e => {
        if (curState !== 'click') setState(getState(e.target));
    }, { passive: true });

    document.addEventListener('mouseout', e => {
        if (!e.relatedTarget && curState !== 'click') setState('');
        else if (curState !== 'click') setState(getState(e.relatedTarget));
    }, { passive: true });

    document.querySelectorAll(CTA_SEL).forEach(btn => {
        btn.addEventListener('mousemove', e => {
            const r = btn.getBoundingClientRect();
            const cx = r.left + r.width / 2;
            const cy = r.top + r.height / 2;
            const dx = (e.clientX - cx) * 0.28;
            const dy = (e.clientY - cy) * 0.28;
            btn.style.transform = `translate(${dx}px, ${dy}px)`;
        });
        btn.addEventListener('mouseleave', () => { btn.style.transform = ''; });
    });
}

/* ══════════════════════════════════════════════════════════
   3. CANVAS PARTICLE FIELD
══════════════════════════════════════════════════════════ */
function initCanvas() {
    const canvas = document.getElementById('heroCanvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let W, H, particles = [], mouseX = -1000, mouseY = -1000;
    const COUNT = 90, LINE_DIST = 130, MOUSE_R = 160;

    function resize() {
        W = canvas.width = canvas.offsetWidth;
        H = canvas.height = canvas.offsetHeight;
    }

    class Particle {
        constructor() { this.reset(true); }
        reset(init = false) {
            this.x = Math.random() * W;
            this.y = init ? Math.random() * H : H + 8;
            this.vx = (Math.random() - 0.5) * 0.3;
            this.vy = -(Math.random() * 0.4 + 0.15);
            this.r = Math.random() * 1.8 + 0.5;
            this.a = Math.random() * 0.5 + 0.15;
            this.hue = Math.random() < 0.5 ? 270 : 190;
        }
        update() {
            const dx = this.x - mouseX, dy = this.y - mouseY;
            const d = Math.hypot(dx, dy);
            if (d < MOUSE_R) {
                const f = (MOUSE_R - d) / MOUSE_R;
                this.vx += (dx / d) * f * 0.6;
                this.vy += (dy / d) * f * 0.6;
            }
            this.vx *= 0.98; this.vy *= 0.98;
            this.x += this.vx; this.y += this.vy;
            if (this.x < 0) this.x = W;
            if (this.x > W) this.x = 0;
            if (this.y < -10) this.reset();
        }
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
            ctx.fillStyle = `hsla(${this.hue},80%,70%,${this.a})`;
            ctx.fill();
        }
    }

    function drawLines() {
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const p1 = particles[i], p2 = particles[j];
                const d = Math.hypot(p1.x - p2.x, p1.y - p2.y);
                if (d < LINE_DIST) {
                    ctx.beginPath();
                    ctx.moveTo(p1.x, p1.y);
                    ctx.lineTo(p2.x, p2.y);
                    ctx.strokeStyle = `rgba(168,85,247,${(1 - d / LINE_DIST) * 0.12})`;
                    ctx.lineWidth = 0.7;
                    ctx.stroke();
                }
            }
        }
    }

    resize();
    particles = Array.from({ length: COUNT }, () => new Particle());
    window.addEventListener('resize', resize, { passive: true });
    canvas.addEventListener('mousemove', e => {
        const r = canvas.getBoundingClientRect();
        mouseX = e.clientX - r.left; mouseY = e.clientY - r.top;
    });
    canvas.addEventListener('mouseleave', () => { mouseX = -1000; mouseY = -1000; });

    (function loop() {
        ctx.clearRect(0, 0, W, H);
        drawLines();
        particles.forEach(p => { p.update(); p.draw(); });
        requestAnimationFrame(loop);
    })();
}

/* ══════════════════════════════════════════════════════════
   4. SCROLL PROGRESS BAR
══════════════════════════════════════════════════════════ */
function initScrollProgress() {
    const bar = document.createElement('div');
    bar.id = 'scrollProgress';
    document.body.prepend(bar);

    let rafId = null;
    let lastPct = -1;

    function update() {
        const scrolled = window.scrollY;
        const total = document.documentElement.scrollHeight - window.innerHeight;
        if (total <= 0) return;

        const pct = Math.min(scrolled / total * 100, 100);
        if (Math.abs(pct - lastPct) < 0.05) { rafId = null; return; }
        lastPct = pct;

        bar.style.setProperty('--p', pct.toFixed(3) + '%');
        bar.style.setProperty('--dot-opacity', pct > 2 && pct < 98 ? '1' : '0');
        bar.classList.toggle('is-scrolled', pct > 0.5);
        rafId = null;
    }

    window.addEventListener('scroll', () => {
        if (!rafId) rafId = requestAnimationFrame(update);
    }, { passive: true });

    window.addEventListener('resize', () => {
        if (!rafId) rafId = requestAnimationFrame(update);
    }, { passive: true });

    update();
}


/* ══════════════════════════════════════════════════════════
   5. NAV — glass scroll + auto-hide + active link
══════════════════════════════════════════════════════════ */
function initNav() {
    const nav = document.getElementById('nav');
    if (!nav) return;

    let lastScroll = 0;
    let ticking = false;

    function updateNav() {
        const y = window.scrollY;
        nav.classList.toggle('scrolled', y > 60);
        if (y > 200) {
            if (y > lastScroll + 8) nav.classList.add('nav--hidden');
            else if (y < lastScroll - 4) nav.classList.remove('nav--hidden');
        } else {
            nav.classList.remove('nav--hidden');
        }
        lastScroll = y;
        ticking = false;
    }

    window.addEventListener('scroll', () => {
        if (!ticking) { requestAnimationFrame(updateNav); ticking = true; }
    }, { passive: true });

    const sections = Array.from(document.querySelectorAll('section[id]'));
    const navLinks = document.querySelectorAll('.nav-link');

    function setActiveLink() {
        const scrollMid = window.scrollY + window.innerHeight * 0.35;
        let current = sections[0];
        sections.forEach(s => { if (s.offsetTop <= scrollMid) current = s; });
        navLinks.forEach(l => {
            l.classList.toggle('nav-active', l.getAttribute('href') === '#' + current.id);
        });
    }

    window.addEventListener('scroll', setActiveLink, { passive: true });
    setActiveLink();
}

/* ══════════════════════════════════════════════════════════
   6. SCROLL REVEAL (multi-direction, staggered)
══════════════════════════════════════════════════════════ */
function initReveal() {
    const elements = document.querySelectorAll('[data-reveal]');
    if (!elements.length) return;

    const obs = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            const el = entry.target;
            const siblings = Array.from(el.parentElement?.querySelectorAll('[data-reveal]') || []);
            const delay = Math.min(siblings.indexOf(el) * 90, 450);
            setTimeout(() => el.classList.add('revealed'), delay);
            obs.unobserve(el);
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

    elements.forEach(el => obs.observe(el));
}

/* ══════════════════════════════════════════════════════════
   7. SECTION CHOREOGRAPHY — stagger children on enter
══════════════════════════════════════════════════════════ */
function initSectionChoreography() {
    const cardSelectors = [
        { sel: '.stack-card', dir: 'up' },
        { sel: '.testimonial-card', dir: 'up' },
        { sel: '.timeline-item', dir: 'left' },
        { sel: '.float-card', dir: 'down' },
        { sel: '.cert-card', dir: 'up' }, // ← cert cards stagger
    ];

    const dirMap = {
        up: 'translateY(36px)',
        down: 'translateY(-24px)',
        left: 'translateX(-32px)',
        right: 'translateX(32px)',
    };

    cardSelectors.forEach(({ sel, dir }) => {
        document.querySelectorAll(sel).forEach((el, i) => {
            if (el.hasAttribute('data-reveal')) return;
            el.style.opacity = '0';
            el.style.transform = dirMap[dir] || 'translateY(28px)';
            el.style.transition = `opacity 0.65s ease ${i * 80}ms, transform 0.65s cubic-bezier(0.22,1,0.36,1) ${i * 80}ms`;

            const obs = new IntersectionObserver(entries => {
                if (entries[0].isIntersecting) {
                    el.style.opacity = '1';
                    el.style.transform = 'none';
                    obs.disconnect();
                }
            }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
            obs.observe(el);
        });
    });
}

/* ══════════════════════════════════════════════════════════
   8. COUNTER ANIMATION
══════════════════════════════════════════════════════════ */
function initCounter() {
    const counters = document.querySelectorAll('[data-count]');
    if (!counters.length) return;

    const easeOut = t => 1 - Math.pow(1 - t, 3);

    const obs = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            const el = entry.target;
            const end = +el.dataset.count;
            let start = null;
            const dur = 1800;

            (function step(ts) {
                if (!start) start = ts;
                const p = Math.min((ts - start) / dur, 1);
                el.textContent = Math.floor(easeOut(p) * end);
                if (p < 1) requestAnimationFrame(step);
                else el.textContent = end;
            })(performance.now());

            obs.unobserve(el);
        });
    }, { threshold: 0.5 });

    counters.forEach(el => obs.observe(el));
}

/* ══════════════════════════════════════════════════════════
   9. TECH STACK FILTER (animated transition)
══════════════════════════════════════════════════════════ */
function initStackFilter() {
    const filters = document.querySelectorAll('.stack-filter');
    const cards = document.querySelectorAll('.stack-card');
    if (!filters.length) return;

    filters.forEach(btn => {
        btn.addEventListener('click', () => {
            const filter = btn.dataset.filter;
            filters.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            cards.forEach((card, i) => {
                const match = filter === 'all' || card.dataset.category === filter;
                if (match) {
                    card.classList.remove('hidden');
                    card.style.animationDelay = `${i * 40}ms`;
                    card.style.animation = 'none';
                    card.offsetHeight;
                    card.style.animation = '';
                    card.style.opacity = '0';
                    card.style.transform = 'scale(0.92) translateY(16px)';
                    requestAnimationFrame(() => {
                        card.style.transition = `opacity 0.4s ease ${i * 40}ms, transform 0.4s cubic-bezier(0.34,1.4,0.64,1) ${i * 40}ms`;
                        card.style.opacity = '1';
                        card.style.transform = '';
                    });
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'scale(0.9)';
                    card.style.transition = 'opacity 0.25s ease, transform 0.25s ease';
                    setTimeout(() => card.classList.add('hidden'), 280);
                }
            });
        });
    });
}

/* ══════════════════════════════════════════════════════════
   10. MOBILE MENU — fullscreen overlay
══════════════════════════════════════════════════════════ */
function initHamburger() {
    const hamburger = document.getElementById('hamburger');
    const overlay = document.getElementById('mobileMenu');
    const closeBtn = document.getElementById('mobClose');
    const bg = document.getElementById('mobOverlayBg');
    if (!hamburger || !overlay) return;

    function openMenu() {
        hamburger.classList.add('is-open');
        overlay.classList.add('is-open');
        overlay.setAttribute('aria-hidden', 'false');
        hamburger.setAttribute('aria-expanded', 'true');
        document.body.style.overflow = 'hidden';
    }

    function closeMenu() {
        hamburger.classList.remove('is-open');
        overlay.classList.remove('is-open');
        overlay.setAttribute('aria-hidden', 'true');
        hamburger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
    }

    hamburger.addEventListener('click', () => {
        overlay.classList.contains('is-open') ? closeMenu() : openMenu();
    });

    if (closeBtn) closeBtn.addEventListener('click', closeMenu);
    if (bg) bg.addEventListener('click', closeMenu);

    overlay.querySelectorAll('.mob-link').forEach(link =>
        link.addEventListener('click', () => setTimeout(closeMenu, 120))
    );

    document.addEventListener('keydown', e => {
        if (e.key === 'Escape' && overlay.classList.contains('is-open')) closeMenu();
    });
}

/* ══════════════════════════════════════════════════════════
   11. CONTACT FORM
══════════════════════════════════════════════════════════ */
function initForm() {
    const form = document.getElementById('contactForm');
    const success = document.getElementById('formSuccess');
    const btn = document.getElementById('submit-contact');
    if (!form) return;

    form.addEventListener('submit', async e => {
        e.preventDefault();
        if (!form.checkValidity()) { form.reportValidity(); return; }

        const orig = btn.innerHTML;
        btn.innerHTML = '<span>Sending…</span>';
        btn.disabled = true;

        await new Promise(r => setTimeout(r, 1400));

        btn.innerHTML = '<span>✓ Sent!</span>';
        btn.style.background = 'linear-gradient(135deg, #059669, #34d399)';
        setTimeout(() => {
            btn.innerHTML = orig;
            btn.style.background = '';
            btn.disabled = false;
        }, 2500);

        form.reset();
        if (success) {
            success.classList.add('visible');
            setTimeout(() => success.classList.remove('visible'), 5000);
        }
    });

    form.querySelectorAll('.form-input').forEach(input => {
        input.addEventListener('focus', () => {
            const label = input.closest('.form-group')?.querySelector('.form-label');
            if (label) label.style.color = 'var(--violet-bright)';
            input.parentElement.style.transform = 'scale(1.008)';
            input.parentElement.style.transition = 'transform 0.25s ease';
        });
        input.addEventListener('blur', () => {
            const label = input.closest('.form-group')?.querySelector('.form-label');
            if (label) label.style.color = '';
            input.parentElement.style.transform = '';
        });
    });
}

/* ══════════════════════════════════════════════════════════
   12. PARALLAX — aurora blobs + mouse tilt
══════════════════════════════════════════════════════════ */
function initParallax() {
    const blobs = document.querySelectorAll('.aurora-blob');
    if (!blobs.length) return;

    let ticking = false;

    window.addEventListener('scroll', () => {
        const targetScroll = window.scrollY;
        if (!ticking) {
            requestAnimationFrame(() => {
                blobs.forEach((blob, i) => {
                    blob.style.transform = `translateY(${targetScroll * (i + 1) * 0.1}px)`;
                });
                ticking = false;
            });
            ticking = true;
        }
    }, { passive: true });

    const hero = document.querySelector('.hero');
    if (!hero) return;

    let mx = 0, my = 0, blobX = [0, 0, 0], blobY = [0, 0, 0];
    hero.addEventListener('mousemove', e => {
        const r = hero.getBoundingClientRect();
        mx = (e.clientX - r.left - r.width / 2) / r.width;
        my = (e.clientY - r.top - r.height / 2) / r.height;
    });

    (function animBlobs() {
        blobs.forEach((blob, i) => {
            const depth = (i + 1) * 18;
            blobX[i] += (mx * depth - blobX[i]) * 0.04;
            blobY[i] += (my * depth - blobY[i]) * 0.04;
            blob.style.marginLeft = blobX[i] + 'px';
            blob.style.marginTop = blobY[i] + 'px';
        });
        requestAnimationFrame(animBlobs);
    })();
}

/* ══════════════════════════════════════════════════════════
   13. SMOOTH SCROLL — anchor links
══════════════════════════════════════════════════════════ */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', e => {
            const target = document.querySelector(anchor.getAttribute('href'));
            if (!target) return;
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    });
}

/* ══════════════════════════════════════════════════════════
   14. CARD TILT — 3-D perspective on .proj-card + .cert-card
══════════════════════════════════════════════════════════ */
function initCardTilt() {
    // ── Project cards (5° tilt) ───────────────────────────────
    document.querySelectorAll('.proj-card').forEach(card => {
        let rafId;
        const MAX_TILT = 5;

        card.addEventListener('mousemove', e => {
            cancelAnimationFrame(rafId);
            rafId = requestAnimationFrame(() => {
                const rect = card.getBoundingClientRect();
                const cx = rect.left + rect.width / 2;
                const cy = rect.top + rect.height / 2;
                const dx = (e.clientX - cx) / (rect.width / 2);
                const dy = (e.clientY - cy) / (rect.height / 2);
                card.style.transition = 'none';
                card.style.transform =
                    `perspective(900px) rotateX(${dy * MAX_TILT * -1}deg) rotateY(${dx * MAX_TILT}deg) translateY(-6px)`;
            });
        });

        card.addEventListener('mouseleave', () => {
            cancelAnimationFrame(rafId);
            card.style.transition = 'transform 0.55s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.4s ease, border-color 0.3s ease';
            card.style.transform = '';
        });
    });

    // ── Certification cards (4° tilt — slightly subtler) ──────
    document.querySelectorAll('.cert-card').forEach(card => {
        let rafId;
        const MAX_TILT = 4;

        card.addEventListener('mousemove', e => {
            cancelAnimationFrame(rafId);
            rafId = requestAnimationFrame(() => {
                const rect = card.getBoundingClientRect();
                const cx = rect.left + rect.width / 2;
                const cy = rect.top + rect.height / 2;
                const dx = (e.clientX - cx) / (rect.width / 2);
                const dy = (e.clientY - cy) / (rect.height / 2);
                card.style.transition = 'none';
                card.style.transform =
                    `perspective(900px) rotateX(${dy * MAX_TILT * -1}deg) rotateY(${dx * MAX_TILT}deg) translateY(-5px)`;
            });
        });

        card.addEventListener('mouseleave', () => {
            cancelAnimationFrame(rafId);
            card.style.transition = 'transform 0.55s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.4s ease, border-color 0.3s ease';
            card.style.transform = '';
        });
    });

    // ── Stack cards — colored glow from icon ─────────────────
    document.querySelectorAll('.stack-card').forEach(card => {
        const icon = card.querySelector('.stack-icon');
        const clr = icon?.style.getPropertyValue('--clr') || 'rgba(109,40,217,0.3)';
        card.addEventListener('mouseenter', () => {
            card.style.boxShadow = `0 20px 48px rgba(0,0,0,0.5), 0 0 28px ${clr}33`;
        });
        card.addEventListener('mouseleave', () => {
            card.style.boxShadow = '';
        });
    });
}

/* ══════════════════════════════════════════════════════════
   15. MAGNETIC BUTTONS
══════════════════════════════════════════════════════════ */
function initMagneticButtons() {
    const strength = 0.28;
    document.querySelectorAll('.btn-primary, .btn-ghost, .nav-cta, [data-magnetic]').forEach(btn => {
        let rafId;

        btn.addEventListener('mousemove', e => {
            cancelAnimationFrame(rafId);
            rafId = requestAnimationFrame(() => {
                const r = btn.getBoundingClientRect();
                const cx = r.left + r.width / 2;
                const cy = r.top + r.height / 2;
                const dx = (e.clientX - cx) * strength;
                const dy = (e.clientY - cy) * strength;
                btn.style.transform = `translate(${dx}px, ${dy}px)`;
                btn.style.transition = 'transform 0.15s ease';
            });
        });

        btn.addEventListener('mouseleave', () => {
            cancelAnimationFrame(rafId);
            btn.style.transform = '';
            btn.style.transition = 'transform 0.5s cubic-bezier(0.34,1.56,0.64,1)';
        });
    });
}

/* ══════════════════════════════════════════════════════════
   16. RIPPLE EFFECT — button clicks
══════════════════════════════════════════════════════════ */
function initRipple() {
    document.querySelectorAll('.btn-primary, .btn-ghost').forEach(btn => {
        if (getComputedStyle(btn).position === 'static') btn.style.position = 'relative';
        btn.style.overflow = 'hidden';

        btn.addEventListener('click', e => {
            const r = btn.getBoundingClientRect();
            const size = Math.max(r.width, r.height) * 2;
            const x = e.clientX - r.left;
            const y = e.clientY - r.top;

            const ripple = document.createElement('span');
            Object.assign(ripple.style, {
                position: 'absolute',
                borderRadius: '50%',
                width: size + 'px',
                height: size + 'px',
                left: (x - size / 2) + 'px',
                top: (y - size / 2) + 'px',
                background: 'rgba(255,255,255,0.18)',
                transform: 'scale(0)',
                pointerEvents: 'none',
                animation: 'rippleAnim 0.55s ease-out forwards',
            });
            btn.appendChild(ripple);
            ripple.addEventListener('animationend', () => ripple.remove());
        });
    });

    if (!document.getElementById('rippleStyle')) {
        const s = document.createElement('style');
        s.id = 'rippleStyle';
        s.textContent = `@keyframes rippleAnim { to { transform: scale(1); opacity: 0; } }`;
        document.head.appendChild(s);
    }
}

/* ══════════════════════════════════════════════════════════
   17. FLOATING ICONS — stack icons gentle bob
══════════════════════════════════════════════════════════ */
function initFloatingIcons() {
    document.querySelectorAll('.stack-icon').forEach((icon, i) => {
        const period = 3500 + i * 120;
        const offset = i * 400;
        let start = null;

        (function float(ts) {
            if (!start) start = ts;
            const t = ((ts - start + offset) % period) / period;
            const dy = Math.sin(t * Math.PI * 2) * 3;
            icon.style.transform = `translateY(${dy}px)`;
            requestAnimationFrame(float);
        })(performance.now());
    });
}

/* ══════════════════════════════════════════════════════════
   18. TYPING TEXT — Hero role word
══════════════════════════════════════════════════════════ */
function initTyping() {
    const el = document.getElementById('heroRole');
    if (!el) return;

    const roles = ['Developer', 'Engineer', 'Designer', 'Problem Solver', 'Architect'];
    let rIdx = 0, cIdx = roles[0].length, deleting = false;
    el.textContent = roles[0];

    function type() {
        const word = roles[rIdx];
        if (!deleting) {
            el.textContent = word.slice(0, ++cIdx);
            if (cIdx === word.length) {
                deleting = true;
                return setTimeout(type, 2000);
            }
        } else {
            el.textContent = word.slice(0, --cIdx);
            if (cIdx === 0) {
                deleting = false;
                rIdx = (rIdx + 1) % roles.length;
            }
        }
        setTimeout(type, deleting ? 38 : 65);
    }

    setTimeout(type, 2800);
}

/* ══════════════════════════════════════════════════════════
   19. PROJECT FILTER — stagger filter with enter/exit animations
══════════════════════════════════════════════════════════ */
function initProjectFilter() {
    const filterBtns = document.querySelectorAll('.proj-filter');
    const cards = document.querySelectorAll('.proj-card');
    const grid = document.getElementById('projectsGrid');
    if (!filterBtns.length || !cards.length || !grid) return;

    let currentFilter = 'all';
    let isAnimating = false;

    function cardMatches(card, filter) {
        if (filter === 'all') return true;
        const cats = (card.dataset.pc || '').split(/\s+/);
        return cats.includes(filter);
    }

    function updateCounts(filter) {
        filterBtns.forEach(btn => {
            const f = btn.dataset.pf;
            const count = Array.from(cards).filter(c => {
                if (f === 'all') return true;
                return (c.dataset.pc || '').split(/\s+/).includes(f);
            }).length;
            const badge = btn.querySelector('.pf-count');
            if (badge) {
                badge.textContent = count;
                badge.style.transform = 'scale(1.25)';
                setTimeout(() => { badge.style.transform = ''; }, 300);
            }
        });
    }

    function clearNoResults() {
        const el = grid.querySelector('.proj-no-results');
        if (el) el.remove();
    }

    function showNoResults() {
        clearNoResults();
        const div = document.createElement('div');
        div.className = 'proj-no-results';
        div.innerHTML = `
            <span class="proj-no-results-icon">🔍</span>
            <span class="proj-no-results-text">No projects found for this category yet.</span>
        `;
        grid.appendChild(div);
    }

    function applyFilter(filter) {
        if (filter === currentFilter || isAnimating) return;
        isAnimating = true;
        currentFilter = filter;

        const toShow = [];
        const toHide = [];

        cards.forEach(card => {
            const shouldShow = cardMatches(card, filter);
            const isHidden = card.classList.contains('proj-card--hidden');
            if (shouldShow) toShow.push(card);
            else if (!isHidden) toHide.push(card);
        });

        clearNoResults();

        const EXIT_DUR = 280;
        toHide.forEach((card, i) => {
            card.style.animationDelay = `${i * 30}ms`;
            card.classList.remove('proj-card--entering');
            card.classList.add('proj-card--exiting');
        });

        setTimeout(() => {
            toHide.forEach(card => {
                card.classList.remove('proj-card--exiting');
                card.classList.add('proj-card--hidden');
                card.style.animationDelay = '';
            });

            if (toShow.length === 0) {
                showNoResults();
                isAnimating = false;
                return;
            }

            toShow.forEach((card, i) => {
                card.classList.remove('proj-card--hidden', 'proj-card--exiting');
                card.style.animationDelay = `${i * 65}ms`;
                card.classList.add('proj-card--entering');
            });

            const maxEnterDelay = toShow.length * 65 + 450;
            setTimeout(() => {
                toShow.forEach(card => {
                    card.classList.remove('proj-card--entering');
                    card.style.animationDelay = '';
                });
                isAnimating = false;
            }, maxEnterDelay);

        }, toHide.length > 0 ? EXIT_DUR : 0);
    }

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const filter = btn.dataset.pf;
            filterBtns.forEach(b => {
                b.classList.remove('active');
                b.setAttribute('aria-pressed', 'false');
            });
            btn.classList.add('active');
            btn.setAttribute('aria-pressed', 'true');
            updateCounts(filter);
            applyFilter(filter);
        });
    });

    cards.forEach(card => {
        card.classList.remove('proj-card--hidden', 'proj-card--entering', 'proj-card--exiting');
    });
}

/* ══════════════════════════════════════════════════════════
   20. CERT FILTER — animated stagger filter for certifications
══════════════════════════════════════════════════════════ */
function initCertFilter() {
    const filterBtns = document.querySelectorAll('.cert-filter');
    const cards = document.querySelectorAll('.cert-card');
    const grid = document.getElementById('certsGrid');
    if (!filterBtns.length || !cards.length || !grid) return;

    let currentFilter = 'all';
    let isAnimating = false;

    function cardMatches(card, filter) {
        if (filter === 'all') return true;
        const cats = (card.dataset.cc || '').split(/\s+/);
        return cats.includes(filter);
    }

    function updateCounts(filter) {
        filterBtns.forEach(btn => {
            const f = btn.dataset.cf;
            const count = Array.from(cards).filter(c => {
                if (f === 'all') return true;
                return (c.dataset.cc || '').split(/\s+/).includes(f);
            }).length;
            const badge = btn.querySelector('.cf-count');
            if (!badge) return;
            badge.textContent = count;
            badge.style.transform = 'scale(1.3)';
            setTimeout(() => { badge.style.transform = ''; }, 280);
        });
    }

    function clearNoResults() {
        const el = grid.querySelector('.cert-no-results');
        if (el) el.remove();
    }

    function showNoResults() {
        clearNoResults();
        const div = document.createElement('div');
        div.className = 'cert-no-results';
        div.innerHTML = `
            <span class="cert-no-results-icon">🔍</span>
            <span class="cert-no-results-text">No certifications found for this category.</span>
        `;
        grid.appendChild(div);
    }

    function applyFilter(filter) {
        if (filter === currentFilter || isAnimating) return;
        isAnimating = true;
        currentFilter = filter;

        const toShow = [];
        const toHide = [];

        cards.forEach(card => {
            const shouldShow = cardMatches(card, filter);
            const isHidden = card.classList.contains('cert-card--hidden');
            if (shouldShow) toShow.push(card);
            else if (!isHidden) toHide.push(card);
        });

        clearNoResults();

        const EXIT_DUR = 260;
        toHide.forEach((card, i) => {
            card.style.animationDelay = `${i * 25}ms`;
            card.classList.remove('cert-card--entering');
            card.classList.add('cert-card--exiting');
        });

        setTimeout(() => {
            toHide.forEach(card => {
                card.classList.remove('cert-card--exiting');
                card.classList.add('cert-card--hidden');
                card.style.animationDelay = '';
            });

            if (toShow.length === 0) {
                showNoResults();
                isAnimating = false;
                return;
            }

            toShow.forEach((card, i) => {
                card.classList.remove('cert-card--hidden', 'cert-card--exiting');
                card.style.animationDelay = `${i * 55}ms`;
                card.classList.add('cert-card--entering');
            });

            const maxDelay = toShow.length * 55 + 420;
            setTimeout(() => {
                toShow.forEach(card => {
                    card.classList.remove('cert-card--entering');
                    card.style.animationDelay = '';
                });
                isAnimating = false;
            }, maxDelay);

        }, toHide.length > 0 ? EXIT_DUR : 0);
    }

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const filter = btn.dataset.cf;
            filterBtns.forEach(b => {
                b.classList.remove('active');
                b.setAttribute('aria-pressed', 'false');
            });
            btn.classList.add('active');
            btn.setAttribute('aria-pressed', 'true');
            updateCounts(filter);
            applyFilter(filter);
        });
    });

    // Init: apply "webdev" filter immediately (matches default active button in HTML)
    const DEFAULT_FILTER = 'webdev';
    currentFilter = 'all'; // reset so applyFilter doesn't bail on same-filter guard
    cards.forEach(card => {
        card.classList.remove('cert-card--hidden', 'cert-card--entering', 'cert-card--exiting');
    });
    // Short defer so DOM is painted before we run the exit animation
    requestAnimationFrame(() => applyFilter(DEFAULT_FILTER));
}

/* ══════════════════════════════════════════════════════════
   21. THEME TOGGLE — Dark ↔ Light with localStorage persistence
══════════════════════════════════════════════════════════ */
function initThemeToggle() {
    const btn = document.getElementById('themeToggle');
    const root = document.documentElement;
    const KEY = 'portfolio-theme';

    const saved = localStorage.getItem(KEY) || 'dark';
    applyTheme(saved, false);

    if (!btn) return;

    btn.addEventListener('click', () => {
        const current = root.getAttribute('data-theme') || 'dark';
        const next = current === 'dark' ? 'light' : 'dark';
        applyTheme(next, true);
        localStorage.setItem(KEY, next);
    });

    function applyTheme(theme, animate) {
        if (animate) flashTransition();
        root.setAttribute('data-theme', theme);
        if (btn) {
            btn.setAttribute('aria-label',
                theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'
            );
            btn.title = theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode';
        }
    }

    function flashTransition() {
        const flash = document.createElement('div');
        Object.assign(flash.style, {
            position: 'fixed',
            inset: '0',
            zIndex: '99999',
            pointerEvents: 'none',
            background: 'rgba(255, 255, 255, 0.06)',
            backdropFilter: 'brightness(1.08)',
            opacity: '1',
            transition: 'opacity 0.4s ease',
        });
        document.body.appendChild(flash);
        requestAnimationFrame(() => {
            requestAnimationFrame(() => {
                flash.style.opacity = '0';
                flash.addEventListener('transitionend', () => flash.remove(), { once: true });
            });
        });
    }
}

/* ══════════════════════════════════════════════════════════
   22. BACK-TO-TOP FAB
══════════════════════════════════════════════════════════ */
function initBackToTop() {
    const btn = document.getElementById('backToTop');
    if (!btn) return;

    const SHOW_AT = 400;
    let ticking = false;

    function update() {
        btn.classList.toggle('visible', window.scrollY > SHOW_AT);
        ticking = false;
    }

    window.addEventListener('scroll', () => {
        if (!ticking) { requestAnimationFrame(update); ticking = true; }
    }, { passive: true });

    btn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    update();
}

/* ══════════════════════════════════════════════════════════
   23. CERT MODAL — Lightbox viewer for certificate images
══════════════════════════════════════════════════════════ */
function initCertModal() {
    // ── Element refs ─────────────────────────────────────────
    const modal = document.getElementById('certModal');
    const backdrop = document.getElementById('certModalBackdrop');
    const card = document.getElementById('certModalCard');
    const closeBtn = document.getElementById('certModalClose');
    const img = document.getElementById('certModalImg');
    const skeleton = document.getElementById('certModalSkeleton');
    const errorEl = document.getElementById('certModalError');
    const titleEl = document.getElementById('certModalTitle');
    const metaEl = document.getElementById('certModalMeta');
    const dotEl = document.getElementById('certModalDot');
    const qrNote = document.getElementById('certModalQrNote');
    const verifyBtn = document.getElementById('certModalVerifyBtn');

    // Guard — bail if modal HTML isn't on the page yet
    if (!modal || !img) return;

    // ── Open modal ────────────────────────────────────────────
    function openModal(certCard) {
        // Read data attributes from the cert card element
        const imgSrc = certCard.dataset.certImg || '';
        const title = certCard.dataset.certTitle || 'Certificate';
        const meta = certCard.dataset.certMeta || '';
        const color = certCard.dataset.certColor || '#a78bfa';
        const verifyUrl = certCard.dataset.certUrl || '';

        // ── Populate header ───────────────────────────────────
        titleEl.textContent = title;
        metaEl.innerHTML = meta;          // allows &mdash; entities
        dotEl.style.background = color;
        dotEl.style.color = color;      // used for box-shadow

        // ── Footer: QR note vs verify button ─────────────────
        if (verifyUrl && verifyUrl.trim() !== '') {
            // Has a public verify URL — show the button
            verifyBtn.href = verifyUrl;
            verifyBtn.classList.add('visible');
            verifyBtn.setAttribute('aria-hidden', 'false');
            qrNote.classList.remove('visible');
            qrNote.setAttribute('aria-hidden', 'true');
        } else {
            // QR-only cert — show the scan note
            qrNote.classList.add('visible');
            qrNote.setAttribute('aria-hidden', 'false');
            verifyBtn.classList.remove('visible');
            verifyBtn.setAttribute('aria-hidden', 'true');
            verifyBtn.href = '#';
        }

        // ── Reset image state ─────────────────────────────────
        img.classList.remove('loaded');
        img.src = '';
        img.alt = title;
        skeleton.classList.remove('hidden');
        errorEl.classList.remove('visible');
        errorEl.setAttribute('aria-hidden', 'true');

        // ── Load image ────────────────────────────────────────
        if (imgSrc) {
            const tempImg = new Image();

            tempImg.onload = () => {
                img.src = imgSrc;
                img.classList.add('loaded');
                skeleton.classList.add('hidden');
            };

            tempImg.onerror = () => {
                skeleton.classList.add('hidden');
                errorEl.classList.add('visible');
                errorEl.setAttribute('aria-hidden', 'false');
            };

            tempImg.src = imgSrc;
        } else {
            // No image path provided
            skeleton.classList.add('hidden');
            errorEl.classList.add('visible');
            errorEl.setAttribute('aria-hidden', 'false');
        }

        // ── Show modal ────────────────────────────────────────
        modal.classList.add('is-open');
        modal.setAttribute('aria-hidden', 'false');
        document.body.classList.add('cert-modal-open');

        // Focus the close button for accessibility
        requestAnimationFrame(() => {
            requestAnimationFrame(() => closeBtn.focus());
        });
    }

    // ── Close modal ───────────────────────────────────────────
    function closeModal() {
        modal.classList.remove('is-open');
        modal.setAttribute('aria-hidden', 'true');
        document.body.classList.remove('cert-modal-open');

        // Clean up image after transition ends so no flash on reopen
        const TRANSITION_MS = 420;
        setTimeout(() => {
            img.src = '';
            img.classList.remove('loaded');
        }, TRANSITION_MS);
    }

    // ── Event listeners ───────────────────────────────────────

    // Close button
    closeBtn.addEventListener('click', closeModal);

    // Backdrop click
    backdrop.addEventListener('click', closeModal);

    // Escape key
    document.addEventListener('keydown', e => {
        if (e.key === 'Escape' && modal.classList.contains('is-open')) {
            closeModal();
        }
    });

    // Prevent closing when clicking inside the card itself
    card.addEventListener('click', e => e.stopPropagation());

    // ── Wire up all Preview buttons on cert cards ─────────────
    // Uses event delegation on document so it works even if cards
    // are dynamically added (e.g. after filter re-renders)
    document.addEventListener('click', e => {
        const previewBtn = e.target.closest('.cert-preview-btn');
        if (!previewBtn) return;

        // Walk up to find the .cert-card element that holds the data attrs
        const certCard = previewBtn.closest('.cert-card');
        if (!certCard) return;

        e.stopPropagation();
        openModal(certCard);
    });
}

/* ══════════════════════════════════════════════════════════
   24. RESUME DROPDOWN + PDF MODAL
══════════════════════════════════════════════════════════ */
function initResumeDropdown() {
    // ── Dropdown elements ────────────────────────────────────
    const dropdown = document.getElementById('resumeDropdown');
    const btn = document.getElementById('resumeBtn');
    const menu = document.getElementById('resumeMenu');

    // ── Modal elements ───────────────────────────────────────
    const modal = document.getElementById('resumeModal');
    const backdrop = document.getElementById('resumeModalBackdrop');
    const card = document.getElementById('resumeModalCard');
    const closeBtn = document.getElementById('resumeModalClose');
    const iframe = document.getElementById('resumeModalIframe');
    const skeleton = document.getElementById('resumeModalSkeleton');
    const errorEl = document.getElementById('resumeModalError');
    const titleEl = document.getElementById('resumeModalTitle');
    const downloadBtn = document.getElementById('resumeDownloadBtn');

    if (!modal || !iframe) return;

    // ── Dropdown toggle ──────────────────────────────────────
    function openDropdown() {
        btn.classList.add('is-open');
        menu.classList.add('is-open');
        btn.setAttribute('aria-expanded', 'true');
        menu.setAttribute('aria-hidden', 'false');
    }

    function closeDropdown() {
        btn.classList.remove('is-open');
        menu.classList.remove('is-open');
        btn.setAttribute('aria-expanded', 'false');
        menu.setAttribute('aria-hidden', 'true');
    }

    if (btn && menu) {
        btn.addEventListener('click', e => {
            e.stopPropagation();
            btn.classList.contains('is-open') ? closeDropdown() : openDropdown();
        });

        // Close on outside click
        document.addEventListener('click', e => {
            if (dropdown && !dropdown.contains(e.target)) closeDropdown();
        });

        // Close on Escape
        document.addEventListener('keydown', e => {
            if (e.key === 'Escape' && btn.classList.contains('is-open')) closeDropdown();
        });
    }

    // ── Open PDF modal ───────────────────────────────────────
    function openResumeModal(src, label, downloadName) {
        // Reset state
        iframe.classList.remove('loaded');
        iframe.src = '';
        skeleton.classList.remove('hidden');
        errorEl.classList.remove('visible');
        errorEl.setAttribute('aria-hidden', 'true');

        // Set title + download
        titleEl.textContent = label;
        downloadBtn.href = src;
        downloadBtn.download = downloadName || label + '.pdf';

        // Load iframe
        iframe.onload = () => {
            skeleton.classList.add('hidden');
            iframe.classList.add('loaded');
        };

        iframe.onerror = () => {
            skeleton.classList.add('hidden');
            errorEl.classList.add('visible');
            errorEl.setAttribute('aria-hidden', 'false');
        };

        // Small delay so modal animation starts first
        setTimeout(() => {
            if (src) {
                iframe.src = src;
            } else {
                skeleton.classList.add('hidden');
                errorEl.classList.add('visible');
                errorEl.setAttribute('aria-hidden', 'false');
            }
        }, 80);

        // Show modal
        modal.classList.add('is-open');
        modal.setAttribute('aria-hidden', 'false');
        document.body.classList.add('resume-modal-open');

        requestAnimationFrame(() => {
            requestAnimationFrame(() => closeBtn && closeBtn.focus());
        });
    }

    // ── Close modal ──────────────────────────────────────────
    function closeResumeModal() {
        modal.classList.remove('is-open');
        modal.setAttribute('aria-hidden', 'true');
        document.body.classList.remove('resume-modal-open');
        setTimeout(() => {
            iframe.src = '';
            iframe.classList.remove('loaded');
        }, 350);
    }

    // ── Wire close button + backdrop ─────────────────────────
    if (closeBtn) closeBtn.addEventListener('click', closeResumeModal);
    if (backdrop) backdrop.addEventListener('click', closeResumeModal);
    if (card) card.addEventListener('click', e => e.stopPropagation());

    // Escape key (only when resume modal is open)
    document.addEventListener('keydown', e => {
        if (e.key === 'Escape' && modal.classList.contains('is-open')) {
            closeResumeModal();
        }
    });

    // ── Event delegation for all resume trigger buttons ──────
    // Handles both desktop dropdown items AND mobile buttons
    document.addEventListener('click', e => {
        const trigger = e.target.closest('[data-resume-src]');
        if (!trigger) return;

        const src = trigger.dataset.resumeSrc || '';
        const label = trigger.dataset.resumeLabel || 'Resume';
        const name = trigger.dataset.resumeName || label + '.pdf';

        closeDropdown();
        openResumeModal(src, label, name);
    });
}

/* ══════════════════════════════════════════════════════════
   22. PROJECT REAL IMAGES
   — Lazy-load actual screenshots into each .proj-card.
   — Dual-image crossfade: Light shown by default in light-mode,
     Dark shown by default in dark-mode; hover always swaps.
   — Skeleton shimmer while images load.
   — Graceful no-op fallback when image is not available.
══════════════════════════════════════════════════════════ */
function initProjectImages() {

    // ── Image map ────────────────────────────────────────────────
    // Key  = article[id]  of the .proj-card element
    // base = image shown in LIGHT mode (or the only image)
    // alt  = image shown in DARK  mode (omit if single-image)
    const IMAGE_MAP = {
        'proj-habitflow':    { base: 'ProjectImages/HabitFlow(Light).png',   alt: 'ProjectImages/HabitFlow(Night).png' },
        'proj-riderent':     { base: 'ProjectImages/RideRent(Light).png',    alt: 'ProjectImages/RideRent(Night).png'  },
        'proj-dicegame':     { base: 'ProjectImages/DiceGame(Light).png',    alt: 'ProjectImages/DiceGame(Night).png'  },
        'proj-portfolio':    { base: 'ProjectImages/Portfolio(Light).png',   alt: 'ProjectImages/Portfolio(Night).png' },
        'proj-drumkit':      { base: 'ProjectImages/DrumKit.png'                                                       },
        'proj-simongame':    { base: 'ProjectImages/SimonGame.png'                                                     },
        'proj-zomato':       { base: 'ProjectImages/Zomato.png'                                                        },
        'proj-qrcode':       { base: 'ProjectImages/QR_Code_Generator.png'                                             },
        'proj-fitkart':      { base: 'ProjectImages/FitKart.png'                                                       },
        'proj-knowledgenet': { base: 'ProjectImages/KnowledgeNet.png'                                                  },
        // proj-margdarshak, proj-attendance, proj-codexaminer → no entry → mockup kept
    };

    // ── Inject images into a single card ────────────────────────
    function injectCard(card) {
        const id = card.id;
        const entry = IMAGE_MAP[id];
        if (!entry) return; // No image available — leave the mockup intact

        const wrap = card.querySelector('.proj-img-wrap');
        if (!wrap) return;

        const hasDual = Boolean(entry.alt);

        // ── Build the container that sits over the mockup ─────
        const imgWrap = document.createElement('div');
        imgWrap.className = 'proj-real-img-wrap';

        // ── Skeleton shimmer ──────────────────────────────────
        const skeleton = document.createElement('div');
        skeleton.className = 'proj-img-skeleton';
        imgWrap.appendChild(skeleton);

        // ── Base image (Light / single) ───────────────────────
        const baseImg = document.createElement('img');
        baseImg.className = 'proj-real-img proj-real-img--base';
        if (hasDual) baseImg.classList.add('has-alt');
        baseImg.alt = card.querySelector('.proj-title')?.textContent?.trim() || id;
        baseImg.loading  = 'lazy';
        baseImg.decoding = 'async';
        imgWrap.appendChild(baseImg);

        // ── Alternate image (Dark / Night) ────────────────────
        let altImg = null;
        if (hasDual) {
            altImg = document.createElement('img');
            altImg.className = 'proj-real-img proj-real-img--alt';
            altImg.alt      = baseImg.alt + ' (dark)';
            altImg.loading  = 'lazy';
            altImg.decoding = 'async';
            imgWrap.appendChild(altImg);
        }

        // ── Theme-swap hint badge (only for dual-image cards) ─
        if (hasDual) {
            const badge = document.createElement('span');
            badge.className   = 'proj-theme-badge';
            badge.innerHTML   = '<span class="proj-theme-badge-dot"></span>Hover to toggle theme';
            badge.setAttribute('aria-hidden', 'true');
            imgWrap.appendChild(badge);
        }

        // ── Append container into the card's image wrapper ────
        // Keep the existing mockup behind in case images fail
        wrap.style.position = 'relative';
        wrap.appendChild(imgWrap);

        // ── Image-load helpers ────────────────────────────────
        let loadedCount = 0;
        const totalImages = hasDual ? 2 : 1;

        function onImageLoad(img) {
            img.classList.add('is-loaded');
            loadedCount++;
            if (loadedCount >= totalImages) {
                // All images ready — hide skeleton
                skeleton.classList.add('is-hidden');
            }
        }

        function onImageError(img, src) {
            // If image fails, remove the whole imgWrap so mockup shows
            console.warn(`[ProjectImages] Failed to load: ${src}`);
            imgWrap.remove();
        }

        // ── Set src only when card enters viewport ────────────
        // (already using loading="lazy" for native lazy-load,
        //  but we also defer the src assignment with IO for
        //  maximum control — avoids any hidden preload)
        return { imgWrap, baseImg, altImg, skeleton, entry };
    }

    // ── Collect all cards and set up IntersectionObserver ────────
    const cards = document.querySelectorAll('.proj-card[id]');
    if (!cards.length) return;

    const io = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            const card = entry.target;
            io.unobserve(card); // Only trigger once

            // Retrieve the deferred payload we stored on the card
            const payload = card._imgPayload;
            if (!payload) return;

            const { imgWrap, baseImg, altImg, skeleton, entry: imgEntry } = payload;

            // ── Load base image ──────────────────────────────
            baseImg.addEventListener('load', () => {
                baseImg.classList.add('is-loaded');
                if (!altImg) skeleton.classList.add('is-hidden');
            }, { once: true });

            baseImg.addEventListener('error', () => {
                console.warn(`[ProjectImages] Base image not found: ${imgEntry.base}`);
                imgWrap.remove(); // Fallback: show original mockup
            }, { once: true });

            baseImg.src = imgEntry.base;

            // ── Load alternate image ─────────────────────────
            if (altImg) {
                altImg.addEventListener('load', () => {
                    altImg.classList.add('is-loaded');
                    skeleton.classList.add('is-hidden');
                }, { once: true });

                altImg.addEventListener('error', () => {
                    // Alt failed — keep base only, remove alt ref
                    console.warn(`[ProjectImages] Alt image not found: ${imgEntry.alt}`);
                    altImg.remove();
                    baseImg.classList.remove('has-alt');
                    // Remove badge since there's no alt to swap to
                    imgWrap.querySelector('.proj-theme-badge')?.remove();
                }, { once: true });

                altImg.src = imgEntry.alt;
            }
        });
    }, {
        rootMargin: '200px 0px', // Pre-load 200px before entering viewport
        threshold: 0,
    });

    // ── Build DOM for each card, store payload, start observing ──
    cards.forEach(card => {
        const payload = injectCard(card);
        if (!payload) return;
        card._imgPayload = payload;
        io.observe(card);
    });
}

/* ════════════════════════════════════════════════════════
   23. PROJECT SECTIONS
   — Reorganises existing flat card list into:
       ► Featured (4 priority projects)
       ► Currently Working On (AI Attendance)
       ► All Others (8 remaining, hidden by default)
   — "View All Projects" toggle with smooth CSS grid animation
   — Auto-expands hidden section when a category filter is active
════════════════════════════════════════════════════════ */
function initProjSections() {
    const container = document.getElementById('projectsGrid');
    if (!container) return;

    // ── Define section membership by article[id] ────────────────
    const FEATURED_IDS = ['proj-habitflow', 'proj-riderent', 'proj-margdarshak', 'proj-codexaminer'];
    const WIP_IDS      = ['proj-attendance'];
    // Everything else goes into "All Others"

    // Gather all existing cards in DOM order
    const allCards = Array.from(container.querySelectorAll('.proj-card'));
    if (!allCards.length) return;

    // Classify
    const featuredCards = allCards.filter(c => FEATURED_IDS.includes(c.id));
    const wipCards      = allCards.filter(c => WIP_IDS.includes(c.id));
    const otherCards    = allCards.filter(c =>
        !FEATURED_IDS.includes(c.id) && !WIP_IDS.includes(c.id)
    );

    // ── Helpers ──────────────────────────────────────────
    function makeSectionHeader(labelText, dotClass, count) {
        const hd = document.createElement('div');
        hd.className = 'proj-section-hd';
        hd.innerHTML = `
            <div class="proj-section-label">
                <span class="proj-section-label-dot ${dotClass || ''}"></span>
                ${labelText}
            </div>
            <span class="proj-section-count">${count} project${count !== 1 ? 's' : ''}</span>
            <div class="proj-section-hd-line"></div>
        `;
        return hd;
    }

    function makeSection(className, headerEl, cards) {
        const sec = document.createElement('section');
        sec.className = `proj-section ${className}`;
        sec.appendChild(headerEl);
        const grid = document.createElement('div');
        grid.className = 'proj-grid';
        cards.forEach(c => grid.appendChild(c));
        sec.appendChild(grid);
        return sec;
    }

    // ── Build sections ──────────────────────────────────────
    // Clear container (cards still in memory)
    container.innerHTML = '';

    // 1 — Featured
    if (featuredCards.length) {
        const sec = makeSection(
            'proj-section--featured',
            makeSectionHeader('⭐ Top Featured Projects', '', featuredCards.length),
            featuredCards
        );
        container.appendChild(sec);
    }

    // 2 — WIP
    if (wipCards.length) {
        // Inject WIP badge + modifier class into each WIP card
        wipCards.forEach(card => {
            card.classList.add('proj-card--wip');
            // Remove old featured ribbon if present, add WIP badge
            if (!card.querySelector('.proj-wip-badge')) {
                const badge = document.createElement('div');
                badge.className = 'proj-wip-badge';
                badge.setAttribute('aria-label', 'Currently in development');
                badge.innerHTML = '<span class="proj-wip-badge-dot"></span>Working On';
                card.appendChild(badge);
            }
        });
        const sec = makeSection(
            'proj-section--wip',
            makeSectionHeader('Currently Working On', 'wip-dot', wipCards.length),
            wipCards
        );
        container.appendChild(sec);
    }

    // 3 — Toggle button
    const toggleWrap = document.createElement('div');
    toggleWrap.className = 'proj-toggle-wrap';
    const toggleBtn = document.createElement('button');
    toggleBtn.id = 'projToggleBtn';
    toggleBtn.className = 'proj-toggle-btn';
    toggleBtn.setAttribute('aria-expanded', 'false');
    toggleBtn.setAttribute('aria-controls', 'projAllSection');
    toggleBtn.innerHTML = `
        <span class="proj-toggle-label">View All Projects</span>
        <span class="proj-toggle-count">${otherCards.length}</span>
        <svg class="proj-toggle-arrow" viewBox="0 0 24 24" fill="none"
             stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="6 9 12 15 18 9"/>
        </svg>
    `;
    toggleWrap.appendChild(toggleBtn);
    container.appendChild(toggleWrap);

    // 4 — All-Others (hidden)
    let allSection = null;
    if (otherCards.length) {
        allSection = document.createElement('section');
        allSection.id = 'projAllSection';
        allSection.className = 'proj-section proj-section--all';
        allSection.setAttribute('aria-hidden', 'true');

        // The inner wrapper is required for the grid-template-rows trick
        const inner = document.createElement('div');
        inner.className = 'proj-section-inner';

        const hd = makeSectionHeader('All Projects', '', otherCards.length);
        inner.appendChild(hd);

        const grid = document.createElement('div');
        grid.className = 'proj-grid';
        otherCards.forEach(c => grid.appendChild(c));
        inner.appendChild(grid);

        allSection.appendChild(inner);
        container.appendChild(allSection);
    }

    // ── Toggle logic ──────────────────────────────────────
    let isOpen = false;
    const labelEl = toggleBtn.querySelector('.proj-toggle-label');

    function openAll(silent) {
        if (!allSection) return;
        isOpen = true;
        allSection.classList.add('is-open');
        allSection.setAttribute('aria-hidden', 'false');
        toggleBtn.classList.add('is-open');
        toggleBtn.setAttribute('aria-expanded', 'true');
        if (labelEl) labelEl.textContent = 'Show Less';
        if (!silent) {
            // Scroll toggle button into view so user sees what happened
            setTimeout(() => toggleBtn.scrollIntoView({ behavior: 'smooth', block: 'nearest' }), 80);
        }
    }

    function closeAll() {
        if (!allSection) return;
        isOpen = false;
        allSection.classList.remove('is-open');
        allSection.setAttribute('aria-hidden', 'true');
        toggleBtn.classList.remove('is-open');
        toggleBtn.setAttribute('aria-expanded', 'false');
        if (labelEl) labelEl.textContent = 'View All Projects';
    }

    toggleBtn.addEventListener('click', () => {
        isOpen ? closeAll() : openAll(false);
    });

    // ── Auto-expand when a category filter is applied ────────
    // If someone clicks "AI" filter, show all cards (incl. hidden section)
    // so no project is invisible during filtering.
    const filterBtns = document.querySelectorAll('.proj-filter');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const filter = btn.dataset.pf;
            if (filter && filter !== 'all' && !isOpen) {
                openAll(true); // silent = no scroll
            }
        });
    });

    // Expose for other modules (e.g. if filter wants to collapse)
    window._projSections = { openAll, closeAll, getIsOpen: () => isOpen };
}
