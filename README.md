<div align="center">

# Gemini FREE Real-Time Text-To-Speech (TTS)

**Free real-time Text-to-Speech with Google Gemini API** — low-latency streaming TTS in Python with voice control, translation, custom speaking style, and AI summarization.

[![Demo Video](https://img.youtube.com/vi/_vlilHILGPk/maxresdefault.jpg)](https://www.youtube.com/watch?v=_vlilHILGPk)

[![Python Version](https://img.shields.io/badge/Python-3.12.10%20(Recommended)-blue.svg)](https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe)
[![Powered by Gemini](https://img.shields.io/badge/Powered%20By-Google%20Gemini%20API-orange.svg)](https://aistudio.google.com/api-keys)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

<img alt="comparison" src="https://github.com/user-attachments/assets/74f534a1-23b3-472d-9023-1572c85a4999"/>

</div>

---

## Features

- **Completely Free** – Works on Gemini free tier
- **Real-time Streaming** – Low latency audio
- **30+ Voices** – Choose any Gemini voice
- **Language & Accent Control** – Speak in any language
- **Custom Speaking Style** – Control tone, speed & personality
- **AI Summarization** – Shortens long text before speaking
- **Save Audio** – Export as `.wav`
- **Simple API** – Just a few lines of code

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Get free API key → [Google AI Studio](https://aistudio.google.com/api-keys)

---

## Quick Start & Usage

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

> **Important:** Always create `GeminiTTS` **outside** the loop and reuse the same instance. Creating a new object inside the loop will open multiple websockets and can cause Gemini errors.

---

## Available Voices

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

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `voice_name` | str | `"Zephyr"` | Voice name |
| `target_lang` | str | `None` | Target language/accent |
| `summarize` | bool | `False` | Summarize before speaking |
| `system_instruction` | str | `None` | Speaking style & tone |
| `output_path` | str | `None` | Save as `.wav` |

---

## Why This Project?

All complex TTS logic is already inside `gemini_tts.py`.  
You just import and use it — perfect for productivity.

---

## FAQ

**Is it free?**  
Yes, works with Gemini free tier.

**Can I change voice & language?**  
Yes — use `voice_name` and `target_lang`.

**Can I control how it speaks?**  
Yes — use `system_instruction`.

**Why create object only once?**  
Creating new objects inside the loop opens multiple websockets and can cause Gemini errors.

---

## License

MIT License

**YouTube Tutorial:** [Watch Demo](https://www.youtube.com/watch?v=_vlilHILGPk)
