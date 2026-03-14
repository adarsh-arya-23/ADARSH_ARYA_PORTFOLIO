
import re

f = r"d:\Documents\Z_PORTFOLIO\index.html"
with open(f, "r", encoding="utf-8") as fh:
    html = fh.read()

OLD = '''    <!-- PROJECTS section start -->'''  # will use line-based

# Find the projects section boundaries
start_marker = '<section class="section projects" id="projects"'
end_marker = '</section>\n\n    <!-- '  # next section comment
# Use index-based replacement
s = html.index(start_marker)
# find end: the </section> that closes projects
# We'll find the next section after projects
rest = html[s:]
# Find the closing </section> tag for projects
close = rest.index('</section>') + len('</section>')
e = s + close

NEW_SECTION = '''<section class="section projects" id="projects" aria-label="Projects section">
        <div class="container">
            <div class="section-label" data-reveal>
                <span class="label-line"></span>
                <span>03 &mdash; Projects</span>
            </div>

            <div class="projects-header" data-reveal>
                <h2 class="section-title">
                    Featured <span class="gradient-text">work</span>
                </h2>
                <p class="section-sub">
                    A curated showcase of projects that demonstrate my range,
                    depth, and passion for building great products.
                </p>
            </div>

            <!-- Filter tabs -->
            <div class="proj-filters" data-reveal>
                <button class="proj-filter active" data-pf="all" id="pf-all">All Projects</button>
                <button class="proj-filter" data-pf="web" id="pf-web">Web Apps</button>
                <button class="proj-filter" data-pf="ai" id="pf-ai">AI &amp; ML</button>
                <button class="proj-filter" data-pf="systems" id="pf-systems">Systems</button>
            </div>

            <!-- Project grid -->
            <div class="projects-grid-v2" id="projectsGrid">

                <!-- ── Project 1 (Featured, full-width) ─────────── -->
                <article class="proj-card proj-card--featured" data-pc="web" data-reveal id="proj-habitflow">
                    <div class="proj-img-wrap">
                        <div class="proj-img" style="
                            background: linear-gradient(135deg, #0f0a1e 0%, #1a0f3a 40%, #0d1f40 100%);
                        ">
                            <!-- Browser mockup -->
                            <div class="proj-browser">
                                <div class="proj-browser-bar">
                                    <span class="pb-dot" style="background:#ff5f57"></span>
                                    <span class="pb-dot" style="background:#febc2e"></span>
                                    <span class="pb-dot" style="background:#28c840"></span>
                                    <span class="pb-url">habitflow.app</span>
                                </div>
                                <div class="proj-browser-screen">
                                    <div class="pb-sidebar">
                                        <div class="pb-nav-item active"></div>
                                        <div class="pb-nav-item"></div>
                                        <div class="pb-nav-item"></div>
                                        <div class="pb-nav-item"></div>
                                    </div>
                                    <div class="pb-body">
                                        <div class="pb-stat-row">
                                            <div class="pb-stat" style="--c:#7c3aed">
                                                <div class="pb-stat-num">87%</div>
                                                <div class="pb-stat-lbl">Rate</div>
                                            </div>
                                            <div class="pb-stat" style="--c:#06b6d4">
                                                <div class="pb-stat-num">21</div>
                                                <div class="pb-stat-lbl">Streak</div>
                                            </div>
                                            <div class="pb-stat" style="--c:#10b981">
                                                <div class="pb-stat-num">142</div>
                                                <div class="pb-stat-lbl">Done</div>
                                            </div>
                                        </div>
                                        <div class="pb-chart">
                                            <div class="pb-bar" style="--h:60%;--c:#7c3aed"></div>
                                            <div class="pb-bar" style="--h:80%;--c:#7c3aed"></div>
                                            <div class="pb-bar" style="--h:45%;--c:#7c3aed"></div>
                                            <div class="pb-bar" style="--h:90%;--c:#7c3aed"></div>
                                            <div class="pb-bar" style="--h:70%;--c:#7c3aed"></div>
                                            <div class="pb-bar" style="--h:85%;--c:#7c3aed"></div>
                                            <div class="pb-bar" style="--h:55%;--c:#7c3aed"></div>
                                        </div>
                                        <div class="pb-heatmap">
                                            <div class="pb-heat" style="--op:0.3"></div>
                                            <div class="pb-heat" style="--op:0.6"></div>
                                            <div class="pb-heat" style="--op:1.0"></div>
                                            <div class="pb-heat" style="--op:0.5"></div>
                                            <div class="pb-heat" style="--op:0.8"></div>
                                            <div class="pb-heat" style="--op:0.4"></div>
                                            <div class="pb-heat" style="--op:0.9"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="proj-img-glow" style="--g:#7c3aed"></div>
                        <div class="proj-hover-overlay">
                            <a href="#" class="proj-overlay-btn" id="proj1-preview">
                                <i data-lucide="eye"></i> Preview
                            </a>
                            <a href="#" class="proj-overlay-btn proj-overlay-btn--ghost" id="proj1-src">
                                <i data-lucide="github"></i> Source
                            </a>
                        </div>
                    </div>
                    <div class="proj-info">
                        <div class="proj-meta">
                            <span class="proj-category">Web App</span>
                            <span class="proj-year">2024</span>
                            <span class="proj-status proj-status--live">Live</span>
                        </div>
                        <h3 class="proj-title">HabitFlow <span class="proj-title-accent">Dashboard</span></h3>
                        <p class="proj-desc">
                            A beautiful habit-tracking platform with analytics, streak tracking, activity heatmaps,
                            and AI-powered personalized insights. Built for power users who demand clarity.
                        </p>
                        <div class="proj-tags">
                            <span class="proj-tag">React</span>
                            <span class="proj-tag">TypeScript</span>
                            <span class="proj-tag">Node.js</span>
                            <span class="proj-tag">MongoDB</span>
                            <span class="proj-tag">Chart.js</span>
                        </div>
                        <div class="proj-links">
                            <a href="#" class="proj-link-btn" id="proj1-demo">
                                <i data-lucide="external-link"></i>
                                <span>Live Demo</span>
                            </a>
                            <a href="#" class="proj-link-btn proj-link-btn--ghost" id="proj1-github">
                                <i data-lucide="github"></i>
                                <span>Repository</span>
                            </a>
                        </div>
                    </div>
                </article>

                <!-- ── Project 2 ─────────────────────────────────── -->
                <article class="proj-card" data-pc="systems" data-reveal id="proj-judge">
                    <div class="proj-img-wrap">
                        <div class="proj-img" style="
                            background: linear-gradient(135deg, #020a1a 0%, #0c1d35 100%);
                        ">
                            <div class="proj-code-mockup">
                                <div class="pcm-header">
                                    <span class="pcm-dot" style="background:#ff5f57"></span>
                                    <span class="pcm-dot" style="background:#febc2e"></span>
                                    <span class="pcm-dot" style="background:#28c840"></span>
                                    <span class="pcm-title">solution.cpp</span>
                                </div>
                                <div class="pcm-body">
                                    <div class="pcm-line"><span class="pcm-kw">class</span> <span class="pcm-cls">Solution</span> {</div>
                                    <div class="pcm-line">&nbsp;&nbsp;<span class="pcm-kw">int</span> <span class="pcm-fn">maxProfit</span>(<span class="pcm-kw">vector</span>&lt;<span class="pcm-kw">int</span>&gt;&amp; p) {</div>
                                    <div class="pcm-line">&nbsp;&nbsp;&nbsp;&nbsp;<span class="pcm-kw">int</span> res = <span class="pcm-num">0</span>, low = p[<span class="pcm-num">0</span>];</div>
                                    <div class="pcm-line">&nbsp;&nbsp;&nbsp;&nbsp;<span class="pcm-kw">for</span> (<span class="pcm-kw">auto</span> x : p)</div>
                                    <div class="pcm-line">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;res = max(res, x - low);</div>
                                    <div class="pcm-line">&nbsp;&nbsp;&nbsp;&nbsp;<span class="pcm-kw">return</span> res;</div>
                                    <div class="pcm-line">&nbsp;&nbsp;}</div>
                                    <div class="pcm-line">};</div>
                                </div>
                                <div class="pcm-result pcm-result--pass">
                                    <i data-lucide="check-circle"></i>
                                    All 206 test cases passed &middot; Runtime: 4ms
                                </div>
                            </div>
                        </div>
                        <div class="proj-img-glow" style="--g:#0891b2"></div>
                        <div class="proj-hover-overlay">
                            <a href="#" class="proj-overlay-btn" id="proj2-preview">
                                <i data-lucide="eye"></i> Preview
                            </a>
                            <a href="#" class="proj-overlay-btn proj-overlay-btn--ghost" id="proj2-src">
                                <i data-lucide="github"></i> Source
                            </a>
                        </div>
                    </div>
                    <div class="proj-info">
                        <div class="proj-meta">
                            <span class="proj-category">Systems</span>
                            <span class="proj-year">2024</span>
                            <span class="proj-status proj-status--live">Live</span>
                        </div>
                        <h3 class="proj-title">C++ Online <span class="proj-title-accent">Judge</span></h3>
                        <p class="proj-desc">
                            A competitive programming judge that compiles and evaluates C++ submissions with
                            sandbox execution, real-time feedback, and leaderboards.
                        </p>
                        <div class="proj-tags">
                            <span class="proj-tag">C++</span>
                            <span class="proj-tag">Node.js</span>
                            <span class="proj-tag">Docker</span>
                            <span class="proj-tag">PostgreSQL</span>
                        </div>
                        <div class="proj-links">
                            <a href="#" class="proj-link-btn" id="proj2-demo">
                                <i data-lucide="external-link"></i>
                                <span>Live Demo</span>
                            </a>
                            <a href="#" class="proj-link-btn proj-link-btn--ghost" id="proj2-github">
                                <i data-lucide="github"></i>
                                <span>Repository</span>
                            </a>
                        </div>
                    </div>
                </article>

                <!-- ── Project 3 ─────────────────────────────────── -->
                <article class="proj-card" data-pc="ai" data-reveal id="proj-attendance">
                    <div class="proj-img-wrap">
                        <div class="proj-img" style="
                            background: linear-gradient(135deg, #011a0e 0%, #022c22 100%);
                        ">
                            <div class="proj-ai-mockup">
                                <div class="pam-frame">
                                    <div class="pam-corner pam-corner--tl"></div>
                                    <div class="pam-corner pam-corner--tr"></div>
                                    <div class="pam-corner pam-corner--bl"></div>
                                    <div class="pam-corner pam-corner--br"></div>
                                    <div class="pam-face">
                                        <div class="pam-eye pam-eye--l"></div>
                                        <div class="pam-eye pam-eye--r"></div>
                                    </div>
                                    <div class="pam-scan"></div>
                                </div>
                                <div class="pam-status">
                                    <span class="pam-dot"></span>
                                    <span>Face Detected &mdash; Adarsh Singh</span>
                                </div>
                                <div class="pam-bar">
                                    <div class="pam-progress"></div>
                                </div>
                            </div>
                        </div>
                        <div class="proj-img-glow" style="--g:#059669"></div>
                        <div class="proj-hover-overlay">
                            <a href="#" class="proj-overlay-btn" id="proj3-preview">
                                <i data-lucide="eye"></i> Preview
                            </a>
                            <a href="#" class="proj-overlay-btn proj-overlay-btn--ghost" id="proj3-src">
                                <i data-lucide="github"></i> Source
                            </a>
                        </div>
                    </div>
                    <div class="proj-info">
                        <div class="proj-meta">
                            <span class="proj-category">AI &amp; ML</span>
                            <span class="proj-year">2023</span>
                            <span class="proj-status proj-status--live">Live</span>
                        </div>
                        <h3 class="proj-title">AI Attendance <span class="proj-title-accent">System</span></h3>
                        <p class="proj-desc">
                            Computer vision-powered facial recognition that automates attendance tracking
                            with real-time detection, admin dashboard, and detailed analytics.
                        </p>
                        <div class="proj-tags">
                            <span class="proj-tag">Python</span>
                            <span class="proj-tag">OpenCV</span>
                            <span class="proj-tag">React</span>
                            <span class="proj-tag">SQLite</span>
                        </div>
                        <div class="proj-links">
                            <a href="#" class="proj-link-btn" id="proj3-demo">
                                <i data-lucide="external-link"></i>
                                <span>Live Demo</span>
                            </a>
                            <a href="#" class="proj-link-btn proj-link-btn--ghost" id="proj3-github">
                                <i data-lucide="github"></i>
                                <span>Repository</span>
                            </a>
                        </div>
                    </div>
                </article>

                <!-- ── Project 4 ─────────────────────────────────── -->
                <article class="proj-card" data-pc="web" data-reveal id="proj-saas">
                    <div class="proj-img-wrap">
                        <div class="proj-img" style="
                            background: linear-gradient(135deg, #1a0a2e 0%, #2d1060 100%);
                        ">
                            <div class="proj-saas-mockup">
                                <div class="psm-topbar">
                                    <div class="psm-logo"></div>
                                    <div class="psm-nav">
                                        <div class="psm-nav-item"></div>
                                        <div class="psm-nav-item"></div>
                                        <div class="psm-nav-item"></div>
                                        <div class="psm-btn"></div>
                                    </div>
                                </div>
                                <div class="psm-hero">
                                    <div class="psm-headline"></div>
                                    <div class="psm-sub"></div>
                                    <div class="psm-ctas">
                                        <div class="psm-cta psm-cta--primary"></div>
                                        <div class="psm-cta"></div>
                                    </div>
                                    <div class="psm-preview"></div>
                                </div>
                            </div>
                        </div>
                        <div class="proj-img-glow" style="--g:#6d28d9"></div>
                        <div class="proj-hover-overlay">
                            <a href="#" class="proj-overlay-btn" id="proj4-preview">
                                <i data-lucide="eye"></i> Preview
                            </a>
                            <a href="#" class="proj-overlay-btn proj-overlay-btn--ghost" id="proj4-src">
                                <i data-lucide="github"></i> Source
                            </a>
                        </div>
                    </div>
                    <div class="proj-info">
                        <div class="proj-meta">
                            <span class="proj-category">Web App</span>
                            <span class="proj-year">2024</span>
                            <span class="proj-status proj-status--build">Building</span>
                        </div>
                        <h3 class="proj-title">DevLaunch <span class="proj-title-accent">SaaS</span></h3>
                        <p class="proj-desc">
                            A full-featured SaaS boilerplate with auth, billing, teams, and a
                            polished landing page. Ships with Stripe, shadcn/ui, and full TypeScript.
                        </p>
                        <div class="proj-tags">
                            <span class="proj-tag">Next.js</span>
                            <span class="proj-tag">TypeScript</span>
                            <span class="proj-tag">Stripe</span>
                            <span class="proj-tag">Prisma</span>
                        </div>
                        <div class="proj-links">
                            <a href="#" class="proj-link-btn" id="proj4-demo">
                                <i data-lucide="external-link"></i>
                                <span>Live Demo</span>
                            </a>
                            <a href="#" class="proj-link-btn proj-link-btn--ghost" id="proj4-github">
                                <i data-lucide="github"></i>
                                <span>Repository</span>
                            </a>
                        </div>
                    </div>
                </article>

            </div><!-- /projects-grid-v2 -->

            <!-- Footer CTA -->
            <div class="projects-footer" data-reveal>
                <a href="https://github.com" class="btn-ghost" id="view-all-projects"
                    aria-label="View all projects on GitHub" target="_blank" rel="noopener noreferrer">
                    <i data-lucide="github"></i>
                    <span>View All on GitHub</span>
                    <i data-lucide="arrow-right"></i>
                </a>
            </div>
        </div>
    </section>'''

new_html = html[:s] + NEW_SECTION + html[e:]

with open(f, "w", encoding="utf-8") as fh:
    fh.write(new_html)

print(f"Done — new length: {len(new_html)} chars")
