from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from lib.get_video import get_video

app = FastAPI()


@app.get("/download-video")
async def download_video(url: str):
    buffer = get_video(url)

    return StreamingResponse(
        content=buffer,
        media_type="video/mp4",
        headers={"Content-Disposition": "attachment; filename=video.mp4"},
    )
