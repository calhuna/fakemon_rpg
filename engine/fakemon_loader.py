import os
import json

FAKEMON_DATA_PATH = "data/fakemon"

class Fakemon:
    def __init__(self, data):
        self.name = data["name"]
        self.id = data["id"]
        self.types = data["types"]
        self.base_stats = data["base_stats"]
        self.exp_yield = data["exp_yield"]
        self.evolution = data["evolution"]
        self.abilities = data["abilities"]
        self.moves = data["moves"]

    def __repr__(self):
        return f"<Fakemon {self.name} (#{self.id})>"

def load_all_fakemon():
    fakemon_db = {}
    for filename in os.listdir(FAKEMON_DATA_PATH):
        if filename.endswith(".json"):
            with open(os.path.join(FAKEMON_DATA_PATH, filename), "r") as f:
                data = json.load(f)
                fakemon = Fakemon(data)
                fakemon_db[fakemon.name] = fakemon
    return fakemon_db
