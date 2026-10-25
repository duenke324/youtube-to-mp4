# YouTube para MP4

Script em Python para descarregar vídeos do YouTube em **MP4 até 1080p**, com vídeo e áudio juntos num único ficheiro.

## Funcionalidades

- Descarrega vídeos e playlists inteiras
- Qualidade máxima de 1080p, dando preferência a H.264 (compatível com quase todos os leitores)
- Junta automaticamente o vídeo e o áudio num MP4
- Nomes de ficheiro compatíveis com o Windows
- Se um vídeo falhar, continua com os restantes

## Requisitos

- Python 3.9 ou superior
- Dependências:

```bash
pip install yt-dlp imageio-ffmpeg
```

> Se já tiveres o `ffmpeg` instalado no sistema, o script usa esse. Caso contrário, usa o do `imageio-ffmpeg`.

## Utilização

**Pedir o link no terminal:**

```bash
python youtube.py
```

**Um ou mais vídeos (ou playlists):**

```bash
python youtube.py https://www.youtube.com/watch?v=XXXX https://www.youtube.com/watch?v=YYYY
```

**Escolher a pasta de destino:**

```bash
python youtube.py https://www.youtube.com/watch?v=XXXX -o D:\Videos
```

Por omissão, os vídeos ficam na pasta `downloads` ao lado do script, com o nome `Título [1080p].mp4`.

## Opções

| Opção | Descrição |
|---|---|
| `links` | Um ou mais links de vídeos ou playlists |
| `-o`, `--saida` | Pasta de destino (padrão: `downloads`) |

## Aviso

Usa este script só para conteúdo que tens direito a descarregar e respeita os [Termos de Serviço do YouTube](https://www.youtube.com/t/terms).
