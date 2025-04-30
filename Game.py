import pygame

pygame.init()

BG = (0,50,0,)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.Rect((400,300,25,25))
run = True
while run:

    screen.fill(BG)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] :
        player.move_ip(-1,0)
    elif key[pygame.K_d] :
        player.move_ip(1,0)
    elif key[pygame.K_w] :
        player.move_ip(0,-1)

    pygame.draw.rect(screen,(0,100,0),player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()#Hello Idiot
import pygame

pygame.init()

BG = (0,50,0,)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.Rect((400,300,25,25))
run = True
while run:

    screen.fill(BG)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] :
        player.move_ip(-1,0)
    elif key[pygame.K_d] :
        player.move_ip(1,0)
    elif key[pygame.K_w] :
        player.move_ip(0,-1)

    pygame.draw.rect(screen,(0,100,0),player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
