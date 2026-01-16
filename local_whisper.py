
import whisper
import argparse
import os

def transcribe_and_translate(audio_path, translate=False):
    """
    Transcribes and optionally translates an audio file.

    Args:
        audio_path (str): Path to the audio file.
        translate (bool): Whether to translate the transcription to English.
    """
    if not os.path.exists(audio_path):
        print(f"Error: Audio file not found at '{audio_path}'")
        return

    print("Loading Whisper model...")
    model = whisper.load_model("base")
    print("Model loaded.")

    print(f"Transcribing '{audio_path}'...")
    result = model.transcribe(audio_path)

    print("\n--- Transcription ---")
    print(result["text"])

    if translate:
        print("\nTranslating to English...")
        translation_result = model.transcribe(audio_path, task="translate")

        print("\n--- Translation (English) ---")
        print(translation_result["text"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe and translate audio files locally with Whisper.")
    parser.add_argument("audio_path", help="Path to the audio file to transcribe.")
    parser.add_argument("--translate", action="store_true", help="Translate the transcription to English.")
    args = parser.parse_args()

    transcribe_and_translate(args.audio_path, args.translate)
