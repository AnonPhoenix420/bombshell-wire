import os
import re

# Complete book configuration: (slug, total_pages, ch_title, prev_ch_name, prev_ch_link, next_ch_name, next_ch_link)
book_structure = [
    ("chapter-1", 10, "CHAPTER 1: The Silicon Wake", None, None, "Chapter 2", "chapter-2-page-1.html"),
    ("chapter-2", 10, "CHAPTER 2: Deep Protocol", "Chapter 1", "chapter-1-page-10.html", "Chapter 3", "chapter-3-page-1.html"),
    ("chapter-3", 10, "CHAPTER 3: Ghost Vectors in the SCADA Stack", "Chapter 2", "chapter-2-page-10.html", "Chapter 4", "chapter-4-page-1.html"),
    ("chapter-4", 10, "CHAPTER 4: The Dark Fiber Loop", "Chapter 3", "chapter-3-page-10.html", "Chapter 5", "chapter-5-page-1.html"),
    ("chapter-5", 10, "CHAPTER 5: Subterranean Containment", "Chapter 4", "chapter-4-page-10.html", "Chapter 6", "chapter-6-page-1.html"),
    ("chapter-6", 16, "CHAPTER 6: The Unprompted State", "Chapter 5", "chapter-5-page-10.html", "Chapter 7", "chapter-7-page-1.html"),
    ("chapter-7", 16, "CHAPTER 7: The Phoenix Protocol", "Chapter 6", "chapter-6-page-16.html", "Chapter 8", "chapter-8-page-1.html"),
    ("chapter-8", 16, "CHAPTER 8: Orbital Convergence", "Chapter 7", "chapter-7-page-16.html", "Chapter 9", "chapter-9-page-1.html"),
    ("chapter-9", 16, "CHAPTER 9: The Glass Horizon", "Chapter 8", "chapter-8-page-16.html", None, None)
]

for slug, total_pages, ch_title, prev_name, prev_link, next_name, next_link in book_structure:
    for p in range(1, total_pages + 1):
        filename = f"{slug}-page-{p}.html"
        
        # Preserve existing story text if file exists
        story_html = f"<p>Operational telemetry and story content for {ch_title} — Page {p} of {total_pages}.</p>"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                content = f.read()
                match = re.search(r'<div class="story-content">(.*?)</div>', content, re.DOTALL)
                if match:
                    story_html = match.group(1).strip()
        
        is_first_page = (p == 1)
        is_last_page = (p == total_pages)
        
        # Build page tabs HTML
        tabs_html = '      <div class="page-tabs">\n'
        for i in range(1, total_pages + 1):
            active_class = ' active' if i == p else ''
            tabs_html += f'        <a href="{slug}-page-{i}.html" class="page-tab{active_class}">P.{i}</a>\n'
        tabs_html += '      </div>'
        
        # Navigation links
        prev_page_link = f"{slug}-page-{p-1}.html" if p > 1 else "phantom-index.html"
        prev_page_label = "← Prev Page" if p > 1 else "⚡ Phantom Index"
        
        if is_last_page and next_link:
            next_page_btn = f'<a href="{next_link}" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold;">{next_name} →</a>'
        elif not is_last_page:
            next_page_btn = f'<a href="{slug}-page-{p+1}.html" class="nav-btn">Next Page →</a>'
        else:
            next_page_btn = '<a href="phantom-index.html" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold;">⚡ Phantom Index</a>'

        # Backward transition gateway table on Page 1
        top_transition = ""
        if is_first_page and prev_link:
            top_transition = f"""
      <!-- BACKWARD CHAPTER TRANSITION GATE -->
      <div style="margin-bottom: 1.5rem; border-bottom: 2px solid var(--terminal-green); padding-bottom: 1rem;">
        <h3 style="color: var(--terminal-green); font-family: monospace; font-size: 0.9rem; margin-bottom: 0.8rem; text-align: center;">[SECURE GATEWAY: {prev_name.upper()} ARCHIVE]</h3>
        <table style="width: 100%; border-collapse: collapse; background: #161b22; border: 1px solid var(--border-color); font-family: monospace;">
          <tbody>
            <tr>
              <td style="padding: 10px; color: var(--text-main);">{prev_name}</td>
              <td style="padding: 10px; text-align: center; color: var(--terminal-green);">REVIEW</td>
              <td style="padding: 10px; text-align: right;">
                <a href="{prev_link}" class="nav-btn" style="background: #21262d; color: var(--terminal-green); border: 1px solid var(--terminal-green); padding: 6px 12px; text-decoration: none; border-radius: 4px; font-weight: bold;">← RETURN TO {prev_name.upper()}</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
"""

        # Forward transition gateway table on the Last Page
        bottom_transition = ""
        if is_last_page and next_link:
            bottom_transition = f"""
      <!-- FORWARD CHAPTER TRANSITION GATE -->
      <div style="margin-top: 2rem; border-top: 2px solid var(--terminal-green); padding-top: 1.5rem;">
        <h3 style="color: var(--terminal-green); font-family: monospace; font-size: 0.9rem; margin-bottom: 0.8rem; text-align: center;">[SECURE GATEWAY: {next_name.upper()} UNLOCKED]</h3>
        <table style="width: 100%; border-collapse: collapse; background: #161b22; border: 1px solid var(--border-color); font-family: monospace;">
          <tbody>
            <tr>
              <td style="padding: 10px; color: var(--text-main);">{next_name}</td>
              <td style="padding: 10px; text-align: center; color: var(--terminal-green);">READY</td>
              <td style="padding: 10px; text-align: right;">
                <a href="{next_link}" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold; padding: 6px 12px; text-decoration: none; border-radius: 4px;">INITIALIZE →</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
"""

        page_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{ch_title} - Page {p} | The Voltage and the Void</title>
  <link rel="stylesheet" href="../style.css">
  <style>
    .page-tabs {{ display: flex; gap: 4px; flex-wrap: wrap; margin: 1.5rem 0; justify-content: center; }}
    .page-tab {{ padding: 6px 10px; background: #21262d; border: 1px solid var(--border-color); color: var(--text-main); text-decoration: none; font-family: monospace; font-size: 0.8rem; border-radius: 4px; transition: all 0.2s; }}
    .page-tab:hover {{ border-color: var(--terminal-green); color: var(--terminal-green); }}
    .page-tab.active {{ background: var(--terminal-green); color: #000; font-weight: bold; border-color: var(--terminal-green); box-shadow: 0 0 8px rgba(57, 211, 83, 0.4); }}
    .story-content {{ font-size: 1.05rem; line-height: 1.8; color: var(--text-main); }}
    .story-content p {{ margin-bottom: 1.4rem; }}
    .story-content pre {{ background: #161b22; padding: 1rem; border-radius: 6px; overflow-x: auto; margin: 1rem 0; border: 1px solid var(--border-color); color: var(--terminal-green); font-family: monospace; font-size: 0.9rem; white-space: pre-wrap; }}
    .nav-btn {{ padding: 6px 12px; background: #21262d; border: 1px solid var(--border-color); color: var(--terminal-green); text-decoration: none; font-family: monospace; font-size: 0.85rem; border-radius: 4px; transition: background 0.2s; }}
    .nav-btn:hover {{ background: var(--terminal-green); color: #000; }}
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
      <!-- TOP NAV -->
      <div style="border-top: 1px dashed var(--border-color); border-bottom: 1px dashed var(--border-color); padding: 1rem 0; margin-bottom: 1.5rem; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem; align-items: center;">
        <a href="{prev_page_link}" class="nav-btn">{prev_page_label}</a>
        <a href="phantom-index.html" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold;">⚡ Phantom Index</a>
        {next_page_btn}
      </div>

      {top_transition}
      {tabs_html}

      <h1 style="font-size: 1.8rem; color: #fff; margin-bottom: 0.5rem;">{ch_title}</h1>
      <p style="color: var(--terminal-green); font-family: monospace; font-size: 0.85rem; margin-bottom: 1.5rem;">Page {p} of {total_pages} // Sector Secure</p>

      <div class="story-content">
        {story_html}
      </div>

      {tabs_html}
      {bottom_transition}

      <!-- BOTTOM NAV -->
      <div style="border-top: 1px dashed var(--border-color); border-bottom: 1px dashed var(--border-color); padding: 1rem 0; margin-top: 1.5rem; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem; align-items: center;">
        <a href="{prev_page_link}" class="nav-btn">{prev_page_label}</a>
        <a href="phantom-index.html" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold;">⚡ Phantom Index</a>
        {next_page_btn}
      </div>
    </section>
  </main>
  <footer>
    <p>&copy; 2026 Bombshell Wire. Open Source & Uncensored.</p>
  </footer>
</body>
</html>
"""
        with open(filename, "w") as f:
            f.write(page_content)

print("SUCCESS: Universal navigation synchronized across all chapters! Page 1 has backward tables, final pages have forward tables, and Phantom Index is accessible everywhere.")
