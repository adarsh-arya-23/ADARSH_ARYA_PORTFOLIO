
f = r"d:\Documents\Z_PORTFOLIO\index.html"
with open(f, "r", encoding="utf-8") as fh:
    html = fh.read()

OLD_NAV = '''    <!-- NAV -->
    <nav class="nav" id="nav" role="navigation" aria-label="Main navigation">
        <div class="nav-inner">
            <a href="#home" class="nav-logo" aria-label="Home">
                <span class="logo-text">AS</span>
                <span class="logo-dot"></span>
            </a>
            <ul class="nav-links" role="list">
                <li><a href="#about" class="nav-link">About</a></li>
                <li><a href="#stack" class="nav-link">Stack</a></li>
                <li><a href="#projects" class="nav-link">Projects</a></li>
                <li><a href="#experience" class="nav-link">Experience</a></li>
                <li><a href="#contact" class="nav-link">Contact</a></li>
            </ul>
            <a href="#contact" class="nav-cta" id="nav-cta-btn">Let\'s Talk &#8594;</a>
            <button class="hamburger" id="hamburger" aria-label="Toggle menu" aria-expanded="false">
                <span></span><span></span><span></span>
            </button>
        </div>
    </nav>

    <!-- Mobile Menu -->
    <div class="mobile-menu" id="mobileMenu" role="dialog" aria-label="Mobile navigation">
        <ul role="list">
            <li><a href="#about" class="mobile-link">About</a></li>
            <li><a href="#stack" class="mobile-link">Stack</a></li>
            <li><a href="#projects" class="mobile-link">Projects</a></li>
            <li><a href="#experience" class="mobile-link">Experience</a></li>
            <li><a href="#contact" class="mobile-link">Contact</a></li>
        </ul>
    </div>'''

# Find and replace
import re

# Use a flexible match since comments may have encoding artifacts
start = html.find('<nav class="nav" id="nav"')
# find the end of the mobile-menu div
end_marker = '</div>\n\n    <!-- HERO'
end = html.find(end_marker)
if end == -1:
    end_marker = '</div>\r\n\r\n    <!-- HERO'
    end = html.find(end_marker)
if end == -1:
    # fallback approach
    end = html.find('<!-- HERO')
    # walk back to find the </div> before it
    sub = html[:end]
    close_tag = sub.rfind('</div>')
    end = close_tag + len('</div>')
else:
    end = end + len('</div>')

print(f"NAV start: {start}, end: {end}")
print(f"Replacing: {repr(html[start:start+60])}")

NEW_NAV = '''<nav class="nav" id="nav" role="navigation" aria-label="Main navigation">
        <div class="nav-inner">

            <!-- Logo -->
            <a href="#home" class="nav-logo" aria-label="Go to top">
                <span class="logo-mark">
                    <span class="logo-text">AS</span>
                    <span class="logo-dot"></span>
                </span>
                <span class="logo-name">Adarsh Singh</span>
            </a>

            <!-- Desktop Links -->
            <ul class="nav-links" role="list">
                <li><a href="#about"      class="nav-link" data-nav="about">About</a></li>
                <li><a href="#stack"      class="nav-link" data-nav="stack">Stack</a></li>
                <li><a href="#projects"   class="nav-link" data-nav="projects">Projects</a></li>
                <li><a href="#experience" class="nav-link" data-nav="experience">Experience</a></li>
                <li><a href="#contact"    class="nav-link" data-nav="contact">Contact</a></li>
            </ul>

            <!-- CTA -->
            <a href="#contact" class="nav-cta" id="nav-cta-btn" aria-label="Contact me">
                <span>Let's Talk</span>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>

            <!-- Hamburger -->
            <button class="hamburger" id="hamburger" aria-label="Toggle menu" aria-expanded="false" aria-controls="mobileMenu">
                <span class="ham-line ham-line--top"></span>
                <span class="ham-line ham-line--mid"></span>
                <span class="ham-line ham-line--bot"></span>
            </button>

        </div>
    </nav>

    <!-- ── Full-screen Mobile Overlay ─── -->
    <div class="mobile-overlay" id="mobileMenu" role="dialog" aria-label="Mobile navigation" aria-modal="true" aria-hidden="true">
        <div class="mob-overlay-bg" id="mobOverlayBg"></div>
        <div class="mob-content">
            <div class="mob-header">
                <a href="#home" class="nav-logo mob-logo" aria-label="Home">
                    <span class="logo-text">AS</span>
                    <span class="logo-dot"></span>
                </a>
                <button class="mob-close" id="mobClose" aria-label="Close menu">&times;</button>
            </div>
            <nav class="mob-nav" aria-label="Mobile navigation links">
                <ul role="list">
                    <li><a href="#about"      class="mob-link" data-mob="0">About</a></li>
                    <li><a href="#stack"      class="mob-link" data-mob="1">Stack</a></li>
                    <li><a href="#projects"   class="mob-link" data-mob="2">Projects</a></li>
                    <li><a href="#experience" class="mob-link" data-mob="3">Experience</a></li>
                    <li><a href="#contact"    class="mob-link" data-mob="4">Contact</a></li>
                </ul>
            </nav>
            <div class="mob-footer">
                <a href="#contact" class="btn-primary mob-cta" id="mob-cta">
                    <span>Let's Talk</span>
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </a>
                <p class="mob-tagline">Open to work &middot; Remote/Hybrid</p>
            </div>
        </div>
    </div>'''

new_html = html[:start] + NEW_NAV + '\n\n    ' + html[end:]
with open(f, "w", encoding="utf-8") as fh:
    fh.write(new_html)
print(f"Done. New length: {len(new_html)}")
