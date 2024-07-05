import json
import os
from pathlib import Path

class APIConfig:
    _config_path = os.path.abspath(f'{os.getcwd()}/config/config.json')
    _emailSettings = []

    def __init__(self) -> None:
        if Path(self._config_path).is_file():
            with open(self._config_path) as config:
                json_data = json.load(config)
                self._emailSettings = json_data["emailSettings"]
        else: 
            with open(self._config_path, 'w') as config:
                config.write('{"emailSettings": [{ "apikey": "", "email": "" }]}')
    
    def getEmail(self):
        pass
