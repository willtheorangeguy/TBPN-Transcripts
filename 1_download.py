"""
This script uses yt-dlp to download audio, by year,
from the Diet TBPN videos on YouTube.
"""

import yt_dlp

def download_videos(playlist_url):
    """
    Downloads all videos from the YouTube playlist.
    """
    ydl_opts = {
        "format": "bestaudio",
        "noplaylist": False,
        "ignoreerrors": True,
        "download_archive": "downloaded.log",
        "outtmpl": "%(upload_date>%Y)s/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "0",
            }
        ],
        'concurrent-fragments': True,
        'no-mtime': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(playlist_url)

if __name__ == "__main__":
    playlist = "https://www.youtube.com/playlist?list=PLBV_0ax_G8bpVbF8ndXETB2S2obcwF8gT"
    download_videos(playlist)
    print("Downloaded all Diet TBPN episodes from the TBPN channel.")
