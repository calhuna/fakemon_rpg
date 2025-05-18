import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 255, 255)

    def update(self, map_data, game):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and map_data[self.y-1][self.x] == 'G': self.y -= 1
        elif keys[pygame.K_DOWN] and map_data[self.y+1][self.x] == 'G': self.y += 1
        elif keys[pygame.K_LEFT] and map_data[self.y][self.x-1] == 'G': self.x -= 1
        elif keys[pygame.K_RIGHT] and map_data[self.y][self.x+1] == 'G': self.x += 1

        # trigger a test battle
        if self.x == 7 and self.y == 7:
            game.start_battle('Wild Embercub')

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x * 32, self.y * 32, 32, 32))
