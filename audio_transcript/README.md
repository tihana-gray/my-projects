# Orlando Audio Transcription Project

### Author: Tihana Gray  
### Source: *Orlando: A Biography* by Virginia Woolf – Chapter 1, Part 3

---

## Overview
This project demonstrates how to use **OpenAI Whisper** in Python to:
- Transcribe an MP3 audio file to text.
- Clean filler words (e.g., “uh”, “um”, “you know”).
- Export the clean transcript to a **Microsoft Word (.docx)** document.
- Maintain **British English** spelling and context.

The project was developed and executed in **GitHub Codespaces**.

---

## Requirements

### Python Libraries
| Library | Purpose | Reference |
|----------|----------|------------|
| `openai-whisper` | Speech-to-text model by OpenAI | [GitHub](https://github.com/openai/whisper) |
| `python-docx` | Create and edit Word documents | [Docs](https://python-docx.readthedocs.io/en/latest/) |
| `torch` | Required backend for Whisper | [PyTorch](https://pytorch.org/) |
| `re` | Built-in regex for cleaning text | [Python re](https://docs.python.org/3/library/re.html) |
| `pathlib` | Path management | [Python pathlib](https://docs.python.org/3/library/pathlib.html) |

---

## Installation

Run the following inside your Codespace terminal (or local environment):

```bash
pip install openai-whisper python-docx torch
sudo apt-get update && sudo apt-get install ffmpeg -y
```
> **Note:**  
FFmpeg is required for Whisper to process MP3, M4A, WAV, and other audio formats.

---

### Virtual Environment Setup

If you are using a virtual environment, activate it and install dependencies there:

```bash
source /workspaces/my-projects/.venv/bin/activate
pip install openai-whisper python-docx torch
```

---

### Usage

1. Place your audio file in the audio_transcript directory.

```bash
/workspaces/my-projects/audio_transcript/orlando_03_woolf_128kb.mp3
```

2. Run the transcription script:

```bash
python /workspaces/my-projects/audio_transcript/orlando_transcript.py
```

3. Output:

A cleaned transcript saved as:

```bash
orlando_03_woolf_128kb_transcript_clean.docx
```

### Cleaning Logic

The script removes common disfluencies and filler phrases such as: uh, um, erm, ah, i mean, you know, kinda, sort of.<br>
It also tidies punctuation and removes excess spacing using regular expressions (`re`) to improve readability and flow.


---


## Notes

### Model Choice

Whisper offers several model sizes: `tiny`, `base`, `small`, `medium`, and `large`.<br>
Larger models are more accurate but slower and memory-intensive.<br>
The `small` model offers a balance between performance and quality.<br>

### Language Enforcement

The parameter `language="en"` ensures transcription is processed in English (UK), preventing Whisper from auto-detecting another language.

### CPU vs GPU Usage

Setting `fp16=False` ensures compatibility with CPU-only environments such as GitHub Codespaces or standard laptops.


## 📚 References

- OpenAI Whisper: https://github.com/openai/whisper
- python-docx Documentation: https://python-docx.readthedocs.io/en/latest/
- Python Regular Expressions HOWTO: https://docs.python.org/3/howto/regex.html
- PyTorch Official Site: https://pytorch.org/
- pathlib Module: https://docs.python.org/3/library/pathlib.html
- FFmpeg: https://ffmpeg.org/


### ✨ Future Improvements

- Automatic paragraph formatting — split text based on pauses or sentence length.
- Speaker identification — differentiate between multiple voices in dialogue.
- Additional export formats — PDF and plain text alongside .docx.
- GUI interface — build a drag-and-drop transcription application.

## License

This project is open-source and intended for educational and research use.<br>
All audio used belongs to the public domain (Orlando: A Biography by Virginia Woolf).<br>
Source link: https://archive.org/details/orlandoabiography2_2412_librivox/orlando_04_woolf_128kb.mp3

## End