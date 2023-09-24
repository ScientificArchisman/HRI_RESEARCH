import logging
import os
import datetime


LOG_NAME = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.log"
LOG_PATH = os.path.join(os.getcwd(), "logs", LOG_NAME)

os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)



logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

if __name__ == "__main__":
    logging.info("This is an information log")
    logging.warning("This is a warning log")
    logging.error("This is an error log")
    logging.critical("This is a critical log")