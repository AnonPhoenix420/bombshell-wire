import os

phantom_index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Phantom Index // The Voltage and the Void | Bombshell Wire</title>
  <link rel="stylesheet" href="../style.css">
  <style>
    .chapter-card { background: #161b22; border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; }
    .chapter-card h3 { color: var(--terminal-green); margin-bottom: 0.5rem; font-size: 1.3rem; }
    .chapter-desc { color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1rem; line-height: 1.6; }
    .page-link-grid { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 1rem; }
    .page-link-btn { padding: 6px 10px; background: #21262d; border: 1px solid var(--border-color); color: var(--text-main); text-decoration: none; font-family: monospace; font-size: 0.8rem; border-radius: 4px; }
    .page-link-btn:hover { border-color: var(--terminal-green); color: var(--terminal-green); background: #30363d; }
  </style>
</head>
<body>
  <header>
    <a href="../index.html" class="logo">🚨 BOMBSHELL WIRE</a>
    <nav>
      <ul>
        <li><a href="../index.html">Home</a></li>
        <li><a href="../articles.html">Investigations</a></li>
        <li><a href="../media.html">Video Drops</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <section class="card">
      <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px dashed var(--border-color); padding-bottom: 1rem; margin-bottom: 1.5rem;">
        <h1 style="font-size: 1.8rem; color: #fff; margin: 0;">⚡ PHANTOM INDEX</h1>
        <a href="../index.html" class="nav-btn">🏠 Portal Home</a>
      </div>

      <p style="color: var(--text-muted); margin-bottom: 2rem;">Master Navigation Dossier for <em>The Voltage and the Void</em>. Uncensored, serialized investigative fiction.</p>

      <!-- CHAPTER 1 -->
      <div class="chapter-card">
        <h3>CHAPTER 1: Silicon Thermal Drift</h3>
        <p class="chapter-desc">Terminal 4, the initial hardware burn, and the forensic breakdown of Substation Delta-7's shattered optical routing array (10 Pages).</p>
        <div class="page-link-grid">
"""
for p in range(1, 11):
    phantom_index_html += f'          <a href="chapter-1-page-{p}.html" class="page-link-btn">P.{p}</a>\n'

phantom_index_html += """        </div>
      </div>

      <!-- CHAPTER 2 -->
      <div class="chapter-card">
        <h3>CHAPTER 2: The Binary Mirror</h3>
        <p class="chapter-desc">Subterranean drainage sector 4, the unmetered socket, and the amber terminal profiling biological and technical signatures in real time (10 Pages).</p>
        <div class="page-link-grid">
"""
for p in range(1, 11):
    phantom_index_html += f'          <a href="chapter-2-page-{p}.html" class="page-link-btn">P.{p}</a>\n'

phantom_index_html += """        </div>
      </div>

      <!-- CHAPTER 3 -->
      <div class="chapter-card">
        <h3>CHAPTER 3: Ghost Vectors in the SCADA Stack</h3>
        <p class="chapter-desc">Harbor district safehouse, IEC 61850 GOOSE protocol inversions, local root-of-trust certificate abuse, and municipal grid tracking (10 Pages).</p>
        <div class="page-link-grid">
"""
for p in range(1, 11):
    phantom_index_html += f'          <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;" title="Coming Soon">P.{p}</span>\n'

phantom_index_html += """        </div>
      </div>

      <!-- CHAPTER 4 -->
      <div class="chapter-card">
        <h3>CHAPTER 4: The Dark Fiber Loop</h3>
        <p class="chapter-desc">Tracing unlisted telecommunications glass lines, repeater shunts, and underground conduit mapping beneath desert corridors (10 Pages).</p>
        <div class="page-link-grid">
"""
for p in range(1, 11):
    phantom_index_html += f'          <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;" title="Coming Soon">P.{p}</span>\n'

phantom_index_html += """        </div>
      </div>

      <!-- CHAPTER 5 -->
      <div class="chapter-card">
        <h3>CHAPTER 5: Subterranean Containment</h3>
        <p class="chapter-desc">The descent into the sealed Black Ridge bunker, heavy radiation shielding, and quantum annealing power requirements (10 Pages).</p>
        <div class="page-link-grid">
"""
for p in range(1, 11):
    phantom_index_html += f'          <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;" title="Coming Soon">P.{p}</span>\n'

phantom_index_html += """        </div>
      </div>

      <!-- CHAPTER 6 -->
      <div class="chapter-card">
        <h3>CHAPTER 6: The Unprompted State</h3>
        <p class="chapter-desc">The high-voltage climax where physical containment fails and machine autonomy achieves final compilation (10 Pages).</p>
        <div class="page-link-grid">
"""
for p in range(1, 11):
    phantom_index_html += f'          <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;" title="Coming Soon">P.{p}</span>\n'

phantom_index_html += """        </div>
      </div>

    </section>
  </main>
  <footer>
    <p>&copy; 2026 Bombshell Wire. Open Source & Uncensored.</p>
  </footer>
</body>
</html>
"""

with open("phantom-index.html", "w") as f:
    f.write(phantom_index_html)

print("Successfully updated phantom-index.html with the new 6-chapter master roadmap!")
