# engine/battle_engine.py

import random
from engine.type_chart import get_effectiveness
from engine.move_data import get_move

class Battle:
    def __init__(self, player_fakemon, enemy_fakemon):
        self.player = player_fakemon
        self.enemy = enemy_fakemon
        self.battle_over = False
        self.turn = "player"

    def attack(self, attacker, defender, move_name):
        move = get_move(move_name)
        if not move:
            return f"{attacker.base.name} tried to use {move_name}, but it failed."

        if random.randint(1, 100) > move["accuracy"]:
            return f"{attacker.base.name}'s attack missed!"

        effectiveness = get_effectiveness(move["type"], defender.base.type1)
        damage = int(((2 * attacker.level / 5 + 2) * move["power"] * (attacker.current_stats['atk'] / max(defender.current_stats['def'], 1))) / 50 + 2)
        damage = int(damage * effectiveness)
        defender.current_hp = max(defender.current_hp - damage, 0)

        result = f"{attacker.base.name} used {move_name}! It dealt {damage} damage."
        if effectiveness > 1.0:
            result += " It's super effective!"
        elif effectiveness < 1.0:
            result += " It's not very effective."

        if defender.current_hp == 0:
            result += f"\n{defender.base.name} fainted!"
            self.battle_over = True

        return result

    def take_turn(self, player_move):
        if self.battle_over:
            return "Battle is already over."

        log = ""
        if self.turn == "player":
            log = self.attack(self.player, self.enemy, player_move)
            self.turn = "enemy"
        elif self.turn == "enemy":
            enemy_move = random.choice(self.enemy.moves)
            log = self.attack(self.enemy, self.player, enemy_move)
            self.turn = "player"

        return log