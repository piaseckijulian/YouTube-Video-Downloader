import base64
import logging
from os import environ

import requests
from dotenv import load_dotenv
from fastapi import HTTPException
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

load_dotenv()

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(message)s", datefmt="%d/%m/%y %H:%M:%S"
)


def get_video(video_url: str) -> str:
    ydl_opts = {
        "username": environ.get("YOUTUBE_USERNAME"),
        "password": environ.get("YOUTUBE_PASSWORD"),
        "format": "best[ext=mp4]",
        "quiet": True,
        "outtmpl": "",
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            video_url = info["url"]

            res = requests.get(video_url)
            video_content = res.content

            video_base64 = base64.b64encode(video_content).decode("utf-8")

            return video_base64

    except DownloadError:
        raise HTTPException(status_code=400, detail="VIDEO_UNAVAILABLE")

    except Exception as e:
        logging.error(
            f"An unknown error occurred. Video URL: {video_url}, Error: {e}"
        )

        raise HTTPException(
            status_code=500, detail="An unknown error occurred"
        )
