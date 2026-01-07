from IPython.display import Audio, display
from gravar_audio import record
from reconhecer_fala import reconhecer_fala
from request_chat import enviar_para_chatgpt
from response_audio import resposta_em_audio

while input("Pressione Enter para começar a gravação de áudio (ou digite 'sair' para encerrar): ") != 'sair':
    tempo_gravacao = input("Quanto tempo deseja gravar em segundos? Pressione Enter para 5 segundos ou digite o número de segundos: ")

    record_file = record(int(tempo_gravacao) or 5)
    transcription = reconhecer_fala(record_file)
    chatgpt_response = enviar_para_chatgpt(transcription)
    response_audio = resposta_em_audio(chatgpt_response)

    display(Audio(response_audio, autoplay=True))