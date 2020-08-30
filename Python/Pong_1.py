import sys
import pygame
from pygame.locals import QUIT

from paddle import Paddle

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,50,50)
GREEN = (50,255,50)
BLUE = (50,50,255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG GAME")

paddleA = Paddle(RED, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(BLUE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200


all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)


# The loop wil carry on until the user exit the game
carryOn = True

clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.MoveUp(5)
    if keys[pygame.K_s]:
        paddleA.MoveDown(5)
    if keys[pygame.K_UP]:
        paddleB.MoveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.MoveDown(5)
    
    all_sprites_list.update()

    screen.fill(BLACK)
    pygame.draw.line(screen, GREEN, [349, 0], [349,500],5)
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
