import pygame

def main():
    pygame.init()
    pygame.display.set_caption("yatzy")
    screen = pygame.display.set_mode((640, 480))

    header = pygame.image.load("src/pictures/yatzypic.png")
    play = pygame.image.load("src/pictures/play.png")
    players = pygame.image.load("src/pictures/players.png")
    
    screen.fill((0, 0, 0))
    screen.blit(header, (70, 50))
    screen.blit(play, (170, 150))
    screen.blit(players, (150, 280))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if x > 225 and x < 414:
                    if y > 196 and y < 257:
                        screen.fill((0, 0, 0))
                if x > 171 and x < 474:
                    if y > 296 and y < 351:
                        screen.fill((0, 0, 0))

            pygame.display.flip()
            if event.type == pygame.QUIT:
                exit()

if __name__ == "__main__":
    main()