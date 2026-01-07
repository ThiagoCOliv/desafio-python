from gtts import  gTTS
import os

def resposta_em_audio(chatgpt_response):
    gtts_object = gTTS(text=chatgpt_response, lang=os.environ.get("LANGUAGE", "pt"), slow=False)

    response_audio = "/content/response_audio.wav"
    gtts_object.save(response_audio)

    return response_audio