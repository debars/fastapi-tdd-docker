# project/app/config.py

import logging
import os


class Config:
    def __init__(self, environment: str, testing: bool, database_url):
        self.environment = environment
        self.testing = testing
        self.database_url = database_url

    @classmethod
    def from_environ(cls):
        return cls(
            os.environ["ENVIRONMENT"],
            os.environ["TESTING"],
            os.environ["DATABASE_URL"],
        )

    def log(self):
        return self.log


class Logger():
    def __init__(self, loglevel=logging.DEBUG):
        self._log = logging.getLogger(__name__)
        self._log.setLevel(loglevel)
        # create console handler and set level to debug
        logpath = os.path.join('.', 'my.log')
        fh = logging.FileHandler(logpath)
        fh.setLevel(loglevel)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to console handler
        fh.setFormatter(formatter)

        # add console handler to logger
        self._log.addHandler(fh)

    @property
    def log(self):
        return self._log


config = Config.from_environ()
logger = Logger()
logger.log.info("Loading config settings from the environment...")
