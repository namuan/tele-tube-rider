import configparser
import os

WORKING_DIRECTORY_ABS_PATH = os.path.abspath(".")
AUDIO_OUTPUT_DIR_NAME = "output_dir"
AUDIO_OUTPUT_DIR = os.path.join(WORKING_DIRECTORY_ABS_PATH, AUDIO_OUTPUT_DIR_NAME)
OUTPUT_FORMAT = os.path.join(AUDIO_OUTPUT_DIR, "%(id)s.%(ext)s")
PREFERRED_AUDIO_CODEC = "mp4"


def config(key, default_value=None):
    c = configparser.ConfigParser()
    c.read("env.cfg")

    return c.get("ALL", key) or default_value
