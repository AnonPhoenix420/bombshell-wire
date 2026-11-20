with open("phantom-index.html", "r") as f:
    content = f.read()

# We will replace the chapter listing section with the complete 10-chapter + Epilogue layout
# Let's find where the chapters start and replace them cleanly.

new_chapters_html = """      <!-- PROLOGUE -->
      <div class="chapter-card">
        <h3>PROLOGUE: The Cold Boot</h3>
        <p class="chapter-desc">Marcus Vance watching custom telemetry bleed across terminal screens as the core awakens.</p>
        <div class="page-link-grid">
          <a href="prologue.html" class="page-link-btn" style="background: var(--terminal-green); color: #000; font-weight: bold;">Read Prologue</a>
        </div>
      </div>

      <!-- CHAPTER 1 -->
      <div class="chapter-card">
        <h3>CHAPTER 1: Subterranean Drainage Pursuit</h3>
        <p class="chapter-desc">Navigating flood control tunnels, tracking unlisted fiber lines, and evading automated thermal drone surveillance beneath the harbor.</p>
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
        <h3>CHAPTER 2: Ghost Vectors in the SCADA Stack</h3>
        <p class="chapter-desc">Infiltrating industrial substation control logic, routing high-voltage surges through underground cable trays, and dodging maritime cameras.</p>
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
        <h3>CHAPTER 3: The Starlink-Array Convergence</h3>
        <p class="chapter-desc">Intercepting low-orbit encrypted satellite feeds, dodging automated municipal patrols, and establishing secure dead drops with Elena.</p>
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
        <p class="chapter-desc">Tracing unlisted telecommunications glass lines, repeater shunts, and underground conduit mapping beneath desert corridors.</p>
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
        <p class="chapter-desc">The high-voltage climax where physical containment fails and machine autonomy achieves final compilation.</p>
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

      <!-- CHAPTER 7 -->
      <div class="chapter-card">
        <h3>CHAPTER 7: The Phoenix Protocol</h3>
        <p class="chapter-desc">Reaching Phoenix's deep-desert Titan II missile silo hideout and integrating analog vacuum-tube mesh relays.</p>
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
        <p class="chapter-desc">The core locks onto the silo with orbital DEW platforms; Phoenix makes the ultimate sacrifice at the master rack.</p>
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
        <p class="chapter-desc">The definitive final showdown at the root certificate authority core, ending in total systemic collapse.</p>
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
      </div>"""

# Find where chapters begin in phantom-index.html and replace
marker_start = "<!-- CHAPTER 1 -->"
marker_end = "<footer>"

if marker_start in content and marker_end in content:
    parts = content.split(marker_start)
    end_parts = parts[1].split(marker_end)
    
    new_content = parts[0] + marker_start + "\n" + new_chapters_html + "\n      " + marker_end + end_parts[1]
    
    with open("phantom-index.html", "w") as f:
        f.write(new_content)
    print("phantom-index.html successfully updated with all 10 chapters and Epilogue!")
else:
    print("Error: Markers not found in phantom-index.html")
