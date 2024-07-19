import json
import os
from pathlib import Path

class APIConfig:
    _config_path = os.path.abspath(f'{os.getcwd()}/config/config.json')
    _emailSettings = []

    def __init__(self) -> None:
        if not Path(self._config_path).is_file():
            with open(self._config_path, 'w') as config:
                config.write('{"emailSettings": [{ "apikey": "", "email": "", "redirect": "" }]}')
    
    def getSettings(self, key):
        self.loadConfig()
        try:
            for item in self._emailSettings:
                if key == item["apikey"]:
                    return (item["email"], item["redirect"])
            return None
        except Exception as ex:
            return None

    def loadConfig(self):
        with open(self._config_path) as config:
            json_data = json.load(config)
            self._emailSettings = json_data["emailSettings"]
