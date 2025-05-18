import pygame
import json

class Battle:
    def __init__(self, game, enemy_name):
        self.game = game
        self.enemy_name = enemy_name
        with open('data/pokemon.json') as f:
            self.pokemon_data = {p['name']: p for p in json.load(f)}
        self.enemy = self.pokemon_data.get(enemy_name, {'name': enemy_name, 'hp': 30})

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.game.end_battle()

    def draw(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 0, 0), (400, 100, 200, 20))
        font = pygame.font.Font(None, 24)
        text = font.render(f"Encountered {self.enemy['name']}! (HP: {self.enemy['hp']})", True, (255, 255, 255))
        screen.blit(text, (50, 300))