from RUL_prediction import logger
from RUL_prediction.entity.config_entity import PrepareCallbacksConfig


class PrepareCallbacks:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    def run(self):
        logger.info("Prepare callbacks stage completed (not required for sklearn RUL model)")
