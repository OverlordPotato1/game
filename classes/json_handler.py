import json
import os


class JsonFile:
    def __init__(self, file):
        self.file = file

        if not os.path.exists(file):
            raise FileNotFoundError

    def fetch(self):
        file = self.file
        with open(file) as file:
            data = json.load(file)

        return data

    def write(self, new_data):
        with open(self.file, 'w') as file:
            json.dump(new_data, file, indent=4)
