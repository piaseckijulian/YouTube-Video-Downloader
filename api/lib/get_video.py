import base64
import logging
from io import BytesIO

from fastapi import HTTPException
from pytube import YouTube
from pytube.exceptions import (
    AgeRestrictedError,
    LiveStreamError,
    MaxRetriesExceeded,
    MembersOnly,
    RegexMatchError,
    VideoPrivate,
    VideoRegionBlocked,
    VideoUnavailable,
)
from pytube.innertube import _default_clients

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(message)s", datefmt="%d/%m/%y %H:%M:%S"
)


# Unblock restricted content
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]


def get_video(video_url: str) -> str:
    try:
        video = YouTube(video_url)
        stream = (
            video.streams.filter(progressive=True, file_extension="mp4")
            .order_by("resolution")
            .desc()
            .first()
        )

        buffer = BytesIO()
        stream.stream_to_buffer(buffer)
        buffer.seek(0)

        # Encode the video data as a base64 string
        video_base64 = base64.b64encode(buffer.read()).decode("utf-8")

        return video_base64
    except VideoPrivate:
        raise HTTPException(status_code=400, detail="VIDEO_PRIVATE")
    except MembersOnly:
        raise HTTPException(status_code=400, detail="VIDEO_MEMBERS_ONLY")
    except AgeRestrictedError:
        raise HTTPException(status_code=400, detail="VIDEO_AGE_RESTRICTED")
    except VideoRegionBlocked:
        raise HTTPException(status_code=400, detail="VIDEO_REGION_BLOCKED")
    except LiveStreamError:
        raise HTTPException(status_code=400, detail="VIDEO_LIVE_STREAM")
    except VideoUnavailable:
        raise HTTPException(status_code=400, detail="VIDEO_UNAVAILABLE")
    except MaxRetriesExceeded:
        raise HTTPException(status_code=400, detail="MAX_RETRIES_EXCEEDED")
    except RegexMatchError:
        raise HTTPException(status_code=400, detail="INVALID_YOUTUBE_URL")
    except Exception as e:
        logging.error(
            f"An unknown error ocurred. Video URL: {video_url}, Error: {e}"
        )
        raise HTTPException(status_code=500, detail="An unknown error ocurred")
