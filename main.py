import pygame, sys, os
from zombie.superstar import superstar

main_dir = os.path.split(os.path.abspath(__file__))[0]
width = 1024
height = 768
screen_size = (width, height)

pygame.init()

pygame.display.set_caption('pvz')
screen = pygame.display.set_mode(screen_size)
file = os.path.join(main_dir, "images", 'background.png')
backgroup = pygame.image.load(file).convert()
file = os.path.join(main_dir, "images", 'plant.png')
plant = pygame.image.load(file).convert_alpha()
plant = pygame.transform.scale(plant, (120, 180))


def main():
    Superstar = superstar(1)
    block = pygame.time.Clock()
    index = 0

    while 1:
        block.tick(20)
        screen.blit(backgroup, (0, 0))
        # screen.blit(plant, (0, 0))
        if index >= 100:
            index = 0
        screen.blit(plant, (80, 60))
        screen.blit(Superstar.images[index % 8], Superstar.rect)
        print(Superstar.rect)
        if Superstar.move():
            Superstar.move()
        print(Superstar.rect)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        index += 1


if __name__ == '__main__':
    main()
