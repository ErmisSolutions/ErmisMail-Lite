import json
from pathlib import Path

class Config:
    _config_path = "config/config.json"
    _cors = []
    def __init__(self) -> None:
        if Path(self._config_path).is_file():
            with open(self._config_path) as config:
                json_data = json.load(config)
                if len(json_data["cors"]) > 0:
                    for url in json_data["cors"]:
                        self._cors.append(url["url"])
                else:
                    self._cors = ['.']
        else: 
            with open(self._config_path, 'w') as config:
                config.write('{"mail": {"server": "","port": "","username": "","password": "","from": "","to": ""},"cors": [{"url": "."}]}')
        
    def Cors(self):
        return self._cors