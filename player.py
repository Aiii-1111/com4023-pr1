import pygame

from bullet import Bullet


class Player:
    def __init__(self):
        self.x = 375
        self.y = 540
        self.speed = 2.5
        self.bullets = []

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < 750:
            self.x += self.speed

    def shoot(self):
        bullet_x = self.x + 22
        bullet_y = self.y - 20
        self.bullets.append(Bullet(bullet_x, bullet_y))

    def update_bullets(self):
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.y < -15:
                self.bullets.remove(bullet)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 50, 30))
        pygame.draw.rect(screen, (0, 255, 0), (self.x + 15, self.y - 10, 20, 10))
        pygame.draw.rect(screen, (0, 255, 0), (self.x + 23, self.y - 20, 4, 10))
        for bullet in self.bullets:
            bullet.draw(screen)
