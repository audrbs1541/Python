import pygame
BLACK = (0,0,0)
WHITE = (255,255,255)

class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
    
    def MoveUp(self, pixels):
        self.rect.y -= pixels

        if self.rect.y <0:
            self.rect.y = 0
    
    def MoveDown(self, pixels):
        self.rect.y += pixels

        if self.rect.y >400:
            self.rect.y = 400

    def MoveLeft(self, pixels, lim_L):
        self.rect.x -= pixels

        if self.rect.x <lim_L:
            self.rect.x = lim_L

    def MoveRight(self, pixels, lim_R):
        self.rect.x += pixels

        if self.rect.x >lim_R:
            self.rect.x = lim_R    

        
