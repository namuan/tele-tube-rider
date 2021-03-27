import logging
import os
import youtube_dl as yt

from bot.extraction_params import create_extraction_params
from bot.exceptions import FileIsTooLargeException
from bot.telegram_notifier import TelegramNotifier


class Video:
    def __init__(self, video_info):
        self.info = video_info


class VideoProvider:
    def __init__(self, bot, chat_id):
        self.bot = bot
        self.chat_id = chat_id
        self.video_info = None

    def process(self, video_link, update_message_id):
        notifier = TelegramNotifier(self.bot, self.chat_id, update_message_id)
        yt_downloader = yt.YoutubeDL({"socket_timeout": 10})
        self.video_info = yt_downloader.extract_info(video_link, download=False)
        notifier.progress_update("‍🤖 processing video")
        request_handler = create_extraction_params(notifier)
        try:
            for yt_video in self.yt_videos():
                logging.info("Processing Video -> {}".format(yt_video.info.get("id")))
                for data in request_handler.process_video(yt_video.info):
                    filename = data["filename"]
                    video_file = open(filename, "rb")

                    notifier.progress_update(
                        "Almost there. Uploading {} 🔈".format(
                            os.path.basename(filename)
                        )
                    )

                    self.bot.send_chat_action(self.chat_id, "upload_video")
                    self.bot.send_video(
                        self.chat_id,
                        video_file,
                        caption="Downloaded using @jd",
                        timeout=120,
                    )
        except FileIsTooLargeException as e:
            file_too_large_error = "[File Is Too Large] {}".format(str(e))
            logging.error(file_too_large_error)
            self.bot.send_message(self.chat_id, file_too_large_error, disable_web_page_preview=True)
            return False
        except:
            return False

        notifier.progress_update("Done! ✅")
        return True

    def yt_videos(self):
        if not self.is_yt_playlist():
            yield Video(self.video_info)
        else:
            for entry in self.get_playlist_videos():
                yield Video(entry)

    def is_yt_playlist(self):
        if "playlist" in self.get_type():
            return True
        return False

    def get_playlist_videos(self):
        return self.video_info["entries"]

    def get_type(self):
        return self.video_info["extractor"]
