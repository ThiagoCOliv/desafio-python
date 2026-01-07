# desafio-python

Projeto de exemplo para gravar áudio, transcrever usando Whisper e enviar para o ChatGPT, retornando uma resposta em áudio.

## Visão geral

Este repositório contém scripts que fazem o fluxo:
- capturar/receber áudio do usuário;
- transcrever áudio com o modelo Whisper (openai-whisper / whisper);
- enviar a transcrição para a API do OpenAI (Chat Completions / ChatGPT);
- gerar áudio da resposta usando gTTS;
- (em ambientes interativos) reproduzir o áudio resultante.

Arquivos principais
- `main.py` — fluxo de interação (usa `display(Audio)` para tocar o áudio em notebooks/Colab);
- `gravar_audio.py` — gravação via JavaScript (destinado a Google Colab / notebook);
- `reconhecer_fala.py` — usa `whisper` para transcrição;
- `request_chat.py` — ponte com a API OpenAI;
- `response_audio.py` — converte texto em áudio usando `gTTS`;

> Observação: os utilitários de gravação e reprodução neste repositório estão implementados para funcionar em Google Colab / Jupyter notebooks (o código usa `google.colab` e `IPython.display`). Para executar localmente no Windows é necessário adaptar `gravar_audio.py` (por exemplo usar `sounddevice` ou `pyaudio`) e ajustar caminhos de arquivo.

## Requisitos

Um arquivo `requirements.txt` inicial foi adicionado com as dependências inferidas a partir do código:

```
openai
openai-whisper
gTTS
ipython
torch
```

Notas sobre requisitos
- `openai-whisper` (ou `whisper`) depende de `torch` — instale a versão de `torch` correta para sua plataforma (CPU vs GPU). Consulte https://pytorch.org/get-started/locally/ para instruções oficiais.
- Em Windows, a instalação de `torch` normalmente usa um comando com o índice de pacotes da PyTorch. Um exemplo para instalação CPU-only (PowerShell):

```powershell
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

- `ffmpeg` é frequentemente necessário para manipular arquivos de áudio com alguns backends — instale o `ffmpeg` no sistema e certifique-se de que esteja no PATH.

## Configuração

1. Copie ou defina sua chave da OpenAI em variáveis de ambiente. Exemplo rápido editando `env.py` (apenas para testes locais — não comitar chaves ao Git):

```python
import os
os.environ['OPENAI_API_KEY'] = 'sua_chave_aqui'
os.environ['LANGUAGE'] = 'pt'
```

Ou prefira definir no sistema:

```powershell
$env:OPENAI_API_KEY = 'sua_chave_aqui'
$env:LANGUAGE = 'pt'
```

2. Instale dependências:

```powershell
pip install -r .\requirements.txt
```

Se precisar de instalação específica do `torch`, use o comando recomendado pelo site da PyTorch (exemplo acima para CPU).

## Como executar

- Execução em Google Colab / Jupyter (recomendado para o estado atual do projeto):
  1. Faça upload dos arquivos para um notebook Colab ou abra o repositório no Colab.
  2. Execute as células/arquivos — `gravar_audio.py` usa JavaScript do navegador para gravar áudio e salvar em `/content`.

- Execução local (Windows):
  - Atenção: para rodar localmente você precisa adaptar `gravar_audio.py` (o atual código usa APIs do navegador/Colab). Uma alternativa rápida é substituir a gravação por `sounddevice`:

## Observações e riscos
- Não coloque sua chave da OpenAI em arquivos versionados. Use variáveis de ambiente para segurança.
- A API usada no código (`openai.ChatCompletion.create`) refere-se a endpoints clássicos — valide se está usando a versão/endpoint correto da sua conta e biblioteca instalada.

## Próximos passos sugeridos
- Adicionar um modo local de gravação (`sounddevice`) e execução automática fora do notebook.
- Pinagem de versões em `requirements.txt`.
- Adicionar instruções detalhadas de instalação do `torch` para Windows GPU/CPU no README.