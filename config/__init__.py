import logging

from .bot_config import config as bot_cfg


def init_logger():
    handlers = [
        logging.StreamHandler(),
    ]

    logging.basicConfig(
        handlers=handlers,
        format="%(asctime)s - %(filename)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )
    logging.captureWarnings(capture=True)
