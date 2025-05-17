import pygame
from engine.overworld import Overworld
from screens.wild_battle import WildBattleScreen

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fakemon RPG")

clock = pygame.time.Clock()
overworld = Overworld("data/map1.txt")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    overworld.update()
    overworld.draw(screen)

    pygame.display.flip()
    clock.tick(60)

    def main():
        pygame.init()
        screen = pygame.display.set_mode((640, 400))
        pygame.display.set_caption("Fakemon Battle Test")

        battle_screen = WildBattleScreen(screen)
        battle_screen.run()

        pygame.quit()

pygame.quit()