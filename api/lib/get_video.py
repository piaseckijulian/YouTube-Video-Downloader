import logging
from io import BytesIO

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


# Return buffer or error
def get_video(video_url: str) -> tuple[BytesIO | None, str | None]:
    try:
        video = YouTube(video_url)
        stream = video.streams.get_highest_resolution()

        buffer = BytesIO()
        # Save video to buffer
        stream.stream_to_buffer(buffer)
        buffer.seek(0)

        return (buffer, None)

    except VideoPrivate:
        return (None, "VIDEO_PRIVATE")
    except MembersOnly:
        return (None, "VIDEO_MEMBERS_ONLY")
    except AgeRestrictedError:
        return (None, "VIDEO_AGE_RESTRICTED")
    except VideoRegionBlocked:
        return (None, "VIDEO_REGION_BLOCKED")
    except LiveStreamError:
        return (None, "VIDEO_LIVE_STREAM")
    except VideoUnavailable:
        return (None, "VIDEO_UNAVAILABLE")
    except MaxRetriesExceeded:
        return (None, "TOO_MANY_REQUESTS")
    except RegexMatchError:
        return (None, "The provided URL is not a valid YouTube video URL")
    except Exception as e:
        logging.error(
            f"An unexpected error occurred. Video URL: {video_url}, Error: {e}"
        )

        return (None, "An unexpected error ocurred")
