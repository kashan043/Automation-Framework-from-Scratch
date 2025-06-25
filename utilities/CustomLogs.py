# utilities/logger.py
import logging
import os
from datetime import datetime

class LogGen:
    LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Logs")
    LOG_FILE = os.path.join(LOG_DIR, f"automation_{datetime.now():%Y-%m-%d}.log")

    @staticmethod
    def loggen(name="automation"):
        # 1️⃣ make sure Logs/ exists
        os.makedirs(LogGen.LOG_DIR, exist_ok=True)

        # 2️⃣ create a logger (one per name)
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        # 3️⃣ avoid adding multiple handlers on repeated calls
        if not logger.handlers:
            fh = logging.FileHandler(LogGen.LOG_FILE, mode="a")
            fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            fh.setFormatter(fmt)
            logger.addHandler(fh)

        return logger
