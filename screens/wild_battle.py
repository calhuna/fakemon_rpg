# screens/wild_battle.py

import pygame
from engine.battle_engine import Battle
from engine.fakemon_loader import load_all_fakemon
from engine.fakemon_instance import FakemonInstance

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HP_GREEN = (80, 200, 120)
HP_RED = (220, 60, 60)
HP_BAR_BG = (100, 100, 100)
MSG_BOX_COLOR = (230, 230, 230)

class WildBattleScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 24)
        self.clock = pygame.time.Clock()

        # Fakemon setup
        self.fakedex = load_all_fakemon()
        self.player_fakemon = FakemonInstance(self.fakedex["Flaruff"], level=5)
        self.player_fakemon.moves = ["Ember", "Tackle"]
        self.enemy_fakemon = FakemonInstance(self.fakedex["Buddrip"], level=5)
        self.enemy_fakemon.moves = ["Vine Whip", "Tackle"]

        self.battle = Battle(self.player_fakemon, self.enemy_fakemon)
        self.message = "A wild Buddrip appeared!"
        self.move_selected = None

    def draw_hp_bar(self, x, y, width, height, hp, max_hp):
        pygame.draw.rect(self.screen, HP_BAR_BG, (x, y, width, height))
        hp_ratio = hp / max_hp
        color = HP_GREEN if hp_ratio > 0.5 else HP_RED
        pygame.draw.rect(self.screen, color, (x, y, int(width * hp_ratio), height))

    def draw_text_box(self, text):
        pygame.draw.rect(self.screen, MSG_BOX_COLOR, (20, 320, 600, 60))
        pygame.draw.rect(self.screen, BLACK, (20, 320, 600, 60), 2)
        rendered = self.font.render(text, True, BLACK)
        self.screen.blit(rendered, (30, 340))

    def draw_ui(self):
        self.screen.fill(WHITE)

        # Enemy info
        self.draw_hp_bar(400, 50, 180, 20, self.enemy_fakemon.current_hp, self.enemy_fakemon.max_hp)
        enemy_name = self.font.render(self.enemy_fakemon.base.name, True, BLACK)
        self.screen.blit(enemy_name, (400, 30))

        # Player info
        self.draw_hp_bar(100, 220, 180, 20, self.player_fakemon.current_hp, self.player_fakemon.max_hp)
        player_name = self.font.render(self.player_fakemon.base.name, True, BLACK)
        self.screen.blit(player_name, (100, 200))

        # Move buttons
        for i, move_name in enumerate(self.player_fakemon.moves):
            rect = pygame.Rect(320 + (i % 2) * 140, 260 + (i // 2) * 40, 130, 30)
            pygame.draw.rect(self.screen, (200, 200, 255), rect)
            pygame.draw.rect(self.screen, BLACK, rect, 2)
            label = self.font.render(move_name, True, BLACK)
            self.screen.blit(label, (rect.x + 10, rect.y + 5))

        # Message box
        self.draw_text_box(self.message)

    def handle_click(self, pos):
        for i, move_name in enumerate(self.player_fakemon.moves):
            rect = pygame.Rect(320 + (i % 2) * 140, 260 + (i // 2) * 40, 130, 30)
            if rect.collidepoint(pos):
                self.move_selected = move_name

    def run(self):
        running = True
        while running:
            self.draw_ui()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            if self.move_selected and not self.battle.battle_over:
                self.message = self.battle.take_turn(self.move_selected)
                pygame.time.delay(600)
                if not self.battle.battle_over:
                    self.message = self.battle.take_turn(None)
                self.move_selected = None

            self.clock.tick(60)
