import pygame
from engine.game import Game

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
game = Game(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.update()
    game.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()