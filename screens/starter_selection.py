import pygame
import os
from engine.fakemon_loader import load_all_fakemon
from engine.fakemon_instance import FakemonInstance
from engine.player_party import PlayerParty

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BOX_COLOR = (200, 200, 255)
HOVER_COLOR = (170, 170, 230)

STARTER_NAMES = ["Flaruff", "Buddrip", "Sparkoil"]
SPRITE_FOLDER = "assets/fakemon"

class StarterSelectionScreen:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 28)
        self.running = True
        self.fakemon_db = load_all_fakemon()
        self.party = PlayerParty()
        self.selected_index = -1
        self.sprites = self.load_sprites()

    def load_sprites(self):
        sprites = {}
        for name in STARTER_NAMES:
            path = os.path.join(SPRITE_FOLDER, f"{name.lower()}.png")
            try:
                img = pygame.image.load(path).convert_alpha()
                sprites[name] = pygame.transform.scale(img, (64, 64))
            except:
                print(f"Missing sprite for {name}")
                sprites[name] = None
        return sprites

    def draw_box(self, rect, name, hovered):
        pygame.draw.rect(self.screen, HOVER_COLOR if hovered else BOX_COLOR, rect)
        pygame.draw.rect(self.screen, BLACK, rect, 2)

        # Draw sprite
        sprite = self.sprites.get(name)
        if sprite:
            self.screen.blit(sprite, (rect.x + rect.width // 2 - 32, rect.y + 10))

        # Draw name
        name_text = self.font.render(name, True, BLACK)
        self.screen.blit(name_text, (rect.x + rect.width // 2 - name_text.get_width() // 2, rect.y + 80))

    def run(self):
        box_rects = []
        spacing = 40
        width = 150
        height = 120
        start_x = 100
        start_y = 150

        for i in range(len(STARTER_NAMES)):
            rect = pygame.Rect(start_x + i * (width + spacing), start_y, width, height)
            box_rects.append(rect)

        while self.running:
            self.screen.fill(WHITE)

            title = self.font.render("Choose your starter Fakemon!", True, BLACK)
            self.screen.blit(title, (220, 60))

            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()[0]

            for i, rect in enumerate(box_rects):
                hovered = rect.collidepoint(mouse_pos)
                self.draw_box(rect, STARTER_NAMES[i], hovered)

                if hovered and mouse_click:
                    self.selected_index = i
                    self.choose_starter()
                    self.running = False

            pygame.display.flip()
            self.clock.tick(60)

        return self.party

    def choose_starter(self):
        name = STARTER_NAMES[self.selected_index]
        if name in self.fakemon_db:
            starter = FakemonInstance(self.fakemon_db[name], level=5)
            self.party.add_fakemon(starter)
