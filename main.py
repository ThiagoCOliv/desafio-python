from IPython.display import Audio, display
from gravar_audio import record
from reconhecer_fala import reconhecer_fala
from request_chat import enviar_para_chatgpt
from response_audio import resposta_em_audio

record_file = record()
transcription = reconhecer_fala(record_file)
chatgpt_response = enviar_para_chatgpt(transcription)
response_audio = resposta_em_audio(chatgpt_response)

display(Audio(response_audio, autoplay=True))