import logging
import os

import yaml

from utils.decorate import singleton

log = logging.getLogger(__name__)


@singleton
class ConfigUtils:
    app_config = {}

    def parse_config(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'rt') as f:
                self.app_config = yaml.safe_load(f.read())
        else:
            log.error("%s not found.", file_path)
            raise ValueError("Config file: {} not found".format(file_path))
        return self.app_config

    def get_config(self):
        if not self.app_config:
            log.warning("app_config is empty, make sure to call "
                        "parse_config() before get_config() ")
        return self.app_config
