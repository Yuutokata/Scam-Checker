import json


class Config:
    def __init__(self):
        file = open("config.json", "r")

        config = json.load(file)

        self.ip = config["ip"]
        self.port = config["port"]

        self.safeSearch = config["safeSearch"]

        self.logs = config["logs"]
