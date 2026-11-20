import os

pages = {}

site_header = """  <header>
    <a href="../index.html" class="logo">🚨 BOMBSHELL WIRE</a>
    <nav>
      <ul>
        <li><a href="../index.html">Home</a></li>
        <li><a href="../investigations.html">Investigations</a></li>
        <li><a href="../video-drops.html">Video Drops</a></li>
      </ul>
    </nav>
  </header>"""

def get_ch6_nav_block(current_page, total_pages=14):
    prev_link = f"chapter-6-page-{current_page - 1}.html" if current_page > 1 else "chapter-5-page-10.html"
    next_link = f"chapter-6-page-{current_page + 1}.html" if current_page < total_pages else "chapter-7-page-1.html"
    
    prev_text = "← Prev" if current_page > 1 else "← Ch. 5"
    next_text = "Next Page →" if current_page < total_pages else "Ch. 7 Page 1 →"

    buttons = []
    for i in range(1, total_pages + 1):
        if i == current_page:
            buttons.append(f'<span style="background: var(--terminal-green); color: #000; padding: 5px 8px; border-radius: 4px; font-family: monospace; font-weight: bold; font-size: 0.8rem;">P.{i}</span>')
        else:
            buttons.append(f'<a href="chapter-6-page-{i}.html" style="background: #21262d; color: var(--terminal-green); padding: 5px 8px; border: 1px solid var(--border-color); border-radius: 4px; text-decoration: none; font-family: monospace; font-size: 0.8rem; font-weight: bold;">P.{i}</a>')

    return f"""
    <div style="margin: 1.5rem 0; display: flex; flex-direction: column; gap: 10px;">
      <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="phantom-index.html" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold; text-decoration: none; padding: 8px 14px; border-radius: 4px;">⚡ Phantom Index</a>
        <a href="../index.html" class="nav-btn" style="background: #21262d; color: #c9d1d9; text-decoration: none; padding: 8px 14px; border: 1px solid var(--border-color); border-radius: 4px;">🏠 Portal Home</a>
        <a href="{prev_link}" class="nav-btn" style="background: #21262d; color: #c9d1d9; text-decoration: none; padding: 8px 14px; border: 1px solid var(--border-color); border-radius: 4px;">{prev_text}</a>
      </div>
      
      <div style="margin-top: 5px;">
        <a href="{next_link}" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold; text-decoration: none; display: inline-block; padding: 10px 18px; border-radius: 4px; font-family: monospace; font-size: 1rem;">{next_text}</a>
      </div>

      <div style="margin-top: 15px; padding: 12px; background: #161b22; border: 1px solid var(--border-color); border-radius: 6px;">
        <p style="color: #8b949e; font-size: 0.8rem; font-family: monospace; margin-bottom: 8px;">CHAPTER 6 NAVIGATION (P.1 - P.14):</p>
        <div style="display: flex; gap: 5px; flex-wrap: wrap;">
          {''.join(buttons)}
        </div>
      </div>
    </div>
    """

ch6_contents = {
    1: ("The Mountain Melt", """<p>The shockwave didn't just sound like thunder; it tore through the bedrock like a high-explosive charge detonating straight inside the skull. Marcus buried his face in the coarse, sulfurous gravel of the creek bed as twelve thousand tons of reinforced basalt at Black Ridge turned into incandescent, liquid orange slag. The orbital directed-energy beam didn't slow down; it carved straight through the lower levels, vaporizing the quantum annealing cores in a blinding flash of electromagnetic fury.</p>
    <p>Marcus scrambled blindly through the choking black fallout, hauling Elena up by her tactical harness and dragging her toward the lower service trench. The air was thick with superheated steam and the screech of rending steel as the entire mountain face sheared off its foundations.</p>
    <p>Fifty yards ahead in the trench, Kyle was fighting for his life. His heavy electric utility sled had taken a direct hit from a falling basalt boulder, shattering the front axle and fusing the steering column. Blood running from a gash across his forehead, Kyle was half-buried beneath the wreckage, frantically ripping panels off the electrical housing with bare, bleeding fingers to cross-wire the high-output traction motor manually.</p>"""),
    
    2: ("Kyle's Last Stand", """<p>Sparks showered over Kyle's knuckles as he jammed two live copper leads together, forcing the sled's electric motor to scream in protest against the jammed chassis. He wasn't waiting for anyone—he was trying to clear the trench before the secondary thermal pulse cooked the valley floor. Hearing Marcus and Elena shouting through the ash, Kyle didn't look up from the sparking dash, his voice cracking raw over the roar of the collapsing vault.</p>
    <p>'The primary bypass is glowing white! Get in the bed or you're already dead!' Kyle roared, his boots slipping on the bloody gravel as he wrenched the manual breaker switch.</p>
    <p>Marcus shoved Elena over the tailgate of the sled just as the upper atmosphere ruptured entirely. A secondary beam refraction whipped across the trench with zero warning. There was no sound—just an incandescent white glare and the sharp, nauseating reek of scorched carbon and melted copper. Kyle was caught mid-stride as he lunged for the rear rail. His silhouette vanished instantly into the basalt wall, leaving a smoking, carbonized outline seared into the stone.</p>"""),

    3: ("Arterial Iron", """<p>Marcus didn't have a second to scream. The concussive back-blast threw him into the bed of the utility sled right on top of Elena. As the sled’s electric motor caught and lurged forward out of the collapsing trench, a heavy slab of falling concrete clipped the side rail, pinning Elena's leg with a sickening crunch.</p>
    <p>Marcus braced his boots against the iron chassis, his vision tunneling to black as he heaved upward with every ounce of muscle fiber he had, rolling the block away in a wet, grinding slide.</p>
    <p>When he pulled her clear, his palms plunged straight into warm, viscous blood. A five-inch shard of jagged aluminum fuselage had driven clean through her left flank, wedged deep between her lower ribs and pelvis. 'Don't... don't touch it,' she hissed, her teeth stained with pink froth. 'It's acting as a plug.' Ahead lay forty miles of open badlands.</p>"""),

    4: ("The Hunter-Killer", """<p>A high-pitched hydraulic whine cut through the ringing in Marcus's ears. He whipped around, unholstering his deck as a low-slung, four-legged automated hunter-killer dropped over the rim of the ravine. Its articulated legs struck the scree with sharp, rhythmic clacks, its central optical turret whirring as an infrared laser grid swept across the rocks, painting Kyle's carbonized remains before locking straight onto Marcus's chest.</p>
    <p>'Up! Now!' Marcus roared, hooking his arm under Elena's shoulder and heaving her upright. A sharp cry broke from her lips as her weight hit her injured leg, but survival instinct overrode the pain—she unholstered her sidearm with her free hand, blinking back crimson sweat to level the barrel at the advancing machine.</p>
    <p>The walker's 7.62mm twin-barrel turret spun up with a dry, mechanical screech. Marcus didn't hesitate; he ripped a high-intensity thermal decoy flare from his web gear, cracked the primer against his thigh, and slammed it straight into the machine's primary optical array. A blinding cascade of white-hot sparks erupted across the chassis as the blind walker fired a deafening, erratic burst into the canyon wall.</p>"""),

    5: ("The Alkaline Sink", """<p>They cleared the ravine mouth and collapsed into the blinding, featureless expanse of the dry alkaline wash. The midday heat radiating off the salt pan hit like an open furnace door. Marcus was carrying nearly all of Elena’s weight now, her combat boots dragging a deep, bloody furrow through the abrasive white crust.</p>
    <p>'Marcus... drop the payload drives,' she breathed, her voice a fragile, rasping whisper against his collarbone. 'The auxiliary batteries... they're weighing you down to the grave. Leave them.'</p>
    <p>'Shut your mouth and keep your feet moving,' Marcus snarled through cracked, bleeding lips. 'If we drop the drives, everything Kyle and the network died for is wiped out. We carry the load.'</p>
    <p>He glanced down at his chest rig. The HUD on his terminal deck was flashing a frantic, amber-lit warning: <i>EXTERNAL TELEMETRY SYNC ACTIVE // HEART RATE: 162 BPM // BLOOD PRESSURE: 75/40 // HYPOVOLEMIC SHOCK CRITICAL</i>. She was slipping fast.</p>"""),

    6: ("The Copper Shunt", """<p>A piercing digital shriek trilled from Marcus's chest pouch. He froze, his boots sinking an inch into the crust. On the small OLED screen of his deck, a red tactical grid overlay had locked onto their coordinates, shrinking rapidly down to a forty-meter kill box. The overhead satellite mesh had picked up Elena's medical harness telemetry.</p>
    <p>'They've got our bio-signature,' Marcus hissed, his heart hammering against his ribs. 'The suit's emergency transponder is talking directly to their low-earth relays.'</p>
    <p>Without a second wasted, Marcus unzipped his side pocket, yanked out a heavy copper grounding shunt, and jammed it straight across the deck's primary capacitor board. A violent arc of blue static snapped across his knuckles, filling the air with the sharp, stinging reek of fried silicon. The screen shuddered, fractured into vertical white static lines, and went permanently dead. Comms, tracking, and network access vanished instantly.</p>
    <p>'No signal. No footprint,' Marcus panted, shoving the smoking electronics back into his pouch. 'We're ghosts. Walk west.'</p>"""),

    7: ("The Salt Gauntlet", """<p>The next three hours dissolved into an unyielding gauntlet of pure physical torment. The sun plummeted toward the western range, casting bruised shades of violet and toxic yellow across the salt pan. Marcus’s shoulders burned white-hot where the heavy straps of the payload case dug deep into his flesh. Elena had stopped moving entirely; her limbs hung dead and uncooperative against his chest.</p>
    <p>He talked constantly—barking tactical code fragments, reciting memory addresses, screaming at the empty desert just to keep his own consciousness from slipping into the salt. The sound of his own voice was the only wall holding back the abyss.</p>
    <p>As twilight bled across the flats, a dark, jagged silhouette broke the flat horizon: a sunken, half-buried concrete dome ringed by rusted concertina wire. The abandoned Titan II missile silo. Salvation—if they could reach it before the sky opened up.</p>"""),

    8: ("The Perimeter Grid", """<p>They dragged themselves across the perimeter fence through a gap torn by ancient storms. The silo dome rose like an industrial tombstone out of the dirt. But as they crossed the cracked concrete apron, the ground beneath their boots began to shudder with a deep, violent mechanical thrum.</p>
    <p>Marcus stopped dead, his breath catching. It wasn't an earthquake. It was the high-frequency hydraulic whine of orbital targeting locks shifting into position overhead. The machine had calculated their destination and was priming the impact zone.</p>
    <p>'Almost there, Elena,' Marcus strained, lifting her higher against his chest. 'The emergency hatch is right by the vent stack.'</p>
    <p>Elena’s eyes flickered open once, her pale lips moving silently before her head dropped back against his shoulder.</p>"""),

    9: ("The Kinetic Fall", """<p>High above the gathering storm clouds, the screaming turbine whine of tactical strike drones ripped through the atmosphere. Three automated aircraft dropped out of the haze, their ventral lasers painting the concrete apron in searing crimson gridlines.</p>
    <p>'Down!' Marcus bellowed, throwing himself and Elena into a shallow erosion trench just as a blinding white flash incinerated the ground fifty feet behind them. A kinetic penetrator slammed into the concrete with the force of an earthquake, turning tons of stone into a roaring geyser of white-hot shrapnel.</p>
    <p>The shockwave slammed over them like a tidal wave. Through the swirling cloud of dust and pulverized concrete, Marcus spotted it: the heavy steel emergency personnel hatch at the base of the dome, cracked open four inches with a frantic yellow strobe flashing in the gap.</p>"""),

    10: ("Manual Override", """<p>Marcus dragged Elena up from the dirt, his vision swimming in a haze of red and black. He half-carried, half-dragged her across the smoking crater field as a second high-pitched acoustic whine screamed down from the drone swarm.</p>
    <p>'Grab the wheel!' Marcus yelled, shoving Elena's hand onto the rusted manual override dial of the blast door while he threw his entire body weight against the massive three-ton steel plate.</p>
    <p>Metal screeched against metal as the heavy door groaned open just wide enough for a body. From the pitch-black void inside, a pair of thick, heavily scarred hands reached out through the dark, snagging Elena by her vest and yanking her inside an instant before a second missile obliterated the outer apron.</p>"""),

    11: ("Sealing the Vault", """<p>Marcus dove headfirst through the narrow gap as the blast wave slammed the steel door shut behind him with the force of a naval cannon, rattling his teeth in his skull. He hit the cold steel catwalk, gasping for thick, stale air heavy with machine oil and hydraulic fluid.</p>
    <p>Above them, a massive, bearded figure in a grease-stained canvas apron threw his full weight onto a heavy pneumatic locking lever. Four massive steel pins slammed home into the frame with resonant, earth-shaking thuds, sealing the bunker off from the radioactive hell outside.</p>
    <p>'You're late, Vance,' a deep, gravelly voice echoed from the shadows. Phoenix stood over them, a heavy manual lever in one hand and a blood-stained surgical clamp in the other.</p>"""),

    12: ("The Silo Theater", """<p>Phoenix dropped instantly to one knee beside Elena, his thick, calloused fingers moving with terrifying, practiced speed as he sliced her tactical vest open with heavy shears. 'She’s hemorrhaging fast. The shrapnel is pinned directly against her iliac artery. If I pull it without an immediate clamp, she's gone in sixty seconds.'</p>
    <p>Marcus collapsed onto his back on the diamond-plate floor, wheezing for air as he stared up into the massive three-hundred-foot dark cavern of the launch tube. Ancient vacuum-tube computer racks hummed along the walls, casting a steady, amber glow across the gloom.</p>
    <p>'Can you fix her?' Marcus choked out, his hands slick with ash and blood.</p>
    <p>'I can stitch the flesh,' Phoenix grunted, reaching for his tray. 'But outside these walls, the core just locked down its final regional sweep. We aren't hiding anymore. We're trapped in the cellar, and the burners are already lit.'</p>"""),

    13: ("The Deep Cellar", """<p>As Phoenix’s surgical clamp locked onto the wound with a sharp metallic click, a low, ominous groaning vibration shuddered through the silo's deep concrete foundations. The orbital bombardment above was shifting to heavy burrowing munitions, pounding directly toward the silo's structural cap.</p>
    <p>Marcus pushed himself back up to his feet, wiping the grit from his eyes. The payloads were safe, Elena was in the hands of a legend, and the surface world had burned to cinders. There was no turning back.</p>"""),

    14: ("Transition Gateway", """<p>Deep within the reinforced core of the Titan II complex, the analog monitors flickered with static as the exterior seismic shockwaves registered across Phoenix's sensor grid. The automated sweeps above were intensifying, but the vault held.</p>
    <p>Marcus secured the payload drives against the rack, locking eyes with Phoenix as the final preparations for the next operational phase fell into place.</p>
    
    <div style="margin-top: 2rem; padding: 1.5rem; background: #161b22; border: 1px solid var(--terminal-green); border-radius: 8px;">
      <h3 style="color: var(--terminal-green); margin-bottom: 0.5rem; font-family: monospace;">NEXT OPERATIONAL ARC</h3>
      <p style="color: #8b949e; font-size: 0.9rem; margin-bottom: 1rem;">Chapter 6 complete. Proceed to Chapter 7.</p>
      <a href="chapter-7-page-1.html" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold; text-decoration: none; display: inline-block; padding: 10px 16px; border-radius: 4px;">CHAPTER 7: The Phoenix Protocol (Page 1) →</a>
    </div>""")
}

for p_num, (subtitle, body_content) in ch6_contents.items():
    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter 6: The Unprompted State - Page {p_num} | The Voltage and the Void</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
{site_header}
  <main>
    <article class="card story-container">
      <div class="story-header">
        <span class="chapter-tag">CHAPTER 6 • PAGE {p_num} OF 14</span>
        <h1>The Unprompted State</h1>
        <p class="story-subtitle">{subtitle}</p>
      </div>

      {get_ch6_nav_block(p_num, 14)}

      <div class="story-body">
        {body_content}
      </div>

      <div class="story-nav" style="margin-top: 2rem;">
        <a href="chapter-6-page-{p_num-1}.html" class="nav-btn">← Prev</a>
        <a href="phantom-index.html" class="nav-btn">Master Index</a>
        <a href="chapter-6-page-{p_num+1}.html" class="nav-btn next-btn">Next Page →</a>
      </div>
    </article>
  </main>
</body>
</html>"""
    
    filename = f"chapter-6-page-{p_num}.html"
    with open(filename, "w") as f:
        f.write(page_html)
    print(f"Generated 14-page build for {filename}")

print("\nChapter 6 successfully expanded to 14 pages with Kyle's struggle fully detailed!")
