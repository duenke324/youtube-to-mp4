"""
Descarregar vídeos do YouTube em MP4 até 1080p.

Uso:
    python youtube.py                          -> pede o link
    python youtube.py LINK [LINK ...]          -> descarrega um ou mais vídeos (ou playlists)
    python youtube.py LINK -o D:\\Videos        -> escolhe a pasta de destino

Requer: pip install yt-dlp imageio-ffmpeg
"""

import argparse
import shutil
import sys
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    sys.exit("yt-dlp não encontrado. Instale com:  pip install yt-dlp")


def encontrar_ffmpeg() -> str:
    caminho = shutil.which("ffmpeg")
    if caminho:
        return caminho
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        sys.exit("ffmpeg não encontrado. Instale com:  pip install imageio-ffmpeg")


def descarregar(links: list[str], pasta: Path):
    pasta.mkdir(parents=True, exist_ok=True)
    opcoes = {
        # Melhor vídeo até 1080p (preferindo H.264/MP4) + melhor áudio; junta tudo num MP4.
        "format": (
            "bv*[height<=1080][vcodec^=avc1]+ba[ext=m4a]/"
            "bv*[height<=1080][ext=mp4]+ba[ext=m4a]/"
            "bv*[height<=1080]+ba/"
            "b[height<=1080]/b"
        ),
        "merge_output_format": "mp4",
        "ffmpeg_location": encontrar_ffmpeg(),
        "outtmpl": str(pasta / "%(title)s [%(height)sp].%(ext)s"),
        "windowsfilenames": True,
        "ignoreerrors": True,
    }
    with yt_dlp.YoutubeDL(opcoes) as ydl:
        return ydl.download(links)


def main():
    parser = argparse.ArgumentParser(description="Descarrega vídeos do YouTube em MP4 1080p.")
    parser.add_argument("links", nargs="*", help="links de vídeos ou playlists")
    parser.add_argument("-o", "--saida", default=str(Path(__file__).parent / "downloads"),
                        help="pasta de destino (padrão: pasta 'downloads' ao lado do script)")
    args = parser.parse_args()

    links = args.links
    if not links:
        link = input("Cole o link do YouTube: ").strip()
        if not link:
            sys.exit("Nenhum link indicado.")
        links = [link]

    erro = descarregar(links, Path(args.saida))
    print("\nConcluído." if not erro else "\nTerminado com erros (ver mensagens acima).")


if __name__ == "__main__":
    main()
