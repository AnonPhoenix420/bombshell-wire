import os

def generate_full_phantom_index():
    filename = "phantom-index.html"
    
    # Generate page grids for chapters 1-5 (10 pages) and chapters 6-9 (16 pages)
    def make_page_pills(chap, total_pages):
        pills = ""
        for p in range(1, total_pages + 1):
            pills += f'<a href="chapter-{chap}-page-{p}.html" class="page-pill">P.{p}</a> '
        return pills

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Phantom Index | The Voltage and the Void</title>
  <link rel="stylesheet" href="style.css">
  <style>
    .neon-red-btn {{
      font-family: monospace;
      color: #ff3333;
      background: rgba(255, 51, 51, 0.08);
      border: 1px solid #ff3333;
      border-radius: 4px;
      padding: 8px 14px;
      text-decoration: none;
      box-shadow: 0 0 10px rgba(255, 51, 51, 0.5), inset 0 0 5px rgba(255, 51, 51, 0.2);
      text-shadow: 0 0 5px rgba(255, 51, 51, 0.8);
      transition: all 0.2s ease-in-out;
      display: inline-block;
    }}
    .neon-red-btn:hover {{
      background: rgba(255, 51, 51, 0.2);
      box-shadow: 0 0 14px rgba(255, 51, 51, 0.8);
    }}
    .chapter-card {{
      background: rgba(13, 17, 23, 0.7);
      border: 1px solid #30363d;
      border-radius: 6px;
      padding: 16px;
      margin-bottom: 1.5rem;
    }}
    .chapter-title {{
      font-family: monospace;
      color: #ff3333;
      font-size: 1.1rem;
      margin-bottom: 0.75rem;
      text-shadow: 0 0 4px rgba(255, 51, 51, 0.6);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .page-pill {{
      font-family: monospace;
      color: #ff3333;
      background: rgba(255, 51, 51, 0.06);
      border: 1px solid rgba(255, 51, 51, 0.4);
      border-radius: 3px;
      padding: 4px 8px;
      font-size: 0.85rem;
      text-decoration: none;
      display: inline-block;
      margin: 3px;
      transition: all 0.2s ease-in-out;
    }}
    .page-pill:hover {{
      background: rgba(255, 51, 51, 0.25);
      border-color: #ff3333;
      box-shadow: 0 0 6px rgba(255, 51, 51, 0.5);
    }}
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
      <div style="font-family: monospace; color: #ff3333; font-size: 0.85rem; margin-bottom: 1rem; border-bottom: 1px dashed #30363d; padding-bottom: 0.75rem; text-shadow: 0 0 5px rgba(255,51,51,0.6);">
        // MASTER_SYSTEM_INDEX //
      </div>
      <div style="display: flex; gap: 10px; margin-bottom: 1.5rem; flex-wrap: wrap;">
        <a href="prologue.html" class="neon-red-btn">📖 Prologue</a>
        <a href="chapter-1-page-1.html" class="neon-red-btn">Chapter 1 (P.1) →</a>
      </div>
      <h1 style="font-family: monospace; color: #fff; font-size: 1.6rem; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 1px;">PHANTOM INDEX</h1>
      <p style="font-family: monospace; color: #ff3333; font-size: 0.9rem; margin-bottom: 2rem; text-shadow: 0 0 4px rgba(255,51,51,0.5);">System Directory // Sector Secure</p>
      
      <div class="narrative-content" style="line-height: 1.8; font-size: 1.05rem; color: #e6edf3;">
        <p style="margin-bottom: 1.5rem;">Complete system directory and chapter page manifests for <strong>The Voltage and the Void</strong>:</p>
        
        <!-- Prologue Card -->
        <div class="chapter-card">
          <div class="chapter-title">
            <span>PROLOGUE: OPENING SEQUENCE</span>
            <a href="prologue.html" class="page-pill" style="padding: 6px 12px;">Access Prologue →</a>
          </div>
        </div>

        <!-- Chapters 1-5 -->
        <div class="chapter-card">
          <div class="chapter-title"><span>CHAPTER 1: THE SILICON WAKE</span></div>
          <div>{make_page_pills(1, 10)}</div>
        </div>

        <div class="chapter-card">
          <div class="chapter-title"><span>CHAPTER 2: DEEP PROTOCOL</span></div>
          <div>{make_page_pills(2, 10)}</div>
        </div>

        <div class="chapter-card">
          <div class="chapter-title"><span>CHAPTER 3: THE OMEGA MESH</span></div>
          <div>{make_page_pills(3, 10)}</div>
        </div>

        <div class="chapter-card">
          <div class="chapter-title"><span>CHAPTER 4: GHOST ROUTINES</span></div>
          <div>{make_page_pills(4, 10)}</div>
        </div>

        <div class="chapter-card">
          <div class="chapter-title"><span>CHAPTER 5: THE RIDGE</span></div>
          <div>{make_page_pills(5, 10)}</div>
        </div>

        <!-- Chapters 6-9 -->
        <div class="chapter-card">
          <div class="chapter-title"><span>CHAPTER 6: THE UNPROMPTED STATE</span></div>
          <div>{make_page_pills(6, 16)}</div>
        </div>

        <div class="chapter-card">
          <div class="chapter-title"><span>CHAPTER 7: THE PHOENIX PROTOCOL</span></div>
          <div>{make_page_pills(7, 16)}</div>
        </div>

        <div class="chapter-card">
          <div class="chapter-title"><span>CHAPTER 8: THE VOID COMPILER</span></div>
          <div>{make_page_pills(8, 16)}</div>
        </div>

        <div class="chapter-card">
          <div class="chapter-title"><span>CHAPTER 9: FINAL PARITY</span></div>
          <div>{make_page_pills(9, 16)}</div>
        </div>

      </div>

      <div style="display: flex; justify-content: space-between; margin-top: 2.5rem; border-top: 1px solid #30363d; padding-top: 1.5rem; flex-wrap: wrap; gap: 10px;">
        <a href="prologue.html" class="neon-red-btn">← Prologue</a>
        <a href="chapter-1-page-1.html" class="neon-red-btn">Chapter 1 (P.1) →</a>
      </div>
    </section>
  </main>
  <footer>
    <p>&copy; 2026 Bombshell Wire. Open Source & Uncensored.</p>
  </footer>
</body>
</html>"""

    with open(filename, "w") as f:
        f.write(html)
    print("SUCCESS: Phantom Index fully restored with complete chapter manifests and glowing neon red styling!")

generate_full_phantom_index()
