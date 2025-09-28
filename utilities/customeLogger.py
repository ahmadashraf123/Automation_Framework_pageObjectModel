import os
import logging

class LogGen:
    @staticmethod
    def loggen():
        log_dir = os.path.join(os.getcwd(), "Logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(log_dir, "automation.log")

        logging.basicConfig(
            filename=log_file,
            format="%(asctime)s:%(levelname)s:%(message)s",
            datefmt='%m%d%y %I:%M:%S %p',
            force=True  # ⬅️ Add this to force logging config
        )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
