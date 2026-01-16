
# Local Whisper

Local Whisper is a Python-based tool that allows you to transcribe and translate audio files locally using OpenAI's powerful Whisper model. No need to send your data to the cloud!

## Features

*   **Local Transcription:** Transcribe audio files (MP3, WAV, etc.) directly on your machine.
*   **Translation:** Translate the transcription into English.
*   **Command-Line Interface:** Easy-to-use CLI for all operations.
*   **Privacy-Focused:** Your audio data never leaves your computer.

## Getting Started

### Prerequisites

*   Python 3.7+
*   `ffmpeg` installed on your system.

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/local-whisper.git
    cd local-whisper
    ```
2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To transcribe an audio file:

```bash
python local_whisper.py <path_to_your_audio_file>
```

To transcribe and translate an audio file to English:

```bash
python local_whisper.py <path_to_your_audio_file> --translate
```
# local-whisper
