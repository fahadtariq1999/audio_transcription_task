from pydub import AudioSegment
import whisper

def transcribe_long_audio(file_path):
    model = whisper.load_model("base")
    audio = AudioSegment.from_file(file_path)
    chunk_length = 5 * 60 * 1000

    full_transcription = []

    for i in range(0, len(audio), chunk_length):
        chunk = audio[i:i + chunk_length]
        chunk_file = f"chunk_{i}.wav"
        chunk.export(chunk_file, format="wav")

        result = model.transcribe(chunk_file)
        full_transcription.append(result["text"])

    return " ".join(full_transcription)

audio_file = input("Enter audio file path: ")
text = transcribe_long_audio(audio_file)
print(text)
