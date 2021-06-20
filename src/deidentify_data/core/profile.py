import json
import yaml
import inspect

class Profile:
    def __init__(self):
        self.columns = None

    def from_file(self,
                  file_path: str):
        assert file_path.endswith('.json')
        with open(file_path ) as file:
            return json.load(file)

    def make_adjustment(self,
                        adjustment: dict) -> dict:
        pass
