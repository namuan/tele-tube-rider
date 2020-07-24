from bot.media_request_handler import MediaRequestHandler
from config.bot_config import OUTPUT_FORMAT

YOUTUBE_EXTRACT_VIDEO_PARAMS = {
    "outtmpl": OUTPUT_FORMAT,
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
    "socket_timeout": 10,
    "retries": 10,
    "prefer_ffmpeg": True,
    "keepvideo": True,
}


def create_extraction_params(notifier):
    extraction_param = YOUTUBE_EXTRACT_VIDEO_PARAMS
    return MediaRequestHandler(extraction_param, notifier)


def is_yt_video(extractor):
    return extractor == "youtube"
