import whisper
import os

model = whisper.load_model("small")

def reconhecer_fala(record_file):
    result = model.transcribe(record_file, fp16=False, language=os.environ.get("LANGUAGE", "pt"))
    return result["text"]