import datetime
import logging
import os
import re
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

import emoji
from colorama import Fore
from utils.config import Config


def remove_emoji(string: str) -> str:  # Entfernt Emoji und macht es für den Computer lesbar
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F1E0-\U0001F1FF"
        "\U00002500-\U00002587"
        "\U00002589-\U00002BEF"
        "\U00002702-\U000027B0"
        "\U00002702-\U000027B0"
        "\U000024C2-\U00002587"
        "\U00002589-\U0001F251"
        "\U0001f926-\U0001f937"
        "\U00010000-\U0010ffff"
        "\u2640-\u2642"
        "\u2600-\u2B55"
        "\u200d"
        "\u23cf"
        "\u23e9"
        "\u231a"
        "\ufe0f"
        "\u3030"
        "\u231b"
        "\u2328"
        "\u23cf"
        "\u23e9"
        "\u23ea"
        "\u23eb"
        "\u23ec"
        "\u23ed"
        "\u23ee"
        "\u23ef"
        "\u23f0"
        "\u23f1"
        "\u23f2"
        "\u23f3"
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r"", string)


class CustomFormatter(logging.Formatter):
    def __init__(self, fmt, datefmt=None):
        super().__init__(fmt, datefmt)
        self.fmt = fmt
        self.datefmt = datefmt

        self.FORMATS = {
            logging.DEBUG: Fore.LIGHTCYAN_EX + fmt + Fore.RESET,
            logging.INFO: Fore.LIGHTYELLOW_EX + fmt + Fore.RESET,
            logging.WARNING: Fore.LIGHTRED_EX + fmt + Fore.RESET,
            logging.ERROR: Fore.LIGHTRED_EX + fmt + Fore.RESET,
            logging.CRITICAL: Fore.LIGHTRED_EX + fmt + Fore.RESET}

    def format(self, record):

        record.emoji_is_present = (
            record.emoji_is_present if hasattr(record, "emoji_is_present") else False)

        if (
                hasattr(record, "emoji")
        ):
            record.msg = emoji.emojize(
                f"{record.emoji}  {record.msg.strip()}"
            )
            record.emoji_is_present = True

        if "\u2192" in record.msg:
            record.msg = record.msg.replace("\u2192", "-->")

            record.msg = remove_emoji(record.msg)
        log_fmt = self.FORMATS.get(record.levelno)
        logging.Formatter.__init__(self, fmt=log_fmt, datefmt=self.datefmt)
        return super().format(record)


logger = logging.getLogger("Backend")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(
    CustomFormatter(fmt=f"%(asctime)s - %(levelname)s: %(message)s", datefmt="%d/%m/%y %H:%M:%S")
)


def save():
    logs_path = os.path.join(Path().absolute(), "logs")
    Path(logs_path).mkdir(parents=True, exist_ok=True)
    logs_file = os.path.join(
        logs_path,
        f"{datetime.datetime.now().strftime('%d-%m-%Y %H-%M-%S')}.log",
    )
    file_handler = TimedRotatingFileHandler(
        logs_file,
        when="D",
        interval=1,
        backupCount=7,
        encoding="utf-8",
        delay=False)
    file_handler.setFormatter(
        logging.Formatter(
            fmt="%(asctime)s - %(levelname)s: %(message)s",
            datefmt="%d/%m/%y %H:%M:%S"))
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)


if Config().logs:
    save()

logger.addHandler(console_handler)
