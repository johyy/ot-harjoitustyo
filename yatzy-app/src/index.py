import pygame

def main():
    pygame.init()
    pygame.display.list_modes()
    screen = pygame.display.set_mode((640, 480))

    header = pygame.image.load("src/yatzypic.png")
    
    screen.fill((0, 0, 0))
    screen.blit(header, (80, 50))
    pygame.display.flip()


    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                exit()

if __name__ == "__main__":
    main()

