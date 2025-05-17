import random

class FakemonInstance:
    def __init__(self, fakemon_data, level=5):
        self.template = fakemon_data  # from FakemonLoader
        self.name = fakemon_data.name
        self.level = level
        self.current_exp = 0
        self.hp = self.calculate_stat("hp")
        self.current_hp = self.hp
        self.moves = self.get_learned_moves()
        self.ability = random.choice(fakemon_data.abilities)

    def calculate_stat(self, stat_name):
        base = self.template.base_stats[stat_name]
        # Simplified stat formula: floor((2 * base * level) / 100) + level + 10
        if stat_name == "hp":
            return ((2 * base * self.level) // 100) + self.level + 10
        else:
            return ((2 * base * self.level) // 100) + 5

    def get_learned_moves(self):
        learned = []
        for level, moves in sorted(self.template.moves.items(), key=lambda x: int(x[0])):
            if int(level) <= self.level:
                learned.extend(moves)
        return learned[-4:]  # Max 4 moves like in mainline Pokémon

    def is_fainted(self):
        return self.current_hp <= 0

    def __repr__(self):
        return f"{self.name} Lv.{self.level} HP:{self.current_hp}/{self.hp} Moves:{self.moves}"
