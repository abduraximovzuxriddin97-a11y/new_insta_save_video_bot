import yt_dlp
import uuid
from pathlib import Path

DOWNLOAD_DIR = Path("downloads")

def download_instagram_video(url: str) -> Path:
    DOWNLOAD_DIR.mkdir(exist_ok=True)

    file_id = uuid.uuid4().hex
    output = DOWNLOAD_DIR / f"{file_id}.%(ext)s"

    ydl_opts = {
        "outtmpl": str(output),
        "format": "mp4",
        "quiet": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return Path(filename)
