<div align="center">

  # 🔊 Gemini FREE Real-Time Text-To-Speech (TTS)

  [![🎥 Demo Video](https://img.youtube.com/vi/_vlilHILGPk/maxresdefault.jpg)](https://www.youtube.com/watch?v=_vlilHILGPk)

  [![Python Version](https://img.shields.io/badge/Python-3.12.10%20(Recommended)-blue.svg)](https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe)
  [![Powered by Gemini](https://img.shields.io/badge/Powered%20By-Google%20Gemini%20API-orange.svg)](https://aistudio.google.com/api-keys)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

</div>

<img width="300" height="146" alt="comparison" src="https://github.com/user-attachments/assets/3133352f-9a70-4d11-bb2b-e51465334df8" />
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 390" width="100%" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif">
  <style>
    /* Default (Light Theme) */
    .bg { fill: #ffffff; }
    .card { fill: #f6f8fa; stroke: #d0d7de; }
    .card-highlight { fill: #f6f8fa; stroke: #1a7f37; }
    .text-title { fill: #1f2328; font-weight: bold; font-size: 15px; }
    .text-title-green { fill: #1a7f37; font-weight: bold; font-size: 15px; }
    .text-primary { fill: #1f2328; font-size: 13px; }
    .text-muted { fill: #57606a; font-size: 12px; }
    .box { fill: #ffffff; stroke: #d0d7de; stroke-width: 1.5; }
    .hero-box { fill: #dafbe1; stroke: #1a7f37; stroke-width: 1.5; }
    .hero-text { fill: #116329; font-weight: bold; font-size: 13px; }
    .arrow { fill: #57606a; font-size: 18px; }
    .green-arrow { fill: #1a7f37; font-size: 18px; }
    
    .badge-red { fill: #ffebe9; stroke: #cf222e; }
    .badge-red-text { fill: #cf222e; font-size: 11px; font-weight: bold; }
    
    .badge-green { fill: #dafbe1; stroke: #1a7f37; }
    .badge-green-text { fill: #116329; font-size: 11px; font-weight: bold; }

    /* GitHub Dark Theme Auto-Adaptation */
    @media (prefers-color-scheme: dark) {
      .bg { fill: #0d1117; }
      .card { fill: #161b22; stroke: #30363d; }
      .card-highlight { fill: #161b22; stroke: #2ea043; }
      .text-title { fill: #f0f6fc; }
      .text-title-green { fill: #3fb950; }
      .text-primary { fill: #f0f6fc; }
      .text-muted { fill: #8b949e; }
      .box { fill: #21262d; stroke: #30363d; }
      .hero-box { fill: rgba(46, 160, 67, 0.15); stroke: #3fb950; }
      .hero-text { fill: #3fb950; }
      .arrow { fill: #8b949e; }
      .green-arrow { fill: #3fb950; }
      
      .badge-red { fill: rgba(248, 81, 73, 0.15); stroke: #f85149; }
      .badge-red-text { fill: #ff7b72; }
      
      .badge-green { fill: rgba(46, 160, 67, 0.15); stroke: #3fb950; }
      .badge-green-text { fill: #56d364; }
    }
  </style>

  <!-- Background -->
  <rect width="800" height="390" class="bg" rx="10"/>

  <!-- TRADITIONAL PAID TTS FLOW -->
  <rect x="30" y="25" width="740" height="150" class="card" rx="8" stroke-width="1.5"/>
  <text x="50" y="55" class="text-title">Traditional TTS APIs (ElevenLabs / Azure / gTTS)</text>
  
  <!-- Badges for Traditional -->
  <rect x="510" y="38" width="115" height="22" class="badge-red" rx="11" stroke-width="1"/>
  <text x="567" y="53" class="badge-red-text" text-anchor="middle">💰 Paid / Per-Char</text>

  <rect x="633" y="38" width="120" height="22" class="badge-red" rx="11" stroke-width="1"/>
  <text x="693" y="53" class="badge-red-text" text-anchor="middle">🛑 Restrictive Limits</text>

  <!-- Flow Boxes -->
  <rect x="50" y="85" width="130" height="65" class="box" rx="6"/>
  <text x="115" y="115" class="text-primary" font-weight="bold" text-anchor="middle">Text Input</text>
  <text x="115" y="132" class="text-muted" text-anchor="middle">(Standard Request)</text>

  <text x="200" y="122" class="arrow" text-anchor="middle">➔</text>

  <rect x="225" y="85" width="220" height="65" class="box" rx="6"/>
  <text x="335" y="112" class="text-primary" text-anchor="middle">HTTP REST Request</text>
  <text x="335" y="132" class="text-muted" text-anchor="middle">(Wait for full audio file)</text>

  <text x="465" y="122" class="arrow" text-anchor="middle">➔</text>

  <rect x="490" y="85" width="220" height="65" class="box" rx="6"/>
  <text x="600" y="112" class="text-primary" text-anchor="middle">Buffered Playback</text>
  <text x="600" y="132" class="text-muted" text-anchor="middle">(High latency delay)</text>

  <!-- THIS REPO GEMINI LIVE WEBSOCKET FLOW -->
  <rect x="30" y="200" width="740" height="160" class="card-highlight" rx="8" stroke-width="2"/>
  <text x="50" y="232" class="text-title-green">🚀 This Repo: Gemini Live API Engine</text>
  
  <!-- Badges for Gemini -->
  <rect x="520" y="215" width="105" height="22" class="badge-green" rx="11" stroke-width="1"/>
  <text x="572" y="230" class="badge-green-text" text-anchor="middle">🎁 100% FREE</text>

  <rect x="633" y="215" width="120" height="22" class="badge-green" rx="11" stroke-width="1"/>
  <text x="693" y="230" class="badge-green-text" text-anchor="middle">♾️ Unlimited RPD</text>

  <!-- Flow Boxes -->
  <rect x="50" y="260" width="130" height="70" class="box" rx="6"/>
  <text x="115" y="292" class="text-primary" font-weight="bold" text-anchor="middle">app.py</text>
  <text x="115" y="310" class="text-muted" text-anchor="middle">(Text Input Loop)</text>

  <text x="200" y="300" class="green-arrow" text-anchor="middle">➔</text>

  <rect x="225" y="255" width="250" height="80" class="hero-box" rx="6"/>
  <text x="350" y="280" class="hero-text" text-anchor="middle">gemini_tts.py Wrapper</text>
  <text x="350" y="298" class="text-muted" text-anchor="middle">models/gemini-3.1-flash-live-preview</text>
  <text x="350" y="318" class="hero-text" font-size="11" text-anchor="middle">Persistent WebSocket Stream</text>

  <text x="495" y="300" class="green-arrow" text-anchor="middle">➔</text>

  <rect x="520" y="260" width="220" height="70" class="box" rx="6"/>
  <text x="630" y="288" class="text-primary" font-weight="bold" text-anchor="middle">Live Audio Stream</text>
  <text x="630" y="308" class="text-muted" text-anchor="middle">(PyAudio Playback &amp; .wav)</text>
</svg>
