# Transcribing an MP3 file using OpenAI Whisper.
# Cleaning filler words, and exporting to a Word document (British English output).

# Audio file: Orlando: A Biography, Orlando: A Biography | Novel by Virginia Woolf
# Chapter 1, Part 3: Orlando attends Queen Elizabeth 

# Author: Tihana Gray


from pathlib import Path
import re
from docx import Document
import whisper


# Path to the MP3 audio file
AUDIO_PATH = Path("/workspaces/my-projects/audio_transcript/orlando_03_woolf_128kb.mp3")

# Choosing the Whisper model size
MODEL_NAME = "small"  # Options: "base", "small", "medium", "large"

# Force transcription language (British English context)
LANGUAGE = "en"
# ------------------------------

def clean_disfluencies(text: str) -> str:
    """Remove filler words and tidy punctuation."""
    patterns = [
        r"\b(u+h+|uh)\b[,\.\?!;:]*",
        r"\b(um+|umm+)\b[,\.\?!;:]*",
        r"\b(erm+|er)\b[,\.\?!;:]*",
        r"\b(a+h+|ah+)\b[,\.\?!;:]*",
        r"\b(i\s+mean)\b[,\.\?!;:]*",
        r"\b(you\s+know)\b[,\.\?!;:]*",
        r"\b(kinda|kind\s+of)\b[,\.\?!;:]*",
        r"\b(sort\s+of)\b[,\.\?!;:]*",
    ]

    cleaned = text
    for pat in patterns:
        cleaned = re.sub(pat, "", cleaned, flags=re.IGNORECASE)

    # Tidying up spacing and punctuation
    cleaned = re.sub(r"\s{2,}", " ", cleaned)
    cleaned = re.sub(r"\s+([,\.\?!;:])", r"\1", cleaned)
    return cleaned.strip()


def save_to_word(text: str, output_file: Path):
    """Write the transcript text to a Word document in UTF-8 encoding."""
    doc = Document()
    doc.add_heading("Clean Transcript (British English)", level=1)
    doc.add_paragraph(text)
    doc.save(output_file)
    print(f"Word file saved at:\n{output_file}")


def main():
    print(f"Loading Whisper model '{MODEL_NAME}'…")
    model = whisper.load_model(MODEL_NAME)

    print(f"Transcribing in British English: {AUDIO_PATH.name}")
    result = model.transcribe(
        str(AUDIO_PATH),
        fp16=False,
        verbose=False,
        language=LANGUAGE  # Force transcription in English
    )

    raw_text = result.get("text", "") or ""
    cleaned_text = clean_disfluencies(raw_text)

    # Save transcript as Word doc next to the audio file
    out_file = AUDIO_PATH.with_name(AUDIO_PATH.stem + "_transcript_clean.docx")
    save_to_word(cleaned_text, out_file)

    print("Transcription complete!")


if __name__ == "__main__":
    main()

