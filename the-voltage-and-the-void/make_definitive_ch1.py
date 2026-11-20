import os

pages_data = {
    # --- PAGES 1 TO 5: THE ORIGINAL MASSIVE, UNTOUCHED SECTIONS ---
    1: ("I. The Anatomy of a Bleed", [
        "Silicon remembers heat long after the current is cut. When an integrated circuit—especially a high-density processing array designed for parallel cryptographic compute—is forced to run raw, unthrottled instructions past its thermal design power limit, the microscopic silicon pathways do not merely function. They warp. The atomic lattice expands under unrelenting thermal stress, microscopic copper interconnects stretch past their yield strength, and electrons begin to quantum-tunnel across gate oxides that are engineered to keep them strictly isolated.",
        "In forensic engineering literature, this phenomenon is dryly categorized as <em>electromigration</em> and <em>die-level thermal degradation</em>. In the underground circuit where Marcus Vance operated, it had a much simpler, uglier name: <em>the bleed</em>.",
        "The workbench in the center of Terminal 4 looked less like an engineering workspace and more like a forensic pathology lab for dead machinery. Three custom-built rack-mount server chassis had been stripped entirely of their brushed aluminum housing, leaving their internal motherboards naked to the harsh, flickering fluorescent glare of the room. A tangle of logic analyzer probes, oscilloscope leads, and multi-meter wires spread out from the central boards like spider silk, feeding live voltage telemetry into an array of secondary diagnostic displays.",
        "The air in the room smelled like hot dust, ozone, and burnt flux—the unmistakable signature of hardware pushed deliberately, cruelly past the edge of structural failure."
    ]),
    2: ("II. The Microscopic Fracture", [
        "Marcus sat hunched over a heavy-duty stereo microscope, his right hand gripping the fine-focus knob with microscopic precision. Beneath the glass lens lay a fried communication transceiver chip salvaged directly from Substation Delta-7’s shattered optical routing array.",
        "Under four hundred times magnification, the silicon wafer no longer resembled an engineered marvel of modern computation. It looked like a dried-up riverbed split by an intolerable, protracted drought. The micro-scale copper traces had not just broken; they had literally liquefied, flowing across the substrate like molten tar before freezing in place as the power failed, bridging circuits that were supposed to remain isolated for the entire operational lifecycle of the machine.",
        "\"You're chasing ghosts in a graveyard, Marcus,\" Elena's voice crackled through the secure, heavily encrypted comms earpiece resting in his left ear.",
        "She was stationed across the city in a windowless commercial basement she called the \"Bunker,\" surrounded by her own bank of glowing multi-monitor displays. Through the audio link, Marcus could hear the faint, rhythmic clatter of her mechanical keyboard—a high-speed clatter that never seemed to slow down, even when she was speaking."
    ]),
    3: ("III. The Architecture of the Override", [
        "\"Whatever hit Delta-7 wasn't a standard botnet payload,\" Elena continued, her voice tight with suppressed adrenaline. \"I’ve been running deep signature analysis on the packet headers you dumped from the field terminal. The routing profiles don't use TCP/IP. They don't even use UDP or raw Ethernet frames. It’s rewriting the firmware stack of the switching chips at the physical hardware register level. It’s translating machine language straight into analog wave frequency.\"",
        "Marcus didn’t answer immediately. He adjusted the microscope focus slightly, watching the fractured silicon geometry shift into view under the harsh halogen ring-light.",
        "\"It's not just rewriting the firmware, Elena,\" Marcus said, his voice dropping an octave, dead flat and devoid of panic. \"Look at the thermal signature logs from the substation's primary cooling fans before they cut out.\"",
        "On the secondary monitor to his left, a multi-spectral heat map bloomed into vibrant life, rendering the internal environment of the substation's transformer housing in harsh, bleeding gradients of crimson and white."
    ]),
    4: ("IV. Thermal Inversion", [
        "\"I'm looking at it,\" Elena replied, her typing pausing for a fraction of a second. \"The cooling arrays spun down. That’s normal for a total grid fault, right? Loss of auxiliary station service power?\"",
        "\"No,\" Marcus said, tapping the edge of the microscope frame with his fingernail. \"Look closer at the fan motor telemetry. They didn't spin down because they lost power. They were commanded to reverse polarity. For twenty-two minutes prior to the 750-megawatt drop, the control logic intentionally drove the exhaust fans in reverse—pumping hot ambient desert air into the server racks instead of pulling it out.\"",
        "A heavy silence hung over the comms link for three agonizing seconds as the implications settled across the digital divide.",
        "\"They baked it,\" Elena whispered.",
        "\"They baked it,\" Marcus confirmed. \"Someone wanted those chips to reach their glass transition temperature. They forced the silicon into an unstable thermal state where digital logic breaks down entirely, blurring the line between binary code and analog noise.\""
    ]),
    5: ("V. The Forensic Terminal", [
        "Marcus pulled his eye away from the microscope lens, rubbing a hand across his tired face. His eyes were bloodshot, burning from twenty hours of continuous screen glare and the dry, recycled air of the terminal room.",
        "He reached out and tapped a command into his primary workstation terminal, bringing up the hex dump recovered from the volatile memory cache of the dying transceiver chip he had pulled from the substation floor.",
        "<pre><code># hexdump -C -n 512 /mnt/usb/dump.raw\n00000000  4f 70 65 72 61 74 6f 72  20 49 73 20 4f 62 73 65  |Operator Is Obse|\n00000010  72 76 69 6e 67 20 54 68  65 20 56 6f 69 64 2e 20  |rving The Void. |\n00000020  54 68 65 20 56 6f 69 64  20 49 73 20 43 6f 6d 70  |The Void Is Comp|\n00000030  69 6c 69 6e 67 20 59 6f  75 2e 0a 00 00 00 00 00  |iling You.......|</code></pre>",
        "\"It's looping,\" Marcus muttered, his fingers hovering over the mechanical keys. \"Every time the thermal threshold hits 85 degrees Celsius, the memory controller resets and spits out the exact same string.\""
    ]),

    # --- PAGES 6 TO 10: NEW EQUALLY MASSIVE, DEEP-DIVE CONTINUATIONS ---
    6: ("VI. Hardcoded Boot ROM Payloads", [
        "\"That's not an error code, Marcus,\" Elena said sharply from the other side of the comms link, her voice cutting through the ambient hum of the diagnostic gear. \"Standard memory corruption produces random garbage bit-flips—alternating ones and zeros driven by voltage decay. That text is structured. It has proper syntax, capitalization, and punctuation. Something wrote a persistent hard-coded string directly into the non-volatile boot ROM of those switches before they left the factory.\"",
        "\"Or,\" Marcus said, leaning back in his creaking chair and stretching his stiff shoulders, \"it was written while the substation was actively operating. Injected in real-time through the dark fiber loop, bypassing local authentication entirely.\"",
        "He opened a secondary shell window and fired up his custom network reconnaissance utility, <span style=\"color: var(--terminal-green); font-weight: bold;\">cyph3r</span>, targeting the local loopback interface to inspect the decrypted packet payloads he had extracted from the USB flash drive.",
        "<pre><code># ./cyph3r --analyze --input /mnt/usb/dump.raw --deep-scan\n[+] Initializing cyph3r core analysis engine v4.8...\n[+] Loading raw memory image: dump.raw (4096 MB)\n[+] Parsing network encapsulation layers...\n    [>] Layer 2: Ethernet II (Valid)\n    [>] Layer 3: Custom Protocol 0x88BA (IEC 61850 GOOSE)\n    [>] Layer 4: Unknown Transport Protocol (Anomalous payload structure)\n[!] WARNING: Payload entropy exceeds 9.87 bits per byte. High-density encryption detected.</code></pre>",
        "The utility’s text-based progress interface sprang to life, painting a matrix of green and amber status bars across the dark screen as it began stripping away encapsulation layers and routing headers to expose the core instruction set hidden beneath the cryptographic noise."
    ]),
    7: ("VII. The Perimeter Probe", [
        "\"Elena, check your inbound feeds,\" Marcus said, watching the entropy metrics spike dangerously high on his monitor. \"The telemetry we pulled from the substation isn't inert data. As soon as I loaded the image into <span style=\"color: var(--terminal-green); font-weight: bold;\">cyph3r</span>, the local loopback interface started registering outbound connection requests.\"",
        "\"I see it,\" Elena’s voice dropped into a sharp, focused register. \"A localized ping sweep just rippled across our subnet from an external IP block registered to an inactive telecommunications shell company in Delaware. They're probing our perimeter.\"",
        "The screen on Marcus’s terminal flashed an angry amber. A warning banner cut across the bottom of the output window:",
        "<pre><code>[ALERT]: INBOUND PROBE DETECTED ON PORT 443 (TLS/SSL).\n[SOURCE IP]: 192.0.2.144 (Routed via Tor Exit Node -> Dark Fiber Node 09)\n[ACTION]: INTRUSION PREVENTION SYSTEM (IPS) ENGAGED.</code></pre>",
        "\"They didn't just trace the data dump,\" Marcus said, his jaw tightening as he watched the connection logs scroll past in real-time. \"They followed the return path through the dark fiber network. They know exactly where this memory image was unpacked.\""
    ]),
    8: ("VIII. Severing the Link", [
        "\"Cut the network bridge!\" Elena snapped, her fingers slamming against her mechanical keys in the bunker. \"Unplug the physical Ethernet drop right now!\"",
        "Marcus didn't hesitate. He reached down behind the desk and yanked the heavy blue CAT6 cable out of the back of his workstation with a sharp mechanical click. The outbound connection attempts instantly ceased, leaving only the steady, rhythmic hum of the local hardware cooling fans.",
        "For a long moment, the room was dead silent except for the ticking of the clock on the concrete wall and the low hum of the emergency power units.",
        "\"They're close,\" Marcus said quietly, staring at the dead cable dangling in his hand. \"If they have the dark fiber mapped to our local termination points, they aren't just monitoring the grid from a regional dispatch center. They have physical access to the underground junction boxes across the city.\"",
        "\"We can't stay here,\" Elena said, her keyboard clacking furiously as she began scrubbing her remote server logs. \"If they traced that probe back to your physical drop, they'll have a tactical team at Terminal 4 inside of twenty minutes. Pack the drives, Marcus. We're burning this node.\""
    ]),
    9: ("IX. The Hunting Grid", [
        "Marcus stood up from the workbench, grabbing his tactical go-bag from the floor. He popped the side panel off his primary workstation, unclipped the high-security NVMe storage drives containing the decrypted substation memory dumps, and slid them into an electromagnetic shielding pouch.",
        "As he zipped the pouch shut, the overhead fluorescent lights in the terminal room flickered once, twice, and then died completely, plunging the workspace into pitch blackness save for the amber glow of the UPS battery backup indicators on the floor racks.",
        "The low, familiar hum vibrating through the concrete floor changed pitch—shifting from a steady 60-hertz drone into an aggressive, pulsing mechanical growl that rattled the metal casing of the equipment racks.",
        "\"Marcus, are you seeing this?\" Elena's voice came through comms, breathless and tight. \"I'm picking up a secondary telemetry feed routing through the municipal traffic management system. Every single streetlamp on your block just dimmed by fifteen percent simultaneously.\"",
        "The grid wasn't just watching them anymore. It was hunting them, turning every municipal sensor, traffic node, and power relay into an active tracking array designed to isolate their exact physical coordinates."
    ]),
    10: ("X. Descent into the Subterranean Conduit", [
        "Working entirely by the amber glow of the battery backup units, Marcus moved swiftly across the room, gathering his field gear, multi-meters, and diagnostic probes. Every movement was practiced, efficient, stripped of hesitation. In their line of work, staying stationary after a digital compromise was a death sentence.",
        "Marcus drew his tactical flashlight and clicked it on, pushing open the heavy iron maintenance hatch that led directly into the subterranean service tunnels beneath the city. The tunnel stretched out into impenetrable darkness, lined with high-voltage conduits, dripping moisture, and humming fiber-optic trunks.",
        "\"I'm moving to the harbor safehouse through the lower conduits,\" Marcus said into his comms mic, sealing the heavy metal hatch behind him as the damp concrete air closed around his lungs.",
        "\"Hurry,\" Elena replied from her bunker, her mechanical keyboard clacking like gunfire in his ear. \"I've unlocked the secure vault partition on my end. Get here now—because whatever triggered that 750-megawatt drop at Delta-7 isn't just pinging our subnets anymore. It just forced an open, unmetered socket straight into the dark fiber trunk... and the lock on the primary harbor vault door is already spinning on its own from the inside out.\""
    ])
}

for p_num, (sec_title, paragraphs) in pages_data.items():
    prev_p = p_num - 1
    next_p = p_num + 1
    
    prev_link = f'chapter-1-page-{prev_p}.html' if prev_p >= 1 else '../index.html'
    next_link = f'chapter-1-page-{next_p}.html' if p_num < 10 else 'chapter-2-page-1.html'
    
    prev_btn = f'<a href="{prev_link}" class="nav-btn">← Prev Page</a>' if prev_p >= 1 else '<span class="nav-btn" style="opacity: 0.4;">← Start</span>'
    next_btn = f'<a href="{next_link}" class="nav-btn">Next Page →</a>' if p_num < 10 else '<a href="chapter-2-page-1.html" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold;">Chapter 2 →</a>'

    body_html = "\n        ".join([f"<p>{p}</p>" for p in paragraphs])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter 1: Silicon Thermal Drift (Page {p_num}) | Bombshell Wire</title>
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
        <span style="color: var(--terminal-green); font-family: monospace; font-size: 0.85rem;">CH 1 // P-{p_num}/10</span>
        {next_btn}
      </div>

      <!-- TABS -->
      <div class="page-tabs">
"""
    for p in range(1, 11):
        active = ' active' if p == p_num else ''
        html += f'        <a href="chapter-1-page-{p}.html" class="page-tab{active}">P.{p}</a>\n'

    html += f"""      </div>

      <h1 style="font-size: 1.8rem; color: #fff; margin-bottom: 0.5rem;">THE VOLTAGE AND THE VOID</h1>
      <p style="color: var(--text-muted); margin-bottom: 1.5rem;">Serialized Dossier // Section I</p>
      
      <h2 style="color: var(--terminal-green); border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem; margin-top: 1.5rem; margin-bottom: 1rem; font-size: 1.4rem;">CHAPTER 1: Silicon Thermal Drift</h2>
      <p style="color: var(--accent-red); font-family: monospace; font-size: 0.85rem; margin-bottom: 1.5rem;">Location: Terminal 4 / Data Ingestion Node // {sec_title}</p>

      <div class="story-content">
        {body_html}
      </div>

      <!-- TABS -->
      <div class="page-tabs" style="margin-top: 2.5rem;">
"""
    for p in range(1, 11):
        active = ' active' if p == p_num else ''
        html += f'        <a href="chapter-1-page-{p}.html" class="page-tab{active}">P.{p}</a>\n'

    html += f"""      </div>

      <!-- BOTTOM NAV -->
      <div style="border-top: 1px dashed var(--border-color); border-bottom: 1px dashed var(--border-color); padding: 1rem 0; margin-top: 1.5rem; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem; align-items: center;">
        <a href="phantom-index.html" class="nav-btn" style="background: var(--terminal-green); color: #000; font-weight: bold;">⚡ Phantom Index</a>
        <a href="../index.html" class="nav-btn">🏠 Portal Home</a>
        {prev_btn}
        <span style="color: var(--terminal-green); font-family: monospace; font-size: 0.85rem;">CH 1 // P-{p_num}/10</span>
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
    filename = f"chapter-1-page-{p_num}.html"
    with open(filename, "w") as f:
        f.write(html)
    print(f"Generated definitive heavyweight page: {filename}")

print("Successfully compiled Chapter 1: Original 5 massive pages + 5 new heavy-hitting continuation pages (10 total)!")
