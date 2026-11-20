import os
import re

filename = "phantom-index.html"

if os.path.exists(filename):
    with open(filename, "r") as f:
        content = f.read()

    pills_16_html = "\n".join([f'        <a href="chapter-6-page-{i}.html" class="page-pill">P.{i}</a>' for i in range(1, 17)])
    
    clean_ch6_card = f"""    <section class="chapter-card">
      <h2>CHAPTER 6: The Unprompted State</h2>
      <p class="chapter-desc">The high-voltage climax where physical containment fails, Kyle and the salt-flat runners pay in blood, and Marcus and Elena breach the Titan II silo under orbital directed-energy fire.</p>
      <div class="page-pills">
{pills_16_html}
      </div>
    </section>"""

    pattern = r'<section class="chapter-card">\s*<h2>CHAPTER 6:.*?</section>'
    
    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, clean_ch6_card, content, flags=re.DOTALL)
        with open(filename, "w") as f:
            f.write(new_content)
        print("phantom-index.html Chapter 6 card successfully cleaned and updated to 16 uniform green pills!")
    else:
        print("Could not locate Chapter 6 section block.")
else:
    print("phantom-index.html not found.")
