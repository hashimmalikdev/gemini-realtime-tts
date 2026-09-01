from gemini_tts import GeminiTTS

# Create the object ONLY ONCE (outside the loop)
tts = GeminiTTS(
    voice_name="Puck",                    # Choose any voice
    target_lang="US Accent English",      # Translate + speak in any language
    system_instruction="Speak Fast",      # Control tone, speed, personality
    summarize=False,                      # `if True`, Summarize long text first
    output_path="audio.wav"               # Save audio as .wav
)

# Reuse the same instance inside the loop
while True:
    text = input("\nTTS: ")
    tts.text(text)
