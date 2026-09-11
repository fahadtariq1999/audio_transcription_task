import whisper

def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]

audio_file = input("Enter audio file path: ")
transcription = transcribe_audio(audio_file)
print("Transcription:")
print(transcription)
