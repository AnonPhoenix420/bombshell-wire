import os

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

def get_ch7_nav_block(current_page, total_pages=16):
    prev_link = f"chapter-7-page-{current_page - 1}.html" if current_page > 1 else "chapter-6-page-16.html"
    next_link = f"chapter-7-page-{current_page + 1}.html" if current_page < total_pages else "epilogue.html"
    
    prev_text = "← Prev" if current_page > 1 else "← Ch. 6"
    next_text = "Next Page →" if current_page < total_pages else "Epilogue →"

    buttons = []
    for i in range(1, total_pages + 1):
        if i == current_page:
            buttons.append(f'<span style="background: var(--terminal-green); color: #000; padding: 5px 8px; border-radius: 4px; font-family: monospace; font-weight: bold; font-size: 0.8rem;">P.{i}</span>')
        else:
            buttons.append(f'<a href="chapter-7-page-{i}.html" style="background: #21262d; color: var(--terminal-green); padding: 5px 8px; border: 1px solid var(--border-color); border-radius: 4px; text-decoration: none; font-family: monospace; font-size: 0.8rem; font-weight: bold;">P.{i}</a>')

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
        <p style="color: #8b949e; font-size: 0.8rem; font-family: monospace; margin-bottom: 8px;">CHAPTER 7 NAVIGATION (P.1 - P.16):</p>
        <div style="display: flex; gap: 5px; flex-wrap: wrap;">
          {''.join(buttons)}
        </div>
      </div>
    </div>
    """

ch7_contents = {
    1: ("The Caliche Flats", """
    <p>The desert didn't breathe; it radiated. By the time Marcus and Elena reached the perimeter of the abandoned Titan II complex, the midday heat had baked the air into a shimmering, distorting mirage that dissolved the horizon line into a wash of pale copper and white. Miles of rusted chain-link fence, topped with loops of razor wire choked in desert dust, marked the boundary of a military ghost town long since forgotten by the defense contractors who built it.</p>
    <p>Above them, the sky was a bruised, cloudless violet, sliced open by the faint, high-altitude glint of a low-earth-orbit surveillance platform passing silently overhead.</p>
    <p>Marcus dropped to one knee behind a sun-bleached concrete culvert, pulling his handheld terminal from his tactical rig. The casing was hot to the touch, baking under the ambient furnace of the Arizona panhandle. He tapped the physical key-matrix, bringing up a localized spectrum analyzer to check for active microwave sweeps.</p>
    <pre style="background: #0d1117; color: var(--terminal-green); padding: 12px; border: 1px solid var(--border-color); border-radius: 6px; font-family: monospace; font-size: 0.85rem; overflow-x: auto; margin: 1rem 0;"><code>[SCANNING: 2.4GHz - 18.0GHz BAND]
SRC: ORBITAL_SAT_108 [LGM-25C RECON GRID]
PWR: -41dBm [ACTIVE THERMAL SWEEP]
VEC: AZIMUTH 142.6 ELEVATION 68.2
STATUS: LOCK ACQUIRED // DISPERSAL IMMINENT</code></pre>
    <p>'They're painting the sector,' Marcus muttered, his voice dry and raspy against the wind. 'Thermal sweeps are running on a fifteen-minute loop. When that bird clears the ridge, we have a four-minute window before the automated drone patrol sweeps the fence line.'</p>
    """),

    2: ("The Vertical Drop", """
    <p>The heavy blast hatch groaned on its grease-caked hydraulic hinges, yielding to Marcus's pry bar with a sound like tearing sheet metal. A wall of stale, subterranean air rushed up to meet them—heavy with the dead weight of fifty-year-old hydraulic fluid, damp concrete, and absolute silence.</p>
    <p>Elena swung her legs over the rim of the access shaft, her weight shifting onto her left side. A sharp, involuntary intake of breath hissed through her teeth. The ragged entry wound on her right thigh—stitched hastily in the back of a salt-flat runner van with coarse nylon thread—strained against the pressure of her tactical trousers, leaving a dark, spreading crescent of fresh crimson soaking through the fabric.</p>
    <p>'I'm on the ladder,' she whispered, her voice bouncing off the cylindrical concrete walls of the descent tube. Her knuckles were stark white as she gripped the rusted rungs.</p>
    <p>'Don't push the leg,' Marcus muttered, dropping down behind her into the shaft and pulling the heavy steel lid halfway shut to block the desert glare.</p>
    """),

    3: ("The Descent into the Red", """
    <p>The descent down the primary utility shaft was a vertical eternity. Ninety feet of damp, vertical iron rungs bolted directly into the curved concrete spine of the silo. Below them, the emergency red glow of the primary atmospheric sensors cast long, skeletal shadows that stretched down into the dark abyss of the launch control center.</p>
    <p>Every time Elena dropped her right foot to the next rung, a shudder ran through her frame, her jaw clenched so tight the muscles ached. Marcus stayed one rung below her, his hands hovering just beneath her boots to catch her if the slick, condensation-slicked iron gave way.</p>
    <pre style="background: #0d1117; color: var(--terminal-green); padding: 12px; border: 1px solid var(--border-color); border-radius: 6px; font-family: monospace; font-size: 0.85rem; overflow-x: auto; margin: 1rem 0;"><code>[SUBSYSTEM DIAGNOSTIC: SHAFT_LEVEL_04]
AIR_TEMP: 14.2°C // HUMIDITY: 89%
OXYGEN_LEVEL: 18.4% [WARNING: SUB-OPTIMAL MIX]
RADIATION_SHIELDING: INTEGRITY 94% // ACTIVE</code></pre>
    <p>'Almost there,' Marcus murmured, looking down past the rusted safety cages into the cavernous control sphere below.</p>
    """),

    4: ("The Launch Control Sphere", """
    <p>They hit the grated catwalk at the base of the shaft, the metal ringing hollowly beneath their boots in the cavernous silence of the underground bunker. Through the gloom, a warm, pulsing amber glow cut through the red emergency strobes. It was Phoenix's domain—racks of heavy, exposed vacuum-tube hardware, their internal filaments glowing like dying campfires against the cold concrete walls.</p>
    <p>Phoenix stood over an iron workbench, a heavy soldering iron in one hand and a magnifying visor strapped across his forehead, surrounded by miles of braided copper wire and decommissioned radar components.</p>
    <p>'You brought the payload drives?' Phoenix rasped without looking up, his voice sounding like grinding gravel.</p>
    <p>'In the case,' Marcus panted, half-supporting Elena as her knees finally buckled against the steel grating.</p>
    """),

    5: ("The Diagnostic Burn", """
    <p>Phoenix didn't look up as Marcus half-carried Elena toward the makeshift medical cot in the corner. He simply reached out, snatched a roll of sterile gauze, and tossed it onto the metal table.</p>
    <p>'The silicon grid is dead weight out here,' Phoenix rasped, his eyes locking onto Marcus. 'The moment you crossed the valley floor, every packet-switched node between here and Flagstaff was burning under orbital surveillance probes. If you brought a modern server chip into this bunker, it would draw an ionized lightning bolt through the ceiling within twelve minutes.'</p>
    <p>He pointed a grease-stained finger at the glowing amber racks. 'We go analog. Or we don't go at all.'</p>
    """),

    6: ("The Vacuum-Tube Array", """
    <p>Marcus set the payload drives down onto the steel workbench with a heavy, metallic thud. He pulled a diagnostic oscilloscope from his pack, connecting its copper-mesh probes directly to the output terminals of the main vacuum-tube rack. The CRT screen flared to life, painting a steady, undulating green sine wave across the dust-flecked glass—clean, organic, and entirely untraceable by digital packet sniffers.</p>
    <pre style="background: #0d1117; color: var(--terminal-green); padding: 12px; border: 1px solid var(--border-color); border-radius: 6px; font-family: monospace; font-size: 0.85rem; overflow-x: auto; margin: 1rem 0;"><code>[ANALOG MESH: TUBE_BANK_04]
FREQ: 142.25 kHz [LF BAND]
MODULATION: AMPLITUDE_SHIFT [VHF MESH]
CARRIER_SIGNAL: STABLE // NO DIGITAL FOOTPRINT</code></pre>
    <p>'Carrier is clean,' Marcus breathed. 'No modulation leakage.'</p>
    """),

    7: ("Stitching the Flesh", """
    <p>While Marcus calibrated the carrier frequency, Phoenix sliced open Elena's tactical trousers with heavy trauma shears. The air in the bunker instantly filled with the sharp, coppery tang of stale blood and antiseptic. The improvised tourniquet had held, but the tissue around the wound was swollen and dark.</p>
    <p>'The aluminum shard missed the femoral artery by less than a millimeter,' Phoenix muttered, his hands moving with steady, surgical precision as he pulled a curved needle through the torn flesh.</p>
    <p>Elena didn't scream; she bit down hard on a strip of rubber tubing, her knuckles turning bone-white as the stitches drew the torn muscle together in the red strobe light.</p>
    """),

    8: ("The Blind Handshake Protocol", """
    <p>With Elena stabilized on the cot, Marcus turned his attention back to the primary console. To punch through the orbital jamming grid, they couldn't broadcast a standard TCP/IP handshake. They had to construct a cascading analog frequency hop—bouncing raw electrical pulses through the abandoned military telephone lines buried deep beneath the Arizona caliche.</p>
    <p>He wired a heavy copper jumper cable from the vacuum-tube oscillator directly into the silo's legacy hardline trunk, his fingers flying across the rotary dial as he punched in the cold-war bootstrap sequence.</p>
    <p>The vacuum tubes hummed in unison, their internal glass envelopes growing hot to the touch as they drew massive surges of raw current from the bunker's emergency diesel generators.</p>
    """),

    9: ("The Resonance Lock", """
    <p>The green sine wave on the oscilloscope tightened, spiking into a sharp, resonant harmonic peak that filled the room with a steady, high-pitched audio whine.</p>
    <pre style="background: #0d1117; color: var(--terminal-green); padding: 12px; border: 1px solid var(--border-color); border-radius: 6px; font-family: monospace; font-size: 0.85rem; overflow-x: auto; margin: 1rem 0;"><code>[TRANSMISSION STATUS: BLIND_HANDSHAKE]
CARRIER_LOCK: 99.4% [ANALOG MESH ACTIVE]
TARGET_NODE: PHOENIX_REGIONAL_RELAY_02
PACKET_LOSS: 0.00% [ISOLATED HARDLINE]</code></pre>
    <p>'We're locked into the hardline trunk,' Marcus whispered, wiping sweat from his forehead. 'If this holds, we can push the entire payload archive across the state border without a single digital trace hitting an active router.'</p>
    """),

    10: ("The Above-Ground Thunder", """
    <p>Before Phoenix could answer, a low, visceral thrum vibrated straight through the concrete floor up into the soles of their boots. The overhead fluorescent emergency tubes didn't just flicker—they detonated in a chain-reaction shower of glass sparks, plunging the control room into the hypnotic, frantic sweep of red emergency strobes.</p>
    <p>Above them, millions of tons of reinforced bedrock shuddered. The orbital directed-energy platform had painted the silo's surface coordinates. The ceiling groaned, raining a fine, suffocating powder of pulverized concrete dust down over the vacuum-tube racks as the first kinetic shockwave hit the bunker doors.</p>
    """),

    11: ("The Conduit Cascades", """
    <p>'They found the thermal vent!' Phoenix roared over the deafening roar of shifting earth and groaning steel. He threw his weight against a heavy manual circuit breaker, attempting to isolate the auxiliary power banks before an electrical surge fried the analog mesh.</p>
    <p>A cascade of thick, yellow-jacketed cables overhead snapped under the structural shear, whipping through the air like live copper serpents and showering white-hot electrical sparks across the metal grating.</p>
    <p>Marcus lunged across the console, his hands shielding the open oscillator as a heavy chunk of concrete ceiling fell three feet away, smashing the primary diagnostic monitor into a million glittering shards.</p>
    """),

    12: ("Holding the Needle", """
    <p>Despite the destruction, the analog oscilloscope held its green lock. The needle on the frequency dial remained pinned hard against the target frequency as the data stream pulsed down the legacy telephone lines.</p>
    <p>'Packet 402 clearing the trunk!' Marcus shouted, his eyes bloodshot and stinging from the concrete dust filling the air. 'The handoff to the regional relay is executing!'</p>
    <p>Elena pulled herself up onto one elbow from the medical cot, her hand gripping her bandaged thigh as she watched the data transfer indicator blink a steady, reassuring amber.</p>
    """),

    13: ("The Final Packet", """
    <p>'Don't let the carrier drop,' she rasped, her voice cutting through the groaning concrete above. 'If the resonance shifts by even half a hertz, the orbital receiver will snap back onto our frequency.'</p>
    <p>Marcus kept his thumb locked firmly down on the manual calibration potentiometer, feeling the vibration of the vacuum tubes humming against his fingertips like a living heartbeat.</p>
    <p>The transmission progress bar ticked forward: 94%... 98%... 99%...</p>
    """),

    14: ("The Direct Strike", """
    <p>At 99.9%, the ceiling above the control room exploded inward. A kinetic penetrator punched clean through three hundred feet of reinforced concrete and earth, detonating just fifty yards away in the lower equipment bay in a blinding flash of white thermal fury.</p>
    <p>The concussive blast picked Marcus and Phoenix off their feet, hurling them across the control room into a rack of spare vacuum tubes that shattered in a cascade of delicate glass.</p>
    <p>The air instantly turned to superheated steam and choking gray smoke, suffocating and thick with the reek of vaporized lead and burnt insulation.</p>
    """),

    15: ("The Dark Transmission", """
    <p>Through the ringing in his ears and the blinding red strobe lights, Marcus crawled back to the console on hands and knees. The screen was completely dead, charred black by the thermal back-blast.</p>
    <p>He stared frantically at the status indicator LED on the hardline trunk interface. For one agonizing second, it flickered dark. Then, with a soft, mechanical click, it flashed solid green.</p>
    <p>Complete. The data archive had cleared the silo boundary and vanished into the analog wilderness before the secondary blast could seal the vault forever.</p>
    """),

    16: ("The Vault Seals", """
    <p>Phoenix grabbed Marcus by the tactical vest, hauling him upright as massive hydraulic emergency pins slammed home into the silo's primary blast door with an earth-shaking, resonant thud that locked the subterranean tomb away from the burning world above.</p>
    <p>They stood in total darkness, broken only by the dim, dying amber glow of a single unblasted vacuum tube cooling slowly in the rack.</p>
    <p>The network was dark. The loop was broken. They were alive in the deep earth.</p>
    <div style='margin-top: 2rem; padding: 1.5rem; background: #161b22; border: 1px solid var(--terminal-green); border-radius: 8px;'><h3 style='color: var(--terminal-green); margin-bottom: 0.5rem; font-family: monospace;'>OPERATIONAL ARC COMPLETE</h3><p style='color: #8b949e; font-size: 0.9rem; margin-bottom: 1rem;'>Chapter 7 complete. The Phoenix Protocol successfully executed.</p><a href='epilogue.html' class='nav-btn' style='background: var(--terminal-green); color: #000; font-weight: bold; text-decoration: none; display: inline-block; padding: 10px 16px; border-radius: 4px;'>PROCEED TO EPILOGUE →</a></div>
    """)
}

for p_num, (subtitle, body_content) in ch7_contents.items():
    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter 7: The Phoenix Protocol - Page {p_num} | The Voltage and the Void</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
{site_header}
  <main>
    <article class="card story-container">
      <div class="story-header">
        <span class="chapter-tag">CHAPTER 7 • PAGE {p_num} OF 16</span>
        <h1>The Phoenix Protocol</h1>
        <p class="story-subtitle">{subtitle}</p>
      </div>

      {get_ch7_nav_block(p_num, 16)}

      <div class="story-body">
        {body_content}
      </div>

      <div class="story-nav" style="margin-top: 2rem;">
        <a href="chapter-7-page-{p_num-1}.html" class="nav-btn">← Prev</a>
        <a href="phantom-index.html" class="nav-btn">Master Index</a>
        <a href="chapter-7-page-{p_num+1}.html" class="nav-btn next-btn">Next Page →</a>
      </div>
    </article>
  </main>
</body>
</html>"""
    
    filename = f"chapter-7-page-{p_num}.html"
    with open(filename, "w") as f:
        f.write(page_html)
    print(f"Generated heavyweight 16-page build for {filename}")

print("\nAll 16 pages of Chapter 7 successfully generated!")
