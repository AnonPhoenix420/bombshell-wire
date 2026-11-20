with open("phantom-index.html", "r") as f:
    content = f.read()

# The verification card HTML block to insert near the top or bottom of the index
sources_card = """
      <!-- REAL-WORLD VERIFICATION & SOURCE ARCHIVE -->
      <div class="chapter-card" style="border-color: #38bdf8; background: #0d1117;">
        <h3 style="color: #38bdf8;">📂 OPEN-SOURCE INTEL & VERIFICATION ARCHIVE</h3>
        <p class="chapter-desc">Real-world reference documentation, defense department data, and technical whitepapers detailing the actual technologies referenced in this narrative.</p>
        <div style="display: flex; flex-direction: column; gap: 0.75rem; margin-top: 1rem; font-family: monospace; font-size: 0.85rem;">
          <div style="background: #161b22; padding: 10px; border: 1px solid var(--border-color); border-radius: 4px; display: flex; justify-content: space-between; align-items: center; flex-wrap: gap; gap: 0.5rem;">
            <span style="color: var(--text-main);">U.S. Department of Defense: Directed Energy Weapons (DEW) Fact Sheet</span>
            <a href="https://armscontrolcenter.org/fact-sheet-directed-energy-weapons/" target="_blank" class="nav-btn" style="background: #38bdf8; color: #000; font-weight: bold; padding: 4px 10px; text-decoration: none; border-radius: 4px; font-size: 0.75rem;">VERIFY ↗</a>
          </div>
          <div style="background: #161b22; padding: 10px; border: 1px solid var(--border-color); border-radius: 4px; display: flex; justify-content: space-between; align-items: center; flex-wrap: gap; gap: 0.5rem;">
            <span style="color: var(--text-main);">High-Frequency Active Auroral Research Program (HAARP) Ionospheric Facility</span>
            <a href="https://en.wikipedia.org/wiki/High-frequency_Active_Auroral_Research_Program" target="_blank" class="nav-btn" style="background: #38bdf8; color: #000; font-weight: bold; padding: 4px 10px; text-decoration: none; border-radius: 4px; font-size: 0.75rem;">VERIFY ↗</a>
          </div>
          <div style="background: #161b22; padding: 10px; border: 1px solid var(--border-color); border-radius: 4px; display: flex; justify-content: space-between; align-items: center; flex-wrap: gap; gap: 0.5rem;">
            <span style="color: var(--text-main);">Office of Naval Research: Counter-Directed Energy Weapons (CDEW) Overview</span>
            <a href="https://www.onr.navy.mil/organization/departments/code-35/division-353/directed-energy-weapons-cdew" target="_blank" class="nav-btn" style="background: #38bdf8; color: #000; font-weight: bold; padding: 4px 10px; text-decoration: none; border-radius: 4px; font-size: 0.75rem;">VERIFY ↗</a>
          </div>
        </div>
      </div>
"""

# Insert right above the Prologue card
target = "<!-- PROLOGUE -->"
if target in content and "OPEN-SOURCE INTEL & VERIFICATION ARCHIVE" not in content:
    content = content.replace(target, sources_card + "\n\n      " + target)
    with open("phantom-index.html", "w") as f:
        f.write(content)
    print("Successfully added verification source links to phantom-index.html!")
else:
    print("Sources card already present or target marker missing.")
