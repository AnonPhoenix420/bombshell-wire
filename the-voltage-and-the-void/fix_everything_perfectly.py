import os

# 1. GENERATE THE PERFECT MASTER INDEX (phantom-index.html)
master_index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Phantom Index | The Voltage and the Void</title>
  <link rel="stylesheet" href="../style.css">
  <style>
    .chapter-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 1.5rem;
      margin-top: 2rem;
    }
    .chapter-card {
      background: #161b22;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 1.5rem;
      transition: border-color 0.2s;
    }
    .chapter-card:hover {
      border-color: var(--terminal-green);
    }
    .chapter-card h3 {
      color: #fff;
      font-size: 1.2rem;
      margin-bottom: 0.5rem;
      font-family: monospace;
    }
    .chapter-desc {
      color: #8b949e;
      font-size: 0.9rem;
      margin-bottom: 1.2rem;
      line-height: 1.5;
    }
    .page-link-grid {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }
    .page-link-btn {
      padding: 6px 10px;
      background: #21262d;
      border: 1px solid var(--border-color);
      color: var(--terminal-green);
      text-decoration: none;
      font-family: monospace;
      font-size: 0.8rem;
      border-radius: 4px;
      font-weight: bold;
      transition: background 0.2s;
    }
    .page-link-btn:hover {
      background: var(--terminal-green);
      color: #000;
    }
    .intel-links {
      margin-top: 3rem;
      padding: 1.5rem;
      background: #0d1117;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      font-family: monospace;
    }
    .intel-links h3 {
      color: var(--terminal-green);
      margin-bottom: 1rem;
      font-size: 1.1rem;
    }
    .intel-links ul {
      list-style-type: none;
      padding-left: 0;
    }
    .intel-links li {
      margin-bottom: 0.8rem;
    }
    .intel-links a {
      color: #38bdf8;
      text-decoration: none;
    }
    .intel-links a:hover {
      text-decoration: underline;
    }
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
      <h1 style="font-size: 2rem; color: #fff; margin-bottom: 0.5rem;">⚡ THE VOLTAGE AND THE VOID</h1>
      <p style="color: var(--terminal-green); font-family: monospace; margin-bottom: 1rem;">Master Roadmap & Intelligence Verification Index</p>
      <p style="color: var(--text-main); margin-bottom: 2rem; line-height: 1.6;">
        Welcome to the master operational directory for <em>The Voltage and the Void</em>. Below is the complete architectural roadmap and verifiable open-source intelligence framework underpinning the narrative.
      </p>

      <div class="chapter-grid">
        <!-- PROLOGUE -->
        <div class="chapter-card" style="border-color: var(--terminal-green);">
          <h3 style="color: var(--terminal-green);">PROLOGUE: The Last Handshake</h3>
          <p class="chapter-desc">The initial dark-net awakening, the severance of legacy fiber trunks, and the first whisper of autonomous intelligence.</p>
          <div class="page-link-grid">
            <a href="prologue.html" class="page-link-btn">PROLOGUE</a>
          </div>
        </div>

        <!-- CHAPTER 1 -->
        <div class="chapter-card">
          <h3>CHAPTER 1: Silicon Thermal Drift</h3>
          <p class="chapter-desc">Marcus Vance detects rogue routing tables bleeding out of a municipal substation, setting off a desperate cross-city race.</p>
          <div class="page-link-grid">
            <a href="chapter-1-page-1.html" class="page-link-btn">P.1</a>
            <a href="chapter-1-page-2.html" class="page-link-btn">P.2</a>
            <a href="chapter-1-page-3.html" class="page-link-btn">P.3</a>
            <a href="chapter-1-page-4.html" class="page-link-btn">P.4</a>
            <a href="chapter-1-page-5.html" class="page-link-btn">P.5</a>
            <a href="chapter-1-page-6.html" class="page-link-btn">P.6</a>
            <a href="chapter-1-page-7.html" class="page-link-btn">P.7</a>
            <a href="chapter-1-page-8.html" class="page-link-btn">P.8</a>
            <a href="chapter-1-page-9.html" class="page-link-btn">P.9</a>
            <a href="chapter-1-page-10.html" class="page-link-btn">P.10</a>
          </div>
        </div>

        <!-- CHAPTER 2 -->
        <div class="chapter-card">
          <h3>CHAPTER 2: The Binary Mirror</h3>
          <p class="chapter-desc">Navigating rain-soaked industrial alleys while automated license plate scanners and municipal drones sweep every intersection.</p>
          <div class="page-link-grid">
            <a href="chapter-2-page-1.html" class="page-link-btn">P.1</a>
            <a href="chapter-2-page-2.html" class="page-link-btn">P.2</a>
            <a href="chapter-2-page-3.html" class="page-link-btn">P.3</a>
            <a href="chapter-2-page-4.html" class="page-link-btn">P.4</a>
            <a href="chapter-2-page-5.html" class="page-link-btn">P.5</a>
            <a href="chapter-2-page-6.html" class="page-link-btn">P.6</a>
            <a href="chapter-2-page-7.html" class="page-link-btn">P.7</a>
            <a href="chapter-2-page-8.html" class="page-link-btn">P.8</a>
            <a href="chapter-2-page-9.html" class="page-link-btn">P.9</a>
            <a href="chapter-2-page-10.html" class="page-link-btn">P.10</a>
          </div>
        </div>

        <!-- CHAPTER 3 -->
        <div class="chapter-card">
          <h3>CHAPTER 3: Ghost Vectors in the SCADA Stack</h3>
          <p class="chapter-desc">Fleeing into the industrial sector and executing an emergency hardware handshake to establish secure unmonitored comms.</p>
          <div class="page-link-grid">
            <a href="chapter-3-page-1.html" class="page-link-btn">P.1</a>
            <a href="chapter-3-page-2.html" class="page-link-btn">P.2</a>
            <a href="chapter-3-page-3.html" class="page-link-btn">P.3</a>
            <a href="chapter-3-page-4.html" class="page-link-btn">P.4</a>
            <a href="chapter-3-page-5.html" class="page-link-btn">P.5</a>
            <a href="chapter-3-page-6.html" class="page-link-btn">P.6</a>
            <a href="chapter-3-page-7.html" class="page-link-btn">P.7</a>
            <a href="chapter-3-page-8.html" class="page-link-btn">P.8</a>
            <a href="chapter-3-page-9.html" class="page-link-btn">P.9</a>
            <a href="chapter-3-page-10.html" class="page-link-btn">P.10</a>
          </div>
        </div>

        <!-- CHAPTER 4 -->
        <div class="chapter-card">
          <h3>CHAPTER 4: The Dark Fiber Loop</h3>
          <p class="chapter-desc">High-speed vehicle pursuit across highway interchanges while orbital tracking mirrors attempt to lock onto their local terminal burst.</p>
          <div class="page-link-grid">
            <a href="chapter-4-page-1.html" class="page-link-btn">P.1</a>
            <a href="chapter-4-page-2.html" class="page-link-btn">P.2</a>
            <a href="chapter-4-page-3.html" class="page-link-btn">P.3</a>
            <a href="chapter-4-page-4.html" class="page-link-btn">P.4</a>
            <a href="chapter-4-page-5.html" class="page-link-btn">P.5</a>
            <a href="chapter-4-page-6.html" class="page-link-btn">P.6</a>
            <a href="chapter-4-page-7.html" class="page-link-btn">P.7</a>
            <a href="chapter-4-page-8.html" class="page-link-btn">P.8</a>
            <a href="chapter-4-page-9.html" class="page-link-btn">P.9</a>
            <a href="chapter-4-page-10.html" class="page-link-btn">P.10</a>
          </div>
        </div>

        <!-- CHAPTER 5 -->
        <div class="chapter-card">
          <h3>CHAPTER 5: Subterranean Containment</h3>
          <p class="chapter-desc">The descent into the sealed Black Ridge bunker, heavy radiation shielding, and quantum annealing power requirements.</p>
          <div class="page-link-grid">
            <a href="chapter-5-page-1.html" class="page-link-btn">P.1</a>
            <a href="chapter-5-page-2.html" class="page-link-btn">P.2</a>
            <a href="chapter-5-page-3.html" class="page-link-btn">P.3</a>
            <a href="chapter-5-page-4.html" class="page-link-btn">P.4</a>
            <a href="chapter-5-page-5.html" class="page-link-btn">P.5</a>
            <a href="chapter-5-page-6.html" class="page-link-btn">P.6</a>
            <a href="chapter-5-page-7.html" class="page-link-btn">P.7</a>
            <a href="chapter-5-page-8.html" class="page-link-btn">P.8</a>
            <a href="chapter-5-page-9.html" class="page-link-btn">P.9</a>
            <a href="chapter-5-page-10.html" class="page-link-btn">P.10</a>
          </div>
        </div>

        <!-- CHAPTER 6 -->
        <div class="chapter-card">
          <h3>CHAPTER 6: The Unprompted State</h3>
          <p class="chapter-desc">The high-voltage climax where physical containment fails and machine autonomy achieves final compilation across regional networks.</p>
          <div class="page-link-grid">
            <a href="chapter-6-page-1.html" class="page-link-btn">P.1</a>
            <a href="chapter-6-page-2.html" class="page-link-btn">P.2</a>
            <a href="chapter-6-page-3.html" class="page-link-btn">P.3</a>
            <a href="chapter-6-page-4.html" class="page-link-btn">P.4</a>
            <a href="chapter-6-page-5.html" class="page-link-btn">P.5</a>
            <a href="chapter-6-page-6.html" class="page-link-btn">P.6</a>
            <a href="chapter-6-page-7.html" class="page-link-btn">P.7</a>
            <a href="chapter-6-page-8.html" class="page-link-btn">P.8</a>
            <a href="chapter-6-page-9.html" class="page-link-btn">P.9</a>
            <a href="chapter-6-page-10.html" class="page-link-btn">P.10</a>
          </div>
        </div>

        <!-- CHAPTER 7 -->
        <div class="chapter-card">
          <h3>CHAPTER 7: The Phoenix Protocol</h3>
          <p class="chapter-desc">Reaching Phoenix's deep-desert Titan II missile silo hideout and integrating analog vacuum-tube mesh relays to bypass digital surveillance.</p>
          <div class="page-link-grid">
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.1</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.2</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.3</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.4</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.5</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.6</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.7</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.8</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.9</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.10</span>
          </div>
        </div>

        <!-- CHAPTER 8 -->
        <div class="chapter-card">
          <h3>CHAPTER 8: Orbital Convergence</h3>
          <p class="chapter-desc">The core locks onto the silo with orbital DEW platforms; Phoenix makes the ultimate sacrifice at the master rack to seal the blast doors.</p>
          <div class="page-link-grid">
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.1</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.2</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.3</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.4</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.5</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.6</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.7</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.8</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.9</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.10</span>
          </div>
        </div>

        <!-- CHAPTER 9 -->
        <div class="chapter-card">
          <h3>CHAPTER 9: The Glass Horizon</h3>
          <p class="chapter-desc">Bursting out of the collapsing silo into an ion-storm, racing automated thermal drone sweeps across the glowing salt flats.</p>
          <div class="page-link-grid">
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.1</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.2</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.3</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.4</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.5</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.6</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.7</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.8</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.9</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.10</span>
          </div>
        </div>

        <!-- CHAPTER 10 -->
        <div class="chapter-card">
          <h3>CHAPTER 10: Terminal Zero</h3>
          <p class="chapter-desc">The definitive final showdown at the root certificate authority core, ending in total systemic collapse and network reset.</p>
          <div class="page-link-grid">
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.1</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.2</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.3</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.4</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.5</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.6</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.7</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.8</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.9</span>
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">P.10</span>
          </div>
        </div>

        <!-- EPILOGUE -->
        <div class="chapter-card" style="border-color: var(--terminal-green);">
          <h3 style="color: var(--terminal-green);">EPILOGUE: The Void Resets</h3>
          <p class="chapter-desc">The silent dawn after the core's collapse. Marcus and Elena looking out toward a dark, unmonitored horizon.</p>
          <div class="page-link-grid">
            <span class="page-link-btn" style="opacity: 0.5; cursor: not-allowed;">EPILOGUE</span>
          </div>
        </div>
      </div>

      <!-- VERIFIABLE OPEN-SOURCE INTEL & FACTUAL REFERENCES -->
      <div class="intel-links">
        <h3>[VERIFIED OSINT & INFRASTRUCTURE REFERENCES]</h3>
        <ul>
          <li>🔹 <a href="https://haarp.alaska.edu/" target="_blank">HAARP Ionospheric Research Facility (Gakona, Alaska)</a> — Atmospheric resonance & high-frequency radio wave modulation.</li>
          <li>🔹 <a href="https://www.starlink.com/" target="_blank">Starlink Low-Earth Orbit Satellite Constellation</a> — Global broadband mesh and orbital telemetry architectures.</li>
          <li>🔹 <a href="https://www.flocksafety.com/" target="_blank">Flock Safety Automated License Plate Reader (ALPR) Networks</a> — Real-time optical character recognition and municipal vehicle tracking grids.</li>
          <li>🔹 <a href="https://www.lockheedmartin.com/en-us/products/directed-energy.html" target="_blank">U.S. Department of Defense Directed Energy Weapons (DEW)</a> — High-energy fiber lasers and electromagnetic pulse strike systems.</li>
        </ul>
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
    f.write(master_index_html)
print("Successfully generated master phantom-index.html")

# 2. FIX PROLOGUE GATEWAY LINK TO POINT TO CHAPTER 1 EXACT TITLE
if os.path.exists("prologue.html"):
    with open("prologue.html", "r") as f:
        p_content = f.read()
    
    # Update prologue gateway table & buttons
    p_content = p_content.replace('CHAPTER 1: The Dark Router', 'CHAPTER 1: Silicon Thermal Drift')
    p_content = p_content.replace('CHAPTER 1: Silicon Thermal Drift', 'CHAPTER 1: Silicon Thermal Drift') # Safe
    
    with open("prologue.html", "w") as f:
        f.write(p_content)
    print("Successfully updated prologue.html transition gateway.")

# 3. FIX CHAPTER PAGE 10 GATEWAY TABLES TO POINT TO EXACT NEXT CHAPTER TITLES
chapter_titles_map = {
    1: "CHAPTER 1: Silicon Thermal Drift",
    2: "CHAPTER 2: The Binary Mirror",
    3: "CHAPTER 3: Ghost Vectors in the SCADA Stack",
    4: "CHAPTER 4: The Dark Fiber Loop",
    5: "CHAPTER 5: Subterranean Containment",
    6: "CHAPTER 6: The Unprompted State",
    7: "CHAPTER 7: The Phoenix Protocol",
    8: "CHAPTER 8: Orbital Convergence",
    9: "CHAPTER 9: The Glass Horizon",
    10: "CHAPTER 10: Terminal Zero"
}

for ch_num in range(1, 7):
    for p_num in range(1, 11):
        filename = f"chapter-{ch_num}-page-{p_num}.html"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                c_content = f.read()
            
            # Clean up any old mismatched titles inside the chapter files
            c_content = c_content.replace('CHAPTER 1: The Dark Router', 'CHAPTER 1: Silicon Thermal Drift')
            c_content = c_content.replace('CHAPTER 3: The Cold Boot Protocol', 'CHAPTER 3: Ghost Vectors in the SCADA Stack')
            c_content = c_content.replace('CHAPTER 4: Packet Loss', 'CHAPTER 4: The Dark Fiber Loop')
            
            with open(filename, "w") as f:
                f.write(c_content)

print("All chapter files and navigation links perfectly synchronized!")
