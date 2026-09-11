import whisper

def transcribe_with_timestamps(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)

    print("\nFull Transcription:")
    print(result["text"])

    print("\nTranscription with Timestamps:")
    for segment in result["segments"]:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"]
        print(f"[{start:.2f}s - {end:.2f}s] {text}")

audio_file = input("Enter audio file path: ")
transcribe_with_timestamps(audio_file)
