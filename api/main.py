from fastapi import FastAPI
from lib.get_video import get_video

app = FastAPI()


@app.get("/download-video")
async def download_video(url: str):
    video_base64 = get_video(url)

    return {"videoBase64": video_base64}
