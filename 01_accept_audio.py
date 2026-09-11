import os

def accept_audio_file(file_path):
    allowed_formats = [".wav", ".mp3"]

    if not os.path.exists(file_path):
        return "File does not exist."

    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension not in allowed_formats:
        return "Unsupported audio format. Please use WAV or MP3."

    return f"Audio file accepted successfully: {file_path}"

audio_file = input("Enter the path of your audio file: ")
result = accept_audio_file(audio_file)
print(result)
