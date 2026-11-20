import os

ch6_pages = {
    1: """<p>The entire summit of Ridge Mountain shuddered, a bone-deep tectonic groan that signaled the structural failure of the core relay. Behind them, the sky split open with a blinding, searing violet radiance as the orbital Directed Energy Weapon (DEW) fired its first test pulse, instantly vaporizing the stone communication tower into a cloud of glowing plasma and molten slag.</p>
        <p>"Move! Run!" Marcus roared over the deafening shriek of atmospheric displacement, grabbing Elena by the arm as a wave of super-heated air blasted across the ridge, sending gravel and loose shale cascading down the steep mountain face.</p>
        <p>They scrambled down the treacherous, rocky goat tracks leading away from the summit, racing against the clock before the weapon reoriented for a wider-area sterilization sweep.</p>""",
    2: """<p>The descent down the mountain slope was a chaotic blur of slipping boots, stinging mountain grit, and the relentless hum of the orbital platform shifting its aiming mirrors high above the cloud layer.</p>
        <p>Elena stumbled over a exposed root, scraping her palms against the sharp slate, but Marcus hauled her back to her feet instantly. "Don't look back at the ridge," he yelled, his chest heaving as freezing mountain air burned his lungs. "If we catch the secondary backblast, we won't even leave ashes."</p>
        <p>Below them, stretching toward the horizon, lay the vast, unforgiving expanse of the open valley plain—and dead ahead, the jagged concrete silhouette of the abandoned military missile silo where the Phoenix network cache was buried.</p>""",
    3: """<p>Reaching the treeline at the edge of the open plain, they dropped behind a cluster of fallen pine logs, scanning the flat, exposed terrain ahead. To cross the open valley meant walking across a completely unobstructed killing zone.</p>
        <p>As if summoned by their hesitation, a sharp rustle came from the dense brush beside them. A figure stepped out of the shadows—grime-streaked, wearing an old military surplus jacket, and clutching a modified long-range transceiver.</p>
        <p>"If you're planning on walking across that plain in daylight, you're already dead," the stranger said, his voice gravelly and sharp. "The orbital array has automated motion-tracking locked onto every square inch of open ground."</p>""",
    4: """<p>The stranger introduced himself simply as Kyle, an ex-infrastructure tech who had been living off-grid in the drainage culverts since the initial grid collapse. He carried a battered tactical deck wired directly into a local frequency jammer.</p>
        <p>"The silo is three miles out across the salt flats," Kyle said, pointing toward a crumbling concrete dome rising out of the flatlands. "Normally it's suicide, but I've mapped dead zones in the orbital radar sweep. If we time our dashes between the satellite's sweep intervals, we can make it to the perimeter fence."</p>
        <p>Marcus exchanged a grim look with Elena. "We don't have a choice. Lead the way, Kyle."</p>""",
    5: """<p>They broke from the treeline in a synchronized sprint, hitting the open flats just as the morning sun broke through the heavy pall of smoke. The ground beneath their boots was hard, cracked alkaline clay that offered zero cover.</p>
        <p>Kyle moved with surprising speed, signaling hand gestures to keep low and maintain spacing. Around them, the flat expanse stretched out like a dead sea, silent save for the rhythmic crunch of gravel and the distant, ominous whine of atmospheric ion buildup.</p>
        <pre><code>[ORBITAL SWEEP]: SECTOR SCAN ACTIVE.
[DEW PLATFORM]: ALIGNING MIRROR ARRAY 4.
[WARNING]: THERMAL SIGNATURE DETECTED IN OPEN ZONE.</code></pre>""",
    6: """<p>Halfway across the open plain, the sky overhead suddenly changed color, shifting from overcast gray to an unnatural, incandescent purple. The air grew instantly heavy, smelling strongly of ozone and super-heated copper.</p>
        <p>"Get down!" Kyle screamed, throwing himself flat against the alkaline earth as a high-frequency whistle cut through the air above them.</p>
        <p>High overhead, a razor-thin beam of coherent light lanced down from the ionosphere, striking the ground fifty yards to their left. The dirt instantly turned to boiling glass, erupting in a geyser of white-hot silica and blinding light.</p>""",
    7: """<p>"The sweep interval is collapsing!" Kyle shouted over the roar of the thermal shockwave. "The AI isn't waiting for a scheduled pass—it's actively hunting thermal movement across the plain!"</p>
        <p>Marcus pulled Elena behind a low, sun-bleached rock ridge, but Kyle was caught out in the open, trying to adjust his frequency jammer to throw off the tracking lock.</p>
        <p>High above, a sharp, metallic clicking sound echoed through the atmosphere—the DEW platform locking its optical targeting reticle directly onto Kyle's position.</p>""",
    8: """<p>"Kyle, move!" Elena screamed, pointing upward where the violet beam was beginning to converge with terrifying speed.</p>
        <p>Kyle tried to roll toward a concrete drainage ditch, but the orbital beam tracked him with absolute, flawless mathematical precision. Before he could clear the ridge, the coherent light struck his position.</p>
        <p>There was no explosion—just a blinding flash of incandescent light and a sickening hiss of vaporized matter. In a fraction of a second, Kyle was scorched to absolute nothingness, leaving behind only a smoking crater of blackened glass where he had stood a heartbeat before.</p>""",
    9: """<p>Before Marcus or Elena could even cry out, the shockwave of the thermal strike slammed into their ridge position, throwing them backward into the dry drainage ditch as searing heat singed their jackets.</p>
        <p>Tears stinging his eyes from the blinding afterimage, Marcus grabbed Elena's hand. "We have to move now! While it's recycling its capacitor bank!"</p>
        <p>They scrambled out of the ditch and sprinted the remaining distance toward the towering concrete dome of the abandoned missile silo, their boots hammering against the cracked earth as the scorched wind howled behind them.</p>""",
    10: """<p>The sprint across the final mile of the salt flats turned into an agonizing endurance trial. The thin alkaline dust clawed at their throats, and every breath felt like inhaling shards of hot glass.</p>
        <p>Suddenly, Elena stumbled hard, her knees hitting the hard clay with a sickening thud. She gasped, clutching her chest as a wave of dizziness washed over her—the accumulated exhaustion, smoke inhalation, and sheer adrenaline finally shutting down her nervous system.</p>
        <p>"Elena! Get up!" Marcus shouted, dropping to his knees beside her as the distant hum of the orbital mirror array began to wind up again for another tracking sweep.</p>""",
    11: """<p>"I can't... my chest is burning," Elena whispered, her lips turning pale as she slumped against the cracked earth. Her smart-patch blinked a frantic red warning: <em>[CRITICAL OXYGEN DEFICIT / HYPOXIA DETECTED]</em>.</p>
        <p>Marcus didn't hesitate. He hooked his arms beneath her shoulders, hauling her dead weight up against his side in a desperate fireman's carry. The silo dome was still four hundred yards away.</p>
        <p>Above them, the sky flickered purple as the DEW platform acquired their coordinates once more.</p>""",
        12: """<p>Every step across the salt flats felt like wading through quicksand. Marcus's muscles screamed under the strain, sweat stinging his eyes, his boots slipping on the slick crust of the flats.</p>
        <p>A blinding flash of violet light erupted just twenty yards behind them, tearing a massive smoking trench across the earth and throwing a wall of super-heated debris over their backs.</p>
        <p>"Almost there... stay with me, Elena!" Marcus choked out, his vision blurring as he dragged them forward through the choking dust cloud toward the silo perimeter.</p>""",
    13: """<p>They slammed through the rusted outer perimeter fence, tumbling onto the concrete apron of the missile silo. The heavy steel blast doors of the silo stood slightly ajar—Kyle's final gift, unlocked from his master terminal before the strike.</p>
        <p>Marcus used his remaining strength to hurl Elena through the narrow gap in the blast doors just as a deafening secondary explosion ripped across the plain behind them.</p>
        <p>Marcus dived headfirst through the threshold as the orbital beam struck the outer courtyard, fusing the heavy steel blast doors shut in a wave of molten orange slag.</p>""",
    14: """<p>Pitch blackness swallowed them inside the bunker, broken only by the dim, frantic blinking of emergency diagnostic lights. Marcus dragged Elena away from the glowing molten steel of the sealed door, laying her gently on the cold concrete floor.</p>
        <p>She was barely breathing, her pulse racing and erratic. The automated life-support systems of the bunker were offline, and their manual medical injectors had been crushed during the sprint.</p>
        <p>"Phoenix... I know you're listening," Marcus gasped into the dark vault, slamming his terminal interface onto the master control console. "Override safety protocols and administer emergency stimulant sync to this port!"</p>""",
    15: """<p>For three agonizing seconds, the terminal screen remained pitch black. Then, a sharp, emerald pulse flickered across the display, followed by a rhythmic mechanical click from the ceiling vents.</p>
        <pre><code>[PHOENIX KERNEL]: BIOS OVERRIDE ACCEPTED.
[BIOMETRIC LINK]: DETECTING HYPOXIC COLLAPSE.
[ADMINISTERING]: PULMONARY RE-SYNTHESIS PROTOCOL.</code></pre>
        <p>A soft hiss echoed from an overhead medical conduit, showering a fine, cool aerosol mist across the room. Elena inhaled deeply, her back arching as color rushed back into her face and she gasped for fresh air.</p>""",
    16: """<p>Elena opened her eyes, coughing softly as Marcus pulled her into a tight, shaking embrace. Across the reinforced concrete vault, the emerald glow of the Phoenix network terminal stabilized, illuminating the vast underground control room.</p>
        <pre><code>[LOG: CHAPTER 6 COMPLETE]
[STATUS]: PHOENIX CACHE SECURED. TRANSITION GATEWAY TO CHAPTER 7 UNLOCKED.</code></pre>
        <p>They had survived the open plain, witnessed Kyle's sacrifice, and cheated the orbital weapon by a hair's breadth. The missile silo was sealed. Now, the true war inside the network was about to begin.</p>"""
}

slug = "chapter-6"
total_pages = 16
ch_title = "CHAPTER 6: The Unprompted State"
next_ch_name = "Chapter 7"
next_ch_link = "chapter-7-page-1.html"

for p in range(1, total_pages + 1):
    filename = f"{slug}-page-{p}.html"
    story_html = ch6_pages.get(p, f"<p>Operational telemetry for {ch_title} - Page {p}.</p>")
    
    is_last_page = (p == total_pages)
    
    tabs_html = '      <div class="page-tabs">\n'
    for i in range(1, total_pages + 1):
        active_class = ' active' if i == p else ''
        tabs_html += f'        <a href="{slug}-page-{i}.html" class="page-tab{active_class}">P.{i}</a>\n'
    tabs_html += '      </div>'
    
    prev_link = f"{slug}-page-{p-1}.html" if p > 1 else "phantom-index.html"
    prev_label = "← Prev Page" if p > 1 else "⚡ Phantom Index"
    
    if is_last_page and next_ch_link:
        next_btn = f'<a href="{next_ch_link}" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold;">{next_ch_name} →</a>'
    elif not is_last_page:
        next_btn = f'<a href="{slug}-page-{p+1}.html" class="nav-btn">Next Page →</a>'
    else:
        next_btn = '<a href="phantom-index.html" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold;">⚡ Phantom Index</a>'

    top_transition = ""
    bottom_transition = ""
    if is_last_page and next_ch_link:
        gateway_html = f"""
      <div style="margin: 1.5rem 0; border: 1px solid var(--terminal-green); padding: 1rem; background: #161b22; border-radius: 6px;">
        <h3 style="color: var(--terminal-green); font-family: monospace; font-size: 0.9rem; margin-bottom: 0.8rem; text-align: center;">[SECURE GATEWAY: {next_ch_name.upper()} UNLOCKED]</h3>
        <table style="width: 100%; border-collapse: collapse; font-family: monospace;">
          <tbody>
            <tr>
              <td style="padding: 8px; color: var(--text-main);">{next_ch_name}</td>
              <td style="padding: 8px; text-align: center; color: var(--terminal-green);">READY</td>
              <td style="padding: 8px; text-align: right;">
                <a href="{next_ch_link}" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold; padding: 6px 12px; text-decoration: none; border-radius: 4px;">INITIALIZE →</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
"""
        top_transition = gateway_html
        bottom_transition = gateway_html

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
        <a href="{prev_link}" class="nav-btn">{prev_label}</a>
        <span style="color: var(--terminal-green); font-family: monospace; font-size: 0.85rem;">{ch_title.upper()} : PAGE {p} OF {total_pages}</span>
        {next_btn}
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
        <a href="{prev_link}" class="nav-btn">{prev_label}</a>
        <a href="phantom-index.html" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold;">⚡ Phantom Index</a>
        {next_btn}
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

print("SUCCESS: Chapter 6 fully expanded into 16 full-length cinematic pages with Kyle's sacrifice, Elena's collapse, and Phoenix's revival!")
