# engine/move_data.py

MOVE_DATA = {
    "Tackle": {"power": 40, "accuracy": 100, "type": "Normal"},
    "Ember": {"power": 40, "accuracy": 100, "type": "Fire"},
    "Water Gun": {"power": 40, "accuracy": 100, "type": "Water"},
    "Vine Whip": {"power": 45, "accuracy": 100, "type": "Grass"},
}

def get_move(name):
    return MOVE_DATA.get(name)