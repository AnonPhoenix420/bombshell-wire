import os

pages = {}

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

# PAGE 1
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

# PAGE 2
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

# PAGE 3
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

# PAGE 4 (Expanded Detail: Entering the Alkaline Wash and Declaring Gear Weight)
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
        <p>They cleared the canyon mouth and spilled out into a blinding, featureless expanse of dry alkaline wash. The midday heat radiating off the salt crust felt like a blast furnace against their sweat-soaked skin. Marcus was hauling nearly all of Elena’s dead weight now, her combat boots dragging through the abrasive white dust and leaving a smeared, irregular furrow of dark blood behind them. Every step sent a white-hot spike of agony through her side where the aluminum shard was wedged.</p>

        <p>"Marcus..." she muttered, her head lolling against his shoulder, her breath coming in shallow, fluttering hitches. "The pack... drop the auxiliary battery. You're dragging an extra thirty pounds of dead weight. You won't make it to the basin."</p>

        <p>"Shut your mouth and keep your feet moving," Marcus panted, his voice cracking from thirst and inhaled ash. He adjusted his grip under her arms, his knuckles whitening. "If we drop the battery, the payload drives lose power. If the drives die, everything Kyle and the others died for is gone. We carry it all."</p>

        <p>He glanced down at his chest rig. The HUD display on his terminal deck was flashing a frantic, amber-lit warning pulse: <em>EXTERNAL TELEMETRY SYNC ACTIVE // HEART RATE: 158 BPM // BLOOD PRESSURE: 80/45 // CRITICAL FLUID LOSS</em>. She was slipping into deep hypovolemic shock, her skin turning an eerie, translucent gray under the desert sun.</p>
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

# PAGE 5 (Expanded Detail: The EMP Sacrifice and Going Dark)
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
        <p>A high, piercing chime trilled from Marcus's chest pouch. He froze, his boots sinking an inch into the crust. On the small OLED screen of his deck, a red geometric grid overlay had suddenly locked onto their exact coordinates, compressing from a regional sector down to a forty-meter kill box. The overhead satellite mesh had picked up Elena’s medical telemetry ping through her suit sensors.</p>

        <p>"They've got our signature," Marcus hissed, his heart hammering against his ribs. "The bio-monitor in your vest is broadcasting right to their low-earth relays."</p>

        <p>Without hesitation, Marcus unzipped his side pocket, pulled out a heavy copper grounding shunt, and jammed it straight across the primary circuit board’s capacitor bank. A sharp, violent crack of blue static snapped against his fingertips, burning his skin and filling the air with the sharp tang of fried silicon. The deck’s screen shuddered, fractured into vertical white lines of digital static, and went permanently black. Their maps, comms, and network tools died instantly. They were blind, deaf, and entirely cut off from the grid.</p>

        <p>"No comms," Marcus muttered, shoving the ruined hunk of metal back into his pouch. "No tracking. We're ghosts now. We walk straight toward the western horizon until we hit the ridge."</p>
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

# PAGE 6 (Expanded Detail: The Hours-Long Salt Crawl and Psychological Weight)
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
        <p>The next three hours became an unbroken nightmare of dirt, sweat, and agony. The sun descended toward the jagged western mountains, casting long, bruised shadows of violet and copper across the flat pan. Every step felt like lifting lead weights. Marcus’s shoulders were raw where the heavy straps of the payload case dug through his jacket, and his mouth tasted like copper and alkaline dust. Elena had stopped talking entirely; her weight had grown dead and uncooperative, her chin pressed against his chest as she drifted in and out of consciousness.</p>

        <p>He talked to her anyway—anything to keep the silence from swallowing them whole. He talked about code structures, about the old terminal rigs back in the eastern sector, about what they were going to do once the root certificate authority was purged. He knew she couldn't hear most of it, but the sound of his own voice kept his legs moving when every muscle fiber screamed to drop to the salt and quit.</p>

        <p>As the light began to fade into a harsh, metallic twilight, a dark irregularity broke the flat horizon ahead. A low, sunken concrete dome, half-buried in sand and ringed by rusted razor wire—the abandoned Titan II complex where Phoenix had gone to ground. But as they closed the final half-mile, the ground beneath their boots began to thrum with a deep, rhythmic vibration.</p>
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

# PAGE 7 (Expanded Detail: The Drone Sweep and Incoming Kinetic Strikes)
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
        <p>The machine hadn't lost them—it had simply cast a wider net, anticipating their destination. High above the darkening cloud layer, the whine of high-altitude turbine engines cut through the wind. Three automated tactical drones dropped out of the haze, their ventral targeting lasers painting the desert floor in bright crimson grids.</p>

        <p>"Get down!" Marcus shouted, pitching forward and dragging Elena off her feet into a shallow, eroded drainage ditch just as a blinding white flash erupted fifty yards to their left. A kinetic penetrator slammed into the salt pan with the roar of an artillery shell, turning tons of earth into a geyser of superheated slag and blinding white dust.</p>

        <p>The shockwave vaulted over them, scouring the brush and showering them in jagged gravel. Through the settling pall of smoke, Marcus looked up and saw their target: the heavy steel emergency personnel hatch at the base of the main silo dome. It was cracked open roughly four inches, a single blinking yellow strobe light marking the threshold in the gathering dark.</p>
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

# PAGE 8 (Expanded Detail: Crawling Through the Slag to the Hatch)
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
        <p>Marcus hauled Elena back onto her feet, his vision swimming with dark red spots. He half-carried, half-dragged her across the cratered concrete apron, their boots crunching over twisted rebar and smoking chunks of concrete. Another high-pitched acoustic whine signaled a second incoming projectile dropping from the drone swarm.</p>

        <p>"Grab the wheel!" Marcus screamed over the rising wind, shoving Elena’s hand onto the rusted manual override wheel of the blast door before throwing his entire body weight against the three-ton steel plate to crank it open on its jammed tracks.</p>

        <p>The heavy metal groaned, screeching in protest as it slid wide enough for a human body. From the pitch-black void inside the threshold, a pair of thick, scarred hands reached out through the gloom, grabbing Elena by her tactical vest and hauling her inward just as the second missile detonated against the outer apron.</p>
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

# PAGE 9
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
        <p>Marcus dove through the narrow gap behind her as the blast wave slammed the steel door shut with a concussive boom that rattled his teeth. He hit the cold diamond-plate catwalk hard, gasping for air that tasted of machine oil, stale coffee, and ancient hydraulic fluid.</p>

        <p>Above them, a massive, bearded man in a grease-stained canvas apron threw his full weight against a pneumatic locking lever. Heavy steel pins slammed into the doorframe with four resonant thuds, sealing the bunker off from the surface world. The silence inside was absolute, heavy, and suffocating.</p>

        <p>"You're late, Vance," a gravelly, unhurried voice rasped from the gloom. Phoenix stood over them, holding a heavy manual lever in one hand and a stained surgical clamp in the other.</p>
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

# PAGE 10
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
endif="True"
</html>"""

# Write all pages to disk
for p_num, content in pages.items():
    if p_num == 10:
        # Clean up weird pseudo-tag in page 10 string fix
        content = content.replace('endif="True"\n', '')
    filename = f"chapter-6-page-{p_num}.html"
    with open(filename, "w") as f:
        f.write(content)
    print(f"Successfully updated {filename}")

print("\nChapter 6 middle gap fully expanded and bridged!")
