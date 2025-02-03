import logging
import os

class LogGen():
    @staticmethod
    def loggen():
        log_directory = os.path.abspath(os.curdir) + "\\..\\logs"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)  # Create the logs directory if it doesn't exist

        path = os.path.join(log_directory, 'automation.log')
        logging.basicConfig(filename=path,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger