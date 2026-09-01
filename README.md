<div align="center">

# Gemini Free Real-Time Text-to-Speech

**Free real-time streaming TTS powered by Google Gemini**

Low latency • 30+ voices • Language control • Custom speaking style • AI summarization

[![Demo Video](https://img.youtube.com/vi/_vlilHILGPk/maxresdefault.jpg)](https://www.youtube.com/watch?v=_vlilHILGPk)

[![Python](https://img.shields.io/badge/Python-3.12.10%20(Recommended)-blue.svg)](https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe)
[![Powered by Gemini](https://img.shields.io/badge/Powered%20By-Google%20Gemini%20API-orange.svg)](https://aistudio.google.com/api-keys)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

<img alt="Gemini Free Real-Time TTS" src="https://github.com/user-attachments/assets/74f534a1-23b3-472d-9023-1572c85a4999" width="780"/>

</div>

---

### Why this exists

Most free TTS options are either slow, limited, or complicated to set up.  
This project gives you **real-time streaming speech** using Google Gemini — completely free on the free tier.

Just a few lines of code and you can start speaking.

---

### Features

- Completely free (Gemini free tier)
- Real-time streaming with low latency
- 30+ high-quality voices
- Speak in any language or accent
- Control tone, speed, and personality
- Optional AI summarization for long text
- Save output as `.wav`
- Extremely simple API

---

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/gemini-realtime-tts.git
cd gemini-realtime-tts
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Get a free API key here → [Google AI Studio](https://aistudio.google.com/api-keys)

---

### Quick Start

```python
from gemini_tts import GeminiTTS

# Create the object ONLY ONCE (outside the loop)
tts = GeminiTTS(
    voice_name="Puck",                    # Choose any voice
    target_lang="US Accent English",      # Translate + speak in any language
    system_instruction="Speak Fast",      # Control tone, speed, personality
    summarize=True,                       # Summarize long text first
    output_path="audio.wav"               # Save audio as .wav
)

# Reuse the same instance inside the loop
while True:
    text = input("\nTTS: ")
    tts.text(text)
```

> **Important:** Always create the `GeminiTTS` object **outside** the loop.  
> Creating it inside the loop opens multiple connections and can cause errors.

---

### Available Voices

| Voice | Pitch | Style | Best For |
|-------|-------|-------|----------|
| **Zephyr** | Higher | Bright | Announcements |
| **Leda** | Higher | Youthful | Gaming |
| **Laomedeia** | Higher | Upbeat | Casual Talk |
| **Achernar** | Higher | Soft | Bedtime Stories |
| **Puck** | Middle | Upbeat | Virtual Assistants |
| **Kore** | Middle | Firm | Tutorials |
| **Aoede** | Middle | Breezy | Podcasts |
| **Callirrhoe** | Middle | Easy-going | Vlogs |
| **Autonoe** | Middle | Bright | Product Demos |
| **Despina** | Middle | Smooth | Customer Support |
| **Erinome** | Middle | Clear | Education |
| **Rasalgethi** | Middle | Informative | News |
| **Gacrux** | Middle | Mature | Business |
| **Pulcherrima** | Middle | Forward | Instructions |
| **Vindemiatrix** | Middle | Gentle | Meditation |
| **Sadaltager** | Middle | Knowledgeable | Audiobooks |
| **Sulafat** | Middle | Warm | Companion AI |
| **Fenrir** | Lower Middle | Excitable | Gaming Commentary |
| **Orus** | Lower Middle | Firm | Security |
| **Iapetus** | Lower Middle | Clear | Audio Guides |
| **Umbriel** | Lower Middle | Easy-going | Chill Podcasts |
| **Alnilam** | Lower Middle | Firm | Corporate Training |
| **Schedar** | Lower Middle | Even | Neutral Narration |
| **Achird** | Lower Middle | Friendly | Onboarding |
| **Zubenelgenubi** | Lower Middle | Casual | Daily Updates |
| **Charon** | Lower | Informative | Scientific Docs |
| **Enceladus** | Lower | Breathy | Storytelling |
| **Algieba** | Lower | Smooth | Voiceover |
| **Algenib** | Lower | Gravelly | Character Acting |
| **Sadachbia** | Lower | Lively | Commercials |

---

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `voice_name` | str | `"Zephyr"` | Voice name |
| `target_lang` | str | `None` | Target language or accent |
| `summarize` | bool | `False` | Summarize text before speaking |
| `system_instruction` | str | `None` | Speaking style, tone, and speed |
| `output_path` | str | `None` | Path to save `.wav` file |

---

### FAQ

**Is it free?**  
Yes, it works on the Gemini free tier.

**Can I change the voice and language?**  
Yes. Use `voice_name` and `target_lang`.

**Can I control how it speaks?**  
Yes. Use `system_instruction`.

**Why create the object only once?**  
Creating a new instance every time opens multiple WebSocket connections and can cause Gemini errors.

---

### License

MIT License

**Demo:** [Watch on YouTube](https://www.youtube.com/watch?v=_vlilHILGPk)
