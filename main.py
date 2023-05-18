import logging
import logging.handlers
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
    TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
except KeyError:
    TELEGRAM_TOKEN = "Telegram token not available!"
    TELEGRAM_CHAT_ID = "Telegram chat ID not available!"
    logger.info("ENV variable not available!")
    #raise


if __name__ == "__main__":
    message = "🚩 Schedule test from GERALT_py."

    r = requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}")
    if r.status_code == 200:
        # print(r.json())
        logger.info(f'Message sent to telegram bot channel: {message}')

