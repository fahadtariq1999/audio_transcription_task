from pydub import AudioSegment
import os

def convert_audio(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    supported_formats = [".mp3", ".wav", ".m4a", ".flac", ".ogg"]

    if extension not in supported_formats:
        raise ValueError("Unsupported audio format")

    audio = AudioSegment.from_file(file_path)
    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(16000)

    output_file = "converted_audio.wav"
    audio.export(output_file, format="wav")
    return output_file

audio_file = input("Enter audio file path: ")
converted_file = convert_audio(audio_file)
print("Audio converted successfully:", converted_file)
