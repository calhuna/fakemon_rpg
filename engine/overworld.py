import pygame

TILE_SIZE = 32
PLAYER_SPEED = 4

class Overworld:
    def __init__(self, map_file):
        self.tileset = pygame.image.load("assets/tileset.png").convert()
        self.player_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.player_image.fill((255, 0, 0))  # Placeholder red square

        self.map = self.load_map(map_file)
        self.player_pos = [5, 5]
        self.camera_offset = [0, 0]

    def load_map(self, filename):
        with open(filename, "r") as f:
            return [list(line.strip()) for line in f]

    def update(self):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0

        if keys[pygame.K_LEFT]:
            dx = -1
        elif keys[pygame.K_RIGHT]:
            dx = 1
        elif keys[pygame.K_UP]:
            dy = -1
        elif keys[pygame.K_DOWN]:
            dy = 1

        if dx != 0 or dy != 0:
            new_x = self.player_pos[0] + dx
            new_y = self.player_pos[1] + dy
            if self.map[new_y][new_x] != "#":  # '#' = wall
                self.player_pos[0] = new_x
                self.player_pos[1] = new_y

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

        px, py = self.player_pos
        screen.blit(
            self.player_image,
            (px * TILE_SIZE, py * TILE_SIZE)
        )