import pygame
from engine.overworld import Overworld
from engine.battle import Battle

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.state = 'overworld'
        self.overworld = Overworld(self)
        self.battle = None

    def update(self):
        if self.state == 'overworld':
            self.overworld.update()
        elif self.state == 'battle':
            self.battle.update()

    def draw(self):
        if self.state == 'overworld':
            self.overworld.draw(self.screen)
        elif self.state == 'battle':
            self.battle.draw(self.screen)

    def start_battle(self, enemy_pokemon):
        from engine.battle import Battle
        self.battle = Battle(self, enemy_pokemon)
        self.state = 'battle'

    def end_battle(self):
        self.state = 'overworld'
