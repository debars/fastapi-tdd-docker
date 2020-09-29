# project/app/config.py

import logging
import os


class Config:
    def __init__(self, environment: str, testing: bool, loglevel: str):
        self.environment = environment
        self.testing = testing
        levels = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }
        self.loglevel = levels[loglevel]

    @classmethod
    def from_environ(cls):
        return cls(
            os.environ["ENVIRONMENT"],
            os.environ["TESTING"],
            os.environ["LOGLEVEL"],
        )

config = Config.from_environ()
log = logging.getLogger(__name__)
log.setLevel(config.loglevel)
# create console handler and set level to debug
logpath = os.path.join('.', 'my.log')
fh = logging.FileHandler(logpath)
fh.setLevel(config.loglevel)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to console handler
fh.setFormatter(formatter)

# add console handler to logger
log.addHandler(fh)
log.info("Loading config settings from the environment...")
