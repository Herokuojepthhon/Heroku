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
    # LOGGER = True

    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1725624123:AAEk5bSDRZoWpECQf3CAgrjBPEB6esHmXx8")

    OWNER_ID = int(os.environ.get("OWNER_ID", "631110062"))

    # Get from my.telegram.org
    API_ID = int(os.environ.get("APP_ID", "3607361"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "c57bcc4b09591db4f90f60b469e8870f")

    DONATION_LINK = None
    WORKERS = 8


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
