# engine/type_chart.py

TYPE_EFFECTIVENESS = {
    ("Fire", "Grass"): 2.0,
    ("Water", "Fire"): 2.0,
    ("Grass", "Water"): 2.0,
    ("Fire", "Water"): 0.5,
    ("Water", "Grass"): 0.5,
    ("Grass", "Fire"): 0.5,
}

def get_effectiveness(move_type, target_type):
    return TYPE_EFFECTIVENESS.get((move_type, target_type), 1.0)