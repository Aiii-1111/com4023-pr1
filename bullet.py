import pygame


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.colour = (255, 255, 0)

    def move(self):
        self.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, 5, 15))

    # the bullet list is being stored in player.py
