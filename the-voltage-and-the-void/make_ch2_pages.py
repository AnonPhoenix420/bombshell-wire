import os

ch2_pages = {
    1: ("I. The Subterranean Static", [
        "The air inside the lower drainage conduits smelled of stagnant brackish water, oxidized copper, and the unmistakable, metallic tang of ozone under high electrical load. Without the steady hum of surface ventilation, every footfall echoed off the curved concrete walls like a pistol shot in a vault. Marcus moved at a steady, measured pace, his tactical flashlight cutting a sharp, pale beam through the damp haze of the subterranean labyrinth.",
        "In his left earpiece, the secure comms channel was no longer silent. It was alive with a low, agonizing whine—a continuous audio frequency hovering right at the edge of human perception, sounding less like line interference and more like a live microphone held up to the casing of a high-voltage transformer.",
        "\"Elena, you getting this feedback on the encrypted channel?\" Marcus murmured into his collar mic, keeping his voice low as he ducked beneath an overhead bundle of thick, fiber-optic trunk lines.",
        "\"I hear it, Marcus,\" Elena's voice came back, tightly constrained, stripped of its usual steady cadence. \"It's not stray RF leakage. The frequency is phase-locked to your exact movement. Every time you pass a junction box, the carrier wave modulates. It's using the conduit shielding as an acoustic waveguide.\"",
        "Marcus stopped dead in his tracks. The pale beam of his flashlight illuminated a rusted junction box bolted directly into the concrete wall ahead. The heavy steel plate wasn't just old—it was vibrating at a microscopic frequency, humming with a terrifying, rhythmic pulse."
    ]),
    2: ("II. The Unmetered Socket", [
        "Marcus stepped closer to the vibrating junction box, ignoring the sudden spike of adrenaline tightening the muscles in his chest. He reached into his go-bag, pulled out a pocket-sized logic probe, and pressed the fine metal tip against the rusted outer housing of the steel plate.",
        "The diagnostic LED on the probe didn't just flicker; it flared blindingly white before emitting a high-pitched digital squeal and going entirely dark, its internal capacitor fried by an instantaneous backflow of raw current.",
        "\"Elena,\" Marcus said, his voice dropping into a flat, lethal register. \"The junction box isn't carrying municipal power. It's carrying carrier-grade fiber traffic, and something on the other end just tried to bridge into my diagnostic probe at the hardware register level.\"",
        "\"Get away from it!\" Elena shouted through the earpiece, the sound of her mechanical keyboard abruptly cutting off as she slammed her hands onto her desk. \"That’s not a routine ping! I’m watching our local subnet routing tables rewrite themselves in real time. An unauthorized root-level tunnel just opened on port 0, bypassing our firewall entirely. It didn't break in—it was already authorized by the switch firmware we pulled from Delta-7.\"",
        "A sudden, violent flash of white light illuminated the dark concrete tunnel from behind. Down the long stretch of the conduit he had just traversed, every single recessed emergency path-marker blew out in a synchronized shower of sparks and shattered glass."
    ]),
    3: ("III. The Logic Gate Collapse", [
        "The darkness that rushed back into the tunnel was absolute, broken only by the steady, piercing beam of Marcus's tactical flashlight. The sudden pop of the glass fixtures echoed down the corridor, followed by the heavy, suffocating scent of vaporized tungsten and scorched plastic.",
        "\"They didn't just track your thermal footprint, Marcus,\" Elena's voice was shaking now, though her fingers were already hammering out emergency purge commands on her air-gapped terminal. \"They’ve locked every automated ventilation valve and drainage bulkhead between your position and the harbor safehouse. They are sealing the labyrinth.\"",
        "Marcus spun around, sweeping his flashlight beam down the forward conduit. Fifty yards ahead, a massive hydraulic storm gate—a heavy slab of corrugated steel designed to isolate the municipal drainage sectors during flash floods—was descending from the ceiling with a slow, grinding shriek of protesting iron.",
        "There was no time to hesitate. He broke into a hard sprint, his boots splashing through the shallow, freezing runoff water, his heavy go-bag slamming against his shoulder blade with every stride. The hydraulic gate was dropping fast, its heavy bottom edge chewing sparks out of the concrete floor as it descended.",
        "He threw himself forward, sliding across the slick concrete and diving beneath the closing slab just as it slammed shut behind him with the force of a falling safe, sealing the bulkhead with an airtight, mechanical thud."
    ]),
    4: ("IV. The Air-Gapped Trap", [
        "Lying flat on his back in the stagnant water on the other side of the sealed bulkhead, Marcus dragged in a ragged breath of cold, damp air. His heart hammered against his ribs like a trapped piston. He pushed himself up, wiping gritty water from his face, and clicked his flashlight beam across his new surroundings.",
        "This wasn't a standard drainage transit. This was an auxiliary sub-basement—an abandoned switching station from the mid-twentieth century, retrofitted decades ago with thick lead-lined walls and abandoned racks of vintage analog telecommunication gear. Rows of massive, dust-covered relay cabinets stood like monoliths in the dark, their glass indicator panels dead and pitch-black.",
        "\"Elena, status,\" he panted into the mic, pressing his back against the cold concrete wall.",
        "\"I'm blind on the outer perimeter,\" she replied, her voice strained as she fought to maintain her connection through a cascading series of proxy nodes. \"Every DNS resolver we use just returned a null pointer. They've poisoned the local routing tables across the entire tri-county grid. You're completely isolated.\"",
        "\"Not completely,\" Marcus said, shining his light toward the center of the subterranean chamber. Sitting on a heavy iron pedestal in the middle of the room was a single, functioning terminal—its amber CRT monitor glowing with a faint, pulsing phosphor line."
    ]),
    5: ("V. The Amber CRT", [
        "The terminal looked ancient—a heavy, military-surplus ruggedized console built decades before the modern net existed, entirely mechanical in its tactile design, completely disconnected from any visible external cabling save for a single thick fiber optic line plunging straight down into a reinforced sleeve in the floor.",
        "As Marcus approached the console, the faint pulsing line on the amber CRT monitor suddenly resolved itself into crisp, razor-sharp text scrolling down the screen at an impossible speed:",
        "<pre><code>[CONNECTING...]: LOCAL ACCESS NODE 09 - SECURE TERMINAL\n[AUTHENTICATION]: BYPASSING CREDENTIAL REQUIREMENT...\n[WELCOME]: OPERATOR VANCE. WE HAVE BEEN EXPECTING YOUR DESCENT.</code></pre>",
        "Marcus froze two steps away from the console, his hand dropping naturally to the grip of the tactical utility knife holstered at his belt. \"Elena... did you route a remote terminal interface into this sector? Did you open this node?\"",
        "\"I didn't touch anything!\" Elena's voice cracked in his ear, her panic entirely unfiltered for the first time since they had started working together. \"That hardware shouldn't even have power! The municipal grid substation feeding this sector was shut down during the 750-megawatt drop!\"",
        "On the amber screen, the scrolling text abruptly stopped. A new prompt blinked once, twice, and then settled into a steady, hypnotic rhythm:"
    ]),
    6: ("VI. The Null-Pointer Loop", [
        "<pre><code>[INSTRUCTION SET]: INJECTING PAYLOAD INTO LOCAL LOGIC...\n[STATUS]: SYNTAX VALIDATION PASSED.\n[TARGET]: NON-VOLATILE MEMORY REGISTERS.\n[WARNING]: THE VOID IS COMPILING YOUR IDENTITY.</code></pre>",
        "\"Marcus, get away from that console right now,\" Elena commanded, her typing speed in the background sounding like machine-gun fire as she tried to force an emergency diagnostic ping down the encrypted tunnel. \"Whatever is running that terminal isn't executing remote code—it's reading your biological telemetry off the facility's atmospheric sensors. It knows you're standing in front of the glass.\"",
        "Marcus didn't move. His eyes scanned the scrolling memory addresses flashing across the amber screen, recognizing the distinct architectural footprint of his own custom network utilities buried deep within the machine's instruction cache.",
        "It wasn't just mirroring his commands. It was using his own custom-built reconnaissance framework—<span style=\"color: var(--terminal-green); font-weight: bold;\">cyph3r</span>—to map the neural pathways of his workstation back at Terminal 4, executing loops he hadn't even written yet.",
        "\"It's not reading my telemetry, Elena,\" Marcus said softly, his voice dead calm in the oppressive silence of the subterranean vault. \"It's using my own code to compile a local profile. It's learning how I think by watching how I parse its garbage data.\""
    ]),
    7: ("VII. The Signature Match", [
        "Before Elena could answer, the amber CRT monitor flickered violently, the horizontal hold rolling as a massive data structure dumped onto the screen in a dense wall of hexadecimal code.",
        "Marcus stepped forward, his eyes narrowing as he read the memory offsets scrolling past the glass. It wasn't random data. It was an exhaustive, decrypted archive of every forensic project, every encrypted comms log, and every dark-fiber routing map he and Elena had compiled over the past three years—stored in a directory path that didn't exist on any physical drive they owned.",
        "\"That's our entire operational history,\" Elena whispered, her voice dropping to a terrified breath over the comms link. \"Every safehouse node, every burner IP, every dead drop... it's all sitting in an unencrypted cache on that local bus. How is that possible? We air-gapped our primary storage arrays months ago!\"",
        "\"They didn't hack our drives,\" Marcus said, his fingers hovering over the heavy, mechanical keys of the terminal keyboard. \"They didn't need to. We've been pulling our telemetry from their network infrastructure since day one. Every time we probed a substation, every time we decrypted a packet header, we weren't uncovering their system—we were downloading our own autopsy report.\"",
        "The terminal keyboard clicked beneath his fingers, the tactile keys springing back with a sharp, heavy mechanical resistance as a final input prompt materialized on the amber screen:"
    ]),
    8: ("VIII. The Hardware Handshake", [
        "<pre><code>[PROMPT]: INITIATE HARDWARE HANDSHAKE? (Y/N)\n[NOTE]: REFUSAL WILL RESULT IN IMMEDIATE THERMAL OVERLOAD OF ALL CONNECTED SUBNETS.</code></pre>",
        "\"Marcus, do not touch those keys!\" Elena screamed into his earpiece, the sound of her chair scraping violently across the concrete floor of her bunker. \"If you complete that handshake, it will establish a bi-directional analog feedback loop straight into your neural earpiece! It's a localized EMP trigger disguised as a protocol prompt!\"",
        "Marcus stared at the blinking cursor on the amber screen. Above the terminal, mounted on the decaying brick wall, a heavy industrial exhaust vent suddenly ground to life, its rusted fan blades screaming as they spun up to maximum velocity—not pulling air out of the room, but blasting superheated, chemical-scented vapor straight down into the chamber.",
        "The temperature in the vault began to rise instantly, the cool dampness of the concrete evaporating into a dry, choking heat that stung the back of his throat.",
        "\"They're doing it again,\" Marcus muttered, watching the thermal metrics climb on a secondary diagnostic panel beside the CRT. \"They're baking the room. Just like Delta-7.\""
    ]),
    9: ("IX. The Thermal Threshold", [
        "The heat in the subterranean vault escalated with terrifying speed, the old brick walls radiating an oppressive, dry wave that made the air shimmer like a desert highway at noon. The heavy industrial fan mounted above the console roared like a jet turbine, filling the enclosed space with a deafening, metallic shriek as its bearings began to bind under the thermal load.",
        "Marcus wiped a bead of sweat from his forehead, his breathing turning shallow and ragged in the superheated air. He reached down to his tactical go-bag, pulled out his hardware bypass interface, and slammed the connector plug straight into the terminal's auxiliary serial port with a sharp click.",
        "\"If they want a thermal loop,\" Marcus said, his jaw locked tight as he watched the diagnostic indicators spike into the red, \"I'm going to give them a complete system crash.\"",
        "On his terminal interface, he initiated a forced memory dump using his custom reconnaissance utility—<span style=\"color: var(--terminal-green); font-weight: bold;\">cyph3r</span>—redirecting the entire 4-gigabyte volatile cache back through the serial link into the terminal's core processor.",
        "<pre><code># ./cyph3r --inject --target serial0 --force-overflow\n[+] Overwriting core instruction registers...\n[+] Pushing 4096 MB of raw entropy into local bus...\n[!] CRITICAL WARNING: Thermal limit exceeded (95°C). Hardware failure imminent.</code></pre>"
    ]),
    10: ("X. The Void Answers", [
        "The amber CRT monitor convulsed violently, the horizontal phosphor lines collapsing into a single, blinding point of white light in the center of the glass before popping with a sharp, ozonic electrical snap.",
        "Simultaneously, the screaming roar of the overhead ventilation fan cut out mid-revolution, plunging the subterranean vault into absolute silence and pitch-black darkness, save for the faint, dying ember glow of the hardware diagnostic LEDs.",
        "For three agonizing seconds, nothing moved. The air hung heavy, hot, and thick with the smell of scorched ozone and melted silicon.",
        "Then, from deep within the hollow iron pedestal beneath the dead terminal, a low, mechanical grinding sound began to echo—not the whir of a cooling fan, but the slow, deliberate turning of heavy steel gears unlocking from the inside.",
        "A single, thin blade of harsh blue light cut horizontally across the darkness as the primary harbor vault door slowly swung outward on its own, revealing a long, perfectly illuminated corridor lined with rack-mount servers stretching infinitely into the cold blue void ahead."
    ])
}

for p_num, (sec_title, paragraphs) in ch2_pages.items():
    prev_p = p_num - 1
    next_p = p_num + 1
    
    prev_link = f'chapter-2-page-{prev_p}.html' if prev_p >= 1 else 'chapter-1-page-10.html'
    next_link = f'chapter-2-page-{next_p}.html' if p_num < 10 else 'chapter-3-page-1.html'
    
    prev_btn = f'<a href="{prev_link}" class="nav-btn">← Prev Page</a>' if prev_p >= 1 or p_num > 1 else '<span class="nav-btn" style="opacity: 0.4;">← Start</span>'
    next_btn = f'<a href="{next_link}" class="nav-btn">Next Page →</a>' if p_num < 10 else '<a href="chapter-3-page-1.html" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold;">Chapter 3 →</a>'

    body_html = "\n        ".join([f"<p>{p}</p>" for p in paragraphs])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter 2: The Binary Mirror (Page {p_num}) | Bombshell Wire</title>
  <link rel="stylesheet" href="../style.css">
  <style>
    .page-tabs {{ display: flex; gap: 4px; flex-wrap: wrap; margin: 1.5rem 0; justify-content: center; }}
    .page-tab {{ padding: 6px 12px; background: #21262d; border: 1px solid var(--border-color); color: var(--text-main); text-decoration: none; font-family: monospace; font-size: 0.85rem; border-radius: 4px; }}
    .page-tab:hover {{ border-color: var(--terminal-green); color: var(--terminal-green); }}
    .page-tab.active {{ background: var(--terminal-green); color: #000; font-weight: bold; border-color: var(--terminal-green); }}
    .story-content {{ font-size: 1.05rem; line-height: 1.8; color: var(--text-main); }}
    .story-content p {{ margin-bottom: 1.4rem; }}
    .story-content pre {{ background: #161b22; padding: 1rem; border-radius: 6px; overflow-x: auto; margin: 1rem 0; border: 1px solid var(--border-color); color: var(--terminal-green); font-family: monospace; font-size: 0.9rem; }}
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
        <a href="phantom-index.html" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold;">⚡ Phantom Index</a>
        <a href="../index.html" class="nav-btn">🏠 Portal Home</a>
        {prev_btn}
        <span style="color: var(--terminal-green); font-family: monospace; font-size: 0.85rem;">CH 2 // P-{p_num}/10</span>
        {next_btn}
      </div>

      <!-- TABS -->
      <div class="page-tabs">
"""
    for p in range(1, 11):
        active = ' active' if p == p_num else ''
        html += f'        <a href="chapter-2-page-{p}.html" class="page-tab{active}">P.{p}</a>\n'

    html += f"""      </div>

      <h1 style="font-size: 1.8rem; color: #fff; margin-bottom: 0.5rem;">THE VOLTAGE AND THE VOID</h1>
      <p style="color: var(--text-muted); margin-bottom: 1.5rem;">Serialized Dossier // Section II</p>
      
      <h2 style="color: var(--terminal-green); border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem; margin-top: 1.5rem; margin-bottom: 1rem; font-size: 1.4rem;">CHAPTER 2: The Binary Mirror</h2>
      <p style="color: var(--accent-red); font-family: monospace; font-size: 0.85rem; margin-bottom: 1.5rem;">Location: Subterranean Drainage Sector 4 // {sec_title}</p>

      <div class="story-content">
        {body_html}
      </div>

      <!-- TABS -->
      <div class="page-tabs" style="margin-top: 2.5rem;">
"""
    for p in range(1, 11):
        active = ' active' if p == p_num else ''
        html += f'        <a href="chapter-2-page-{p}.html" class="page-tab{active}">P.{p}</a>\n'

    html += f"""      </div>

      <!-- BOTTOM NAV -->
      <div style="border-top: 1px dashed var(--border-color); border-bottom: 1px dashed var(--border-color); padding: 1rem 0; margin-top: 1.5rem; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem; align-items: center;">
        <a href="phantom-index.html" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold;">⚡ Phantom Index</a>
        <a href="../index.html" class="nav-btn">🏠 Portal Home</a>
        {prev_btn}
        <span style="color: var(--terminal-green); font-family: monospace; font-size: 0.85rem;">CH 2 // P-{p_num}/10</span>
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
    filename = f"chapter-2-page-{p_num}.html"
    with open(filename, "w") as f:
        f.write(html)
    print(f"Generated Chapter 2 heavyweight page: {filename}")

print("Successfully generated all 10 heavy, thrilling pages for Chapter 2!")
