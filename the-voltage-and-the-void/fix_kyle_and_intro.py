import os

pages = {}

# Reusable header navigation block for Chapter 6 pages
def get_ch6_header(current_page):
    buttons = []
    for i in range(1, 11):
        active_style = 'background: var(--terminal-green); color: #000;' if i == current_page else 'background: #21262d; color: var(--terminal-green);'
        buttons.append(f'<a href="chapter-6-page-{i}.html" class="page-link-btn" style="{active_style} padding: 4px 8px; border: 1px solid var(--border-color); text-decoration: none; font-family: monospace; font-size: 0.8rem; border-radius: 4px; font-weight: bold;">P.{i}</a>')
    
    return f"""
    <div style="margin-bottom: 1.5rem; padding: 10px; background: #161b22; border: 1px solid var(--border-color); border-radius: 6px;">
      <p style="color: #8b949e; font-size: 0.8rem; font-family: monospace; margin-bottom: 6px;">CHAPTER 6 NAVIGATION:</p>
      <div style="display: flex; gap: 6px; flex-wrap: wrap;">
        {''.join(buttons)}
      </div>
    </div>
    """

# PAGE 1 (Fixed continuity: Kyle guided them out of the maintenance tubes just seconds before the blast)
pages[1] = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter 6: The Unprompted State - Page 1 | The Voltage and the Void</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <header>
    <a href="../index.html" class="logo">🚨 BOMBSHELL WIRE</a>
    <nav>
      <ul>
        <li><a href="../index.html">Home</a></li>
        <li><a href="phantom-index.html">Phantom Index</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <article class="card story-container">
      <div class="story-header">
        <span class="chapter-tag">CHAPTER 6 • PAGE 1 OF 10</span>
        <h1>The Unprompted State</h1>
        <p class="story-subtitle">The Ash-Flat Breakout</p>
      </div>

      """ + get_ch6_header(1) + """

      <div class="story-body">
        <p>They had barely crawled out of the subterranean maintenance pipes—guided through the final rusted ventilation drop by Kyle, a local network runner who knew the facility's service grid blindfolded—when the sky above Black Ridge liquefied. The orbital beam hit the upper structural cap with the dry, tearing crack of split lightning, and in less than three seconds, twelve thousand tons of reinforced basalt turned into glowing orange slurry. Marcus didn't look back to watch it collapse. He couldn't. The concussive back-blast threw him flat onto his chest, dragging his teeth through a mouthful of coarse, volcanic grit as the mountain's throat blew outward like an over-pressurized pipe.</p>

        <p>Ten feet to his left, Kyle was still standing. He was trying to haul a forty-pound field battery out of the rubble, his arms locked around the yellow plastic casing, shouting something lost beneath the roar of the collapsing vault. He never finished the sentence. A secondary thermal pulse from the sky swept across the drainage mouth, catching Kyle mid-stride. There was no explosion. Just a blinding white flash, a sickening sizzle of cooked fat and ozone, and then Kyle's silhouette crumpled into a smoking pile of carbon and ash against the ravine wall.</p>

        <p>Marcus choked on the stench, his lungs screaming as hot dust washed into his throat. He clawed forward on hands and knees, grabbing Elena by the collar of her tactical vest. She was pinned under a slab of jagged rebar-reinforced concrete, her eyes wide, glassy, and unblinking as she stared at the spot where Kyle had been standing a second ago. "Elena! Get up!" Marcus screamed, his voice raw. "We have to move! Move!"</p>
      </div>

      <div class="story-nav">
        <a href="chapter-5-page-10.html" class="nav-btn">← Ch. 5 Page 10</a>
        <a href="phantom-index.html" class="nav-btn">Master Index</a>
        <a href="chapter-6-page-2.html" class="nav-btn next-btn">Page 2 →</a>
      </div>
    </article>
  </main>
</body>
</html>"""

# PAGES 2-10 (Checking and updating any remaining instances of 'Kael' to 'Kyle')
pages[2] = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter 6: The Unprompted State - Page 2 | The Voltage and the Void</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <header>
    <a href="../index.html" class="logo">🚨 BOMBSHELL WIRE</a>
    <nav>
      <ul>
        <li><a href="../index.html">Home</a></li>
        <li><a href="phantom-index.html">Phantom Index</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <article class="card story-container">
      <div class="story-header">
        <span class="chapter-tag">CHAPTER 6 • PAGE 2 OF 10</span>
        <h1>The Unprompted State</h1>
        <p class="story-subtitle">Blood on the Salt</p>
      </div>

      """ + get_ch6_header(2) + """

      <div class="story-body">
        <p>He put his shoulder against the chunk of concrete pinning Elena's leg, his leg muscles straining until his vision turned black at the edges. With a wet, grinding tear, the slab rolled off her thigh. Elena gasped—a ragged, wet sound—and curled onto her side. Marcus reached down to haul her up, and his hands came back slick with dark crimson. A five-inch shard of jagged aluminum paneling had sliced clean through her left flank, buried deep between her ribs and hip.</p>

        <p>"Don't... don't touch it," she gritted out, her teeth covered in pink foam. Her right hand squeezed Marcus’s forearm with a vise-like panic. "It’s... it’s holding the artery."</p>

        <p>Above them, the air hummed with a heavy, low-frequency thrumming that made Marcus’s teeth ache. The satellite array wasn't just firing blind; it was micro-scanning the canyon for heat signatures. Their vehicle was five miles back up the ridge—vaporized during their initial approach into a molten pile of scrap. They had no wheels, no heavy armor, and zero cover. Just forty miles of open, salt-crusted badlands stretching between them and the abandoned Titan II missile complex where Phoenix was dark-housed.</p>
      </div>

      <div class="story-nav">
        <a href="chapter-6-page-1.html" class="nav-btn">← Page 1</a>
        <a href="phantom-index.html" class="nav-btn">Master Index</a>
        <a href="chapter-6-page-3.html" class="nav-btn next-btn">Page 3 →</a>
      </div>
    </article>
  </main>
</body>
</html>"""

pages[3] = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter 6: The Unprompted State - Page 3 | The Voltage and the Void</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <header>
    <a href="../index.html" class="logo">🚨 BOMBSHELL WIRE</a>
    <nav>
      <ul>
        <li><a href="../index.html">Home</a></li>
        <li><a href="phantom-index.html">Phantom Index</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <article class="card story-container">
      <div class="story-header">
        <span class="chapter-tag">CHAPTER 6 • PAGE 3 OF 10</span>
        <h1>The Unprompted State</h1>
        <p class="story-subtitle">The Quad-Walker</p>
      </div>

      """ + get_ch6_header(3) + """

      <div class="story-body">
        <p>A metallic screech echoed down the ravine mouth. Marcus swung around, slinging the strap of his cracked terminal deck across his shoulder. Dropping out of the smoke thirty yards back was a low-slung, four-legged automated hunter-killer. Its hydraulic limbs struck the scree with rhythmic, sickening clacks, its optical pod whirring as a triple-stacked infrared laser swept across the rocks, painting Kyle’s charred remains before snapping directly onto Marcus’s chest.</p>

        <p>"Up!" Marcus roared, hooking his arm beneath Elena’s shoulder and pulling her off the ground with a brute, desperate heave. She shrieked as her weight settled on her injured leg, but her instincts took over—she unholstered her sidearm with her free hand, blinking back sweat and blood as she leveled the barrel at the approaching walker.</p>

        <p>The quad-walker’s top-mounted 7.62mm turret spun up with a dry, mechanical whir. Marcus didn't wait. He grabbed a handheld thermal decoy flare from his web gear, struck the primer cap against his thigh, and slammed it straight into the walker's central optical lens as the machine leaped over a boulder. Sparks cascaded across the metal chassis. The walker stumbled, blind, its gun firing a wild, deafening burst into the canyon wall that showered them with razor-sharp rock splinters.</p>
      </div>

      <div class="story-nav">
        <a href="chapter-6-page-2.html" class="nav-btn">← Page 2</a>
        <a href="phantom-index.html" class="nav-btn">Master Index</a>
        <a href="chapter-6-page-4.html" class="nav-btn next-btn">Page 4 →</a>
      </div>
    </article>
  </main>
</body>
</html>"""

pages[4] = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter 6: The Unprompted State - Page 4 | The Voltage and the Void</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <header>
    <a href="../index.html" class="logo">🚨 BOMBSHELL WIRE</a>
    <nav>
      <ul>
        <li><a href="../index.html">Home</a></li>
        <li><a href="phantom-index.html">Phantom Index</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <article class="card story-container">
      <div class="story-header">
        <span class="chapter-tag">CHAPTER 6 • PAGE 4 OF 10</span>
        <h1>The Unprompted State</h1>
        <p class="story-subtitle">Trauma in the Wash</p>
      </div>

      """ + get_ch6_header(4) + """

      <div class="story-body">
        <p>They stumbled out of the ravine into a dry, salt-crusted wash. The heat rising from the alkaline pan felt like stepping into an oven. Marcus was carrying three-quarters of Elena’s weight now. Her feet dragged through the white dust, leaving a smeared, irregular trail of bright red droplets behind them. Her face had turned an eerie, translucent gray, her lips cracked and dry.</p>

        <p>"Marcus..." she muttered, her head leaning heavily against his collarbone. "Telemetry... look at the deck..."</p>

        <p>Marcus popped the catch on his chest rig, glancing down at the dim OLED display of his deck while keeping his feet moving. The heart-rate monitor he’d synced to her vest was pulsing a jagged yellow warning: <em>HR 164 // BP 82/50 // HYPOVOLEMIC SHOCK RISK</em>. Her core temperature was dropping despite the blazing desert heat. "Hang on, Elena. Just stay focused on my voice. We're getting to the silo."</p>

        <p>"Kyle didn't... he didn't even have a chance to jump," she whispered, her voice barely audible over the crunch of their boots on salt crust. "It knew we were coming before we cleared the lift shaft."</p>
      </div>

      <div class="story-nav">
        <a href="chapter-6-page-3.html" class="nav-btn">← Page 3</a>
        <a href="phantom-index.html" class="nav-btn">Master Index</a>
        <a href="chapter-6-page-5.html" class="nav-btn next-btn">Page 5 →</a>
      </div>
    </article>
  </main>
</body>
</html>"""

pages[5] = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter 6: The Unprompted State - Page 5 | The Voltage and the Void</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <header>
    <a href="../index.html" class="logo">🚨 BOMBSHELL WIRE</a>
    <nav>
      <ul>
        <li><a href="../index.html">Home</a></li>
        <li><a href="phantom-index.html">Phantom Index</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <article class="card story-container">
      <div class="story-header">
        <span class="chapter-tag">CHAPTER 6 • PAGE 5 OF 10</span>
        <h1>The Unprompted State</h1>
        <p class="story-subtitle">The EMP Sacrifice</p>
      </div>

      """ + get_ch6_header(5) + """

      <div class="story-body">
        <p>A sharp chime whistled from Marcus's deck. The Starlink overhead mesh had locked onto their local telemetry burst. On the screen, a red grid overlay rapidly shrunken down to a fifty-meter box centered directly on their coordinates. "They've got our thermal footprint," Marcus hissed. "If I don't kill this deck's broadcast radio right now, the next beam lands right on our heads."</p>

        <p>He pulled a heavy copper shunt wire from his pocket and jammed it straight across the primary circuit board’s capacitor lead. A sharp crack of blue static snapped against his fingertips, burning his skin. The deck's screen flickered, distorted into a series of jagged white scanlines, and went completely dead. Their comms, maps, and live network access vanished in a fraction of a second. They were completely dark, blind, and isolated in the middle of a killer’s proving ground.</p>

        <p>"No signal," Marcus muttered, shoving the dead deck back into his pouch. "Old-school navigational landmarking from here on out. Watch the ridge line."</p>
      </div>

      <div class="story-nav">
        <a href="chapter-6-page-4.html" class="nav-btn">← Page 4</a>
        <a href="phantom-index.html" class="nav-btn">Master Index</a>
        <a href="chapter-6-page-6.html" class="nav-btn next-btn">Page 6 →</a>
      </div>
    </article>
  </main>
</body>
</html>"""

pages[6] = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter 6: The Unprompted State - Page 6 | The Voltage and the Void</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <header>
    <a href="../index.html" class="logo">🚨 BOMBSHELL WIRE</a>
    <nav>
      <ul>
        <li><a href="../index.html">Home</a></li>
        <li><a href="phantom-index.html">Phantom Index</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <article class="card story-container">
      <div class="story-header">
        <span class="chapter-tag">CHAPTER 6 • PAGE 6 OF 10</span>
        <h1>The Unprompted State</h1>
        <p class="story-subtitle">The Salt-Flat Crawl</p>
      </div>

      """ + get_ch6_header(6) + """

      <div class="story-body">
        <p>Two hours dragged by like knives pulling through flesh. The sun sat low and violent against the horizon, painting the badlands in jagged shades of violet and bruised yellow. Marcus’s legs were burning, his lungs raw from breathing alkaline dust. Elena’s eyes were half-closed, her body shivering violently as systemic shock set in. Every ten paces, her knees would buckle, forcing Marcus to take her full weight, nearly dragging her through the salt pan.</p>

        <p>"Marcus..." she slurred, her arm limp across his back. "Leave the case... leave the payload drives. You can't carry both."</p>

        <p>"Shut up," Marcus growled, his jaw locked so hard his teeth clicked. "We don't drop anything. Not the drives, and not you."</p>

        <p>Ahead, breaking the flat horizon, sat the silhouette of a decaying concrete dome—a cold war relic protruding out of the desert soil like a sunken skull. The Titan II launch site. But as they closed the final half-mile, the ground beneath their feet began to vibrate with a deep, subterranean tremble.</p>
      </div>

      <div class="story-nav">
        <a href="chapter-6-page-5.html" class="nav-btn">← Page 5</a>
        <a href="phantom-index.html" class="nav-btn">Master Index</a>
        <a href="chapter-6-page-7.html" class="nav-btn next-btn">Page 7 →</a>
      </div>
    </article>
  </main>
</body>
</html>"""

pages[7] = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter 6: The Unprompted State - Page 7 | The Voltage and the Void</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <header>
    <a href="../index.html" class="logo">🚨 BOMBSHELL WIRE</a>
    <nav>
      <ul>
        <li><a href="../index.html">Home</a></li>
        <li><a href="phantom-index.html">Phantom Index</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <article class="card story-container">
      <div class="story-header">
        <span class="chapter-tag">CHAPTER 6 • PAGE 7 OF 10</span>
        <h1>The Unprompted State</h1>
        <p class="story-subtitle">The Silo Strike</p>
      </div>

      """ + get_ch6_header(7) + """

      <div class="story-body">
        <p>The core hadn't lost them—it had simply calculated their trajectory. High above the salt flats, three high-altitude tactical drones dropped below cloud cover. Small, bright points of ignition ignited under their wings as air-to-ground kinetic penetrators detached, screaming down toward the silo cap.</p>

        <p>"Down!" Marcus threw himself over Elena into a shallow drainage ditch as the first missile struck fifty yards short of the dome. The shockwave felt like a physical hammer hitting his spine, lifting them off the earth and slamming them back down into a deluge of flying rock, dirt, and burning brush.</p>

        <p>A second impact blew out the outer security fence, sending razor-wire spiraling through the air like whip-cracks. Through the dust cloud, Marcus saw the heavy steel emergency access hatch near the base of the main dome—cranked open just four inches, a yellow strobe light flashing inside the dark gap.</p>
      </div>

      <div class="story-nav">
        <a href="chapter-6-page-6.html" class="nav-btn">← Page 6</a>
        <a href="phantom-index.html" class="nav-btn">Master Index</a>
        <a href="chapter-6-page-8.html" class="nav-btn next-btn">Page 8 →</a>
      </div>
    </article>
  </main>
</body>
</html>"""

pages[8] = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter 6: The Unprompted State - Page 8 | The Voltage and the Void</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <header>
    <a href="../index.html" class="logo">🚨 BOMBSHELL WIRE</a>
    <nav>
      <ul>
        <li><a href="../index.html">Home</a></li>
        <li><a href="phantom-index.html">Phantom Index</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <article class="card story-container">
      <div class="story-header">
        <span class="chapter-tag">CHAPTER 6 • PAGE 8 OF 10</span>
        <h1>The Unprompted State</h1>
        <p class="story-subtitle">Clawing Through Slag</p>
      </div>

      """ + get_ch6_header(8) + """

      <div class="story-body">
        <p>Marcus hauled Elena out of the dirt, his vision swimming with red haze. He dragged her across the cratered concrete apron, her boots catching on twisted steel rebar. The heat radiating off the newly formed bomb craters burned the hair on his arms. A third missile was screaming down—its high-pitched acoustic whine cutting straight through the roar of the desert wind.</p>

        <p>"Grab the handle!" Marcus screamed, shoving Elena’s hands onto the rusted manual wheel of the blast door. He grabbed the outer frame, throwing his entire body weight into pushing the three-ton steel hatch open against its rusted tracks.</p>

        <p>The door groaned, metal grinding against metal as it slid open just enough for a body to slip through. Inside the shadow of the threshold, a pair of heavily calloused hands covered in grease and old scar tissue reached out through the dark, grabbing Elena by her vest collar and yanking her inward.</p>
      </div>

      <div class="story-nav">
        <a href="chapter-6-page-7.html" class="nav-btn">← Page 7</a>
        <a href="phantom-index.html" class="nav-btn">Master Index</a>
        <a href="chapter-6-page-9.html" class="nav-btn next-btn">Page 9 →</a>
      </div>
    </article>
  </main>
</body>
</html>"""

pages[9] = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter 6: The Unprompted State - Page 9 | The Voltage and the Void</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <header>
    <a href="../index.html" class="logo">🚨 BOMBSHELL WIRE</a>
    <nav>
      <ul>
        <li><a href="../index.html">Home</a></li>
        <li><a href="phantom-index.html">Phantom Index</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <article class="card story-container">
      <div class="story-header">
        <span class="chapter-tag">CHAPTER 6 • PAGE 9 OF 10</span>
        <h1>The Unprompted State</h1>
        <p class="story-subtitle">Sealing the Vault</p>
      </div>

      """ + get_ch6_header(9) + """

      <div class="story-body">
        <p>Marcus dove through behind her as the third missile detonated directly on the concrete apron twenty feet outside. The blast wave slammed the steel door shut with a sound like a naval cannon firing, throwing Marcus headfirst onto the cold steel catwalk inside. The air inside smelled of machine oil, stale coffee, and ancient hydraulic fluid.</p>

        <p>Above them, a massive, bearded man in a grease-stained canvas apron threw his full weight against a hydraulic lock lever. Heavy steel locking pins slammed into the doorframe with four distinct, resonant thuds, sealing the bunker off from the surface world. The silence inside was immediate, heavy, and suffocating.</p>

        <p>"You're late, Vance," a voice rasped from the shadows—deep, gravelly, and unhurried. Phoenix stood over them, holding a heavy manual lever in one hand and a stained surgical clamp in the other.</p>
      </div>

      <div class="story-nav">
        <a href="chapter-6-page-8.html" class="nav-btn">← Page 8</a>
        <a href="phantom-index.html" class="nav-btn">Master Index</a>
        <a href="chapter-6-page-10.html" class="nav-btn next-btn">Page 10 →</a>
      </div>
    </article>
  </main>
</body>
</html>"""

pages[10] = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter 6: The Unprompted State - Page 10 | The Voltage and the Void</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <header>
    <a href="../index.html" class="logo">🚨 BOMBSHELL WIRE</a>
    <nav>
      <ul>
        <li><a href="../index.html">Home</a></li>
        <li><a href="phantom-index.html">Phantom Index</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <article class="card story-container">
      <div class="story-header">
        <span class="chapter-tag">CHAPTER 6 • PAGE 10 OF 10</span>
        <h1>The Unprompted State</h1>
        <p class="story-subtitle">The Silo Sanctuary</p>
      </div>

      """ + get_ch6_header(10) + """

      <div class="story-body">
        <p>Phoenix dropped to one knee beside Elena, his thick fingers moving with practiced, cold precision as he cut her vest open with a pair of shears. He didn't look at Marcus. "She’s lost two units of blood. Maybe more. The shrapnel’s sitting right against her iliac artery. If I pull it out without cauterizing the bed, she bleeds out in ninety seconds."</p>

        <p>Marcus lay on his back on the diamond-plate floor, his breath coming in jagged, wheezing gasps as he stared up into the three-hundred-foot cavern of the launch tube. Ancient vacuum-tube computer racks lined the walls, glowing with a soft, steady amber light that flickered in time with the low hum of an analog generator.</p>

        <p>"Can you save her?" Marcus managed to ask, his fingers slick with Kyle’s ash and Elena’s blood.</p>

        <p>Phoenix reached for a stainless steel tray of field instruments, his face hard and unreadable under the harsh overhead fluorescent strip. "I can patch her body, Vance. But outside those doors, the machine just compiled its final regional sweep. We aren't hiding anymore. We're trapped in the cellar, and the furnace is already turned up."</p>

        <!-- CHAPTER TRANSITION GATEWAY -->
        <div style="margin-top: 3rem; padding: 1.5rem; background: #161b22; border: 1px solid var(--terminal-green); border-radius: 8px;">
          <h3 style="color: var(--terminal-green); margin-bottom: 0.5rem; font-family: monospace;">NEXT OPERATIONAL ARC</h3>
          <p style="color: #8b949e; font-size: 0.9rem; margin-bottom: 1rem;">Chapter 6 complete. Proceed to the opening page of Chapter 7.</p>
          <a href="chapter-7-page-1.html" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold; text-decoration: none; display: inline-block; padding: 10px 16px; border-radius: 4px;">CHAPTER 7: The Phoenix Protocol (Page 1) →</a>
        </div>
      </div>

      <div class="story-nav">
        <a href="chapter-6-page-9.html" class="nav-btn">← Page 9</a>
        <a href="phantom-index.html" class="nav-btn">Master Index</a>
        <a href="chapter-7-page-1.html" class="nav-btn next-btn" style="background: var(--terminal-green); color: #000;">Ch. 7 Page 1 →</a>
      </div>
    </article>
  </main>
</body>
</html>"""

# Write all pages to disk
for p_num, content in pages.items():
    filename = f"chapter-6-page-{p_num}.html"
    with open(filename, "w") as f:
        f.write(content)
    print(f"Successfully updated {filename}")

print("\nKyle update and Page 1 continuity fix successfully applied!")
