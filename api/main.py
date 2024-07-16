from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from lib.get_video import get_video

app = FastAPI()


@app.get("/download-video")
async def download_video(url: str):
    if not url:
        raise HTTPException(
            status_code=400,
            detail="Your request is missing 'url' query parameter",
        )

    buffer, error = get_video(url)

    if buffer:
        return StreamingResponse(
            content=buffer,
            media_type="video/mp4",
            headers={"Content-Disposition": "attachment; filename=video.mp4"},
        )
    else:
        raise HTTPException(status_code=400, detail=error)
