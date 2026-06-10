import pygame
import sys


def main():
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    pygame.init()
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    dog_image = pygame.image.load("02-DogBark/2dogs.jpg")
    dog_image = pygame.transform.scale(dog_image, (IMAGE_SIZE, IMAGE_SIZE))

    font_object_1 = pygame.font.SysFont("comicsansms", 28)

    # Get all of my fonts...
    fonts = pygame.font.get_fonts()
    for font in sorted(fonts):
        print(font)

    caption_1 = font_object_1.render("Two Dogs", True, BLACK)
    bark_sound = pygame.mixer.Sound("02-DogBark/bark.mp3")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                bark_sound.play()

        screen.fill(WHITE)
        screen.blit(dog_image, (0, 0))
        screen.blit(caption_1, (screen.get_width() / 2 - caption_1.get_width() / 2,
                                screen.get_height() - caption_1.get_height() + 2))
        pygame.display.update()


main()
