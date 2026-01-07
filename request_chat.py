import openai
import os

openai.api_key = os.environ.get('OPENAI_API_KEY')

def enviar_para_chatgpt(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[ { "role": "user", "content": transcription } ]
    )

    return response.choices[0].message.content