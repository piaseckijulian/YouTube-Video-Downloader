import io
import os
from os import environ

from dotenv import load_dotenv
from flask import Flask, request, send_file
from flask_cors import CORS
from pytube import YouTube
from pytube.exceptions import (
    AgeRestrictedError,
    LiveStreamError,
    MembersOnly,
    VideoPrivate,
    VideoRegionBlocked,
    VideoUnavailable,
)
from pytube.innertube import _default_clients

load_dotenv()

app = Flask(__name__)
CORS(app)


# Unblocking restricted content
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]


@app.route("/downloadVideo")
def downloadVideo():
    video_url = request.args.get("url")

    if not video_url:
        return {"error": "URL_PARAMETER_MISSING"}, 400

    try:
        video = YouTube(video_url)

        stream = video.streams.get_highest_resolution()
        video_path = stream.download()

        with open(video_path, "rb") as file:
            # Save the content of the video file to video_data
            video_data = file.read()

        # Remove the video file
        os.remove(video_path)

        return send_file(
            io.BytesIO(video_data),
            as_attachment=True,
            download_name=f"{video.title}.mp4",
            mimetype="video/mp4",
        )

    except VideoPrivate:
        return {
            "error": "VIDEO_PRIVATE",
        }, 400
    except MembersOnly:
        return {
            "error": "VIDEO_MEMBERS_ONLY",
        }, 400
    except AgeRestrictedError:
        return {
            "error": "VIDEO_AGE_RESTRICTED",
        }, 400
    except VideoRegionBlocked:
        return {
            "error": "VIDEO_BLOCKED_REGION",
        }, 400
    except LiveStreamError:
        return {
            "error": "VIDEO_LIVE_STREAM",
        }, 400
    except VideoUnavailable:
        return {
            "error": "VIDEO_UNAVAILABLE",
        }, 400
    except Exception:
        return {"error": "Error during downloading video"}, 500


isProd = bool(environ.get("PROD"))

# Production
if __name__ == "__main__" and isProd:
    from waitress import serve

    serve(app, host="0.0.0.0", port=5000)
