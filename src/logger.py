import logging
from config import LOG_FILE

logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def log(message, level="info"):
    if level == "info":
        logging.info(message)
    elif level == "error":
        logging.error(message)