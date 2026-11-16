import pygame

class Barrier(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.health = 5
        self.shape = [[1,1,1,1],
                    [1,0,0,1]]
        self.size = 10
        self.rect = pygame.Rect(x, y, self.size, self.size)