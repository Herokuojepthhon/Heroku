import os
import logging
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "herokumngr.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):
    LOGGER = True

    TG_BOT_TOKEN = "5326314788:AAGyf49DiE3oD7LmxMJvJTTy0dH2Mih86yY"

    OWNER_ID = int("631110062")

    # Get from my.telegram.org
    API_ID = int("6877733")

    # Get from my.telegram.org
    API_HASH = "0d0d6f66a34f26af1693cd16169dea04"

    DONATION_LINK = None
    WORKERS = 8


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
