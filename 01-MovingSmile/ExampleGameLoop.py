import pygame
import sys

pygame.init()
pygame.display.set_caption("Dave Fisher")
screen = pygame.display.set_mode((600, 400))

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(pygame.Color("Gray"))
    pygame.draw.circle(screen, pygame.Color("Yellow"), (50, 50), 25)
    pygame.draw.circle(screen, (255, 0, 0), (screen.get_width() / 2, screen.get_height() / 2), 100)
    pygame.draw.circle(screen, (255, 255, 0), (0, screen.get_height()), 100)
    pygame.display.update()
