# project/app/config.py

import logging
import os


log = logging.getLogger(__name__)


class Config:
    def __init__(self, environment: str, testing: bool):
        self.environment = environment
        self.testing = testing

    @classmethod
    def from_environ(cls):
        return cls(
            os.environ["ENVIRONMENT"],
            os.environ["TESTING"],
        )


log.info("Loading config settings from the environment...")
config = Config.from_environ()
