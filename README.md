# Audio Transcription Pipeline

This project is a simple Python-based transcription pipeline using OpenAI Whisper and pydub/FFmpeg.

## What it does
- Accepts WAV and MP3 audio files
- Transcribes speech into text
- Returns timestamps per segment
- Handles MP3, WAV, M4A, FLAC, and OGG
- Splits long audio into 5-minute chunks

## Design decisions
I chose Python because it has strong audio and speech-processing support. I used Whisper because it is open source, supports multiple languages, and provides segment timestamps. I used pydub with FFmpeg so different audio formats can be converted to a consistent 16 kHz mono WAV format before transcription.

For concurrent uploads, I would use a queue-based design. Each upload would receive a unique task ID and be placed into a queue such as Redis or RabbitMQ. Separate workers, for example Celery workers, would process transcription task in parallel depending on the available CPU or GPU capacity.

For storage, I would keep files locally for a small demo. In production, I would store audio in object storage such as Amazon S3 and keep transcript metadata, task status, timestamps, and errors in PostgreSQL.

For failures, I would retry temporary errors up to three times with a short delay. I would keep the original audio until the task completes or permanently fails. Corrupted or unsupported files would fail immediately rather than being retried.

For an API version, I would use FastAPI with endpoints such as `POST /transcriptions` to upload audio, `GET /transcriptions/{task_id}` to check status and retrieve results, and `GET /health` for service monitoring.

## Setup
Install dependencies:

```bash
pip install -r requirements.txt
```

FFmpeg must also be installed on the system.

Run a script, for example:

```bash
python 02_transcribe_audio.py
```

## Future improvements
A production version would combine these scripts into one API service, add background workers, cloud storage, database persistence, authentication, rate limiting, retries, structured logging, and automatic cleanup of temporary files.
