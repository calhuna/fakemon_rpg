import pygame
from engine.map_loader import load_map
from engine.player import Player

class Overworld:
    def __init__(self, game):
        self.game = game
        self.map_data = load_map('data/map1.txt')
        self.player = Player(5, 5)

    def update(self):
        self.player.update(self.map_data, self.game)

    def draw(self, screen):
        screen.fill((0, 128, 0))
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                color = (100, 200, 100) if tile == 'G' else (150, 150, 255)
                pygame.draw.rect(screen, color, (x*32, y*32, 32, 32))
        self.player.draw(screen)
