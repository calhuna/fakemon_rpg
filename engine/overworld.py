import pygame

TILE_SIZE = 32
ANIMATION_SPEED = 0.1

class Overworld:
    def __init__(self, map_file):
        self.tileset = pygame.image.load("assets/tileset.png").convert()
        self.map = self.load_map(map_file)

        self.player_spritesheet = pygame.image.load("assets/characters/player.png").convert_alpha()
        self.player_direction = "down"
        self.player_frame = 0
        self.frame_timer = 0

        self.directions = {"down": 0, "left": 1, "right": 2, "up": 3}
        self.player_pos = [5, 5]

    def load_map(self, filename):
        with open(filename, "r") as f:
            return [list(line.strip()) for line in f]

    def get_player_sprite(self):
        row = self.directions[self.player_direction]
        col = int(self.player_frame)
        sprite = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
        sprite.blit(self.player_spritesheet, (0, 0), (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        return sprite

    def update(self):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0

        if keys[pygame.K_LEFT]:
            dx = -1
            self.player_direction = "left"
        elif keys[pygame.K_RIGHT]:
            dx = 1
            self.player_direction = "right"
        elif keys[pygame.K_UP]:
            dy = -1
            self.player_direction = "up"
        elif keys[pygame.K_DOWN]:
            dy = 1
            self.player_direction = "down"

        if dx != 0 or dy != 0:
            new_x = self.player_pos[0] + dx
            new_y = self.player_pos[1] + dy
            if self.map[new_y][new_x] != "#":
                self.player_pos[0] = new_x
                self.player_pos[1] = new_y
                self.frame_timer += ANIMATION_SPEED
                if self.frame_timer >= 1:
                    self.player_frame = (self.player_frame + 1) % 3
                    self.frame_timer = 0
            else:
                self.player_frame = 1  # Idle frame
        else:
            self.player_frame = 1  # Idle frame

    def draw(self, screen):
        screen.fill((0, 0, 0))
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                color = (100, 200, 100) if tile == "." else (50, 50, 50)
                pygame.draw.rect(
                    screen,
                    color,
                    (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                )

        sprite = self.get_player_sprite()
        px, py = self.player_pos
        screen.blit(sprite, (px * TILE_SIZE, py * TILE_SIZE))