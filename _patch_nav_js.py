
f = r"d:\Documents\Z_PORTFOLIO\main.js"
with open(f, "r", encoding="utf-8") as fh:
    js = fh.read()

# Replace initNav and initHamburger with updated versions
OLD_NAV_BLOCK = """/* ══════════════════════════════════════════════════════════
   5. NAV — sticky + active link highlighting
══════════════════════════════════════════════════════════ */
function initNav() {
    const nav = document.getElementById('nav');
    if (!nav) return;

    window.addEventListener('scroll', () => {
        nav.classList.toggle('scrolled', window.scrollY > 60);
    }, { passive: true });

    // Active nav link via IntersectionObserver
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');

    const obs = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            navLinks.forEach(l => l.classList.remove('nav-active'));
            const active = nav.querySelector(`.nav-link[href="#${entry.target.id}"]`);
            if (active) active.classList.add('nav-active');
        });
    }, { threshold: 0.35, rootMargin: '-80px 0px 0px 0px' });

    sections.forEach(s => obs.observe(s));
}"""

NEW_NAV_BLOCK = """/* ══════════════════════════════════════════════════════════
   5. NAV — glass scroll + auto-hide + active link
══════════════════════════════════════════════════════════ */
function initNav() {
    const nav = document.getElementById('nav');
    if (!nav) return;

    let lastScroll = 0;
    let ticking = false;

    function updateNav() {
        const y = window.scrollY;
        // Glass effect after 60px
        nav.classList.toggle('scrolled', y > 60);
        // Auto-hide on scroll down, show on scroll up
        if (y > 200) {
            if (y > lastScroll + 8) {
                nav.classList.add('nav--hidden');
            } else if (y < lastScroll - 4) {
                nav.classList.remove('nav--hidden');
            }
        } else {
            nav.classList.remove('nav--hidden');
        }
        lastScroll = y;
        ticking = false;
    }

    window.addEventListener('scroll', () => {
        if (!ticking) { requestAnimationFrame(updateNav); ticking = true; }
    }, { passive: true });

    // ── Active link via scroll position ──────────────────────
    const sections  = Array.from(document.querySelectorAll('section[id]'));
    const navLinks  = document.querySelectorAll('.nav-link');

    function setActiveLink() {
        const scrollMid = window.scrollY + window.innerHeight * 0.35;
        let current = sections[0];
        sections.forEach(s => { if (s.offsetTop <= scrollMid) current = s; });
        navLinks.forEach(l => {
            l.classList.toggle('nav-active', l.getAttribute('href') === '#' + current.id);
        });
    }

    window.addEventListener('scroll', setActiveLink, { passive: true });
    setActiveLink(); // init
}"""

OLD_HAM_BLOCK = """/* ══════════════════════════════════════════════════════════
   10. HAMBURGER / MOBILE MENU
══════════════════════════════════════════════════════════ */
function initHamburger() {
    const hamburger = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobileMenu');
    if (!hamburger || !mobileMenu) return;

    const toggle = () => {
        const open = hamburger.classList.toggle('open');
        mobileMenu.classList.toggle('open', open);
        hamburger.setAttribute('aria-expanded', open);
        document.body.style.overflow = open ? 'hidden' : '';
    };

    hamburger.addEventListener('click', toggle);
    mobileMenu.querySelectorAll('.mobile-link').forEach(link =>
        link.addEventListener('click', () => {
            hamburger.classList.remove('open');
            mobileMenu.classList.remove('open');
            hamburger.setAttribute('aria-expanded', 'false');
            document.body.style.overflow = '';
        })
    );
    document.addEventListener('click', e => {
        if (mobileMenu.classList.contains('open') &&
            !mobileMenu.contains(e.target) &&
            !hamburger.contains(e.target)) {
            hamburger.classList.remove('open');
            mobileMenu.classList.remove('open');
            hamburger.setAttribute('aria-expanded', 'false');
            document.body.style.overflow = '';
        }
    });
}"""

NEW_HAM_BLOCK = """/* ══════════════════════════════════════════════════════════
   10. MOBILE MENU — fullscreen overlay
══════════════════════════════════════════════════════════ */
function initHamburger() {
    const hamburger = document.getElementById('hamburger');
    const overlay   = document.getElementById('mobileMenu');
    const closeBtn  = document.getElementById('mobClose');
    const bg        = document.getElementById('mobOverlayBg');
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

    // Close on link click (smooth scroll takes over)
    overlay.querySelectorAll('.mob-link').forEach(link =>
        link.addEventListener('click', () => setTimeout(closeMenu, 120))
    );

    // Escape key
    document.addEventListener('keydown', e => {
        if (e.key === 'Escape' && overlay.classList.contains('is-open')) closeMenu();
    });
}"""

# Perform replacements
if OLD_NAV_BLOCK in js:
    js = js.replace(OLD_NAV_BLOCK, NEW_NAV_BLOCK)
    print("initNav replaced OK")
else:
    print("WARNING: initNav block not found exactly")

if OLD_HAM_BLOCK in js:
    js = js.replace(OLD_HAM_BLOCK, NEW_HAM_BLOCK)
    print("initHamburger replaced OK")
else:
    print("WARNING: initHamburger block not found exactly")

with open(f, "w", encoding="utf-8") as fh:
    fh.write(js)

print("JS patched successfully")
