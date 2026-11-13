import pygame 

# 4:3 aspect ratio in 1080p
SCRN_HEIGHT = 1080 
SCRN_WIDTH = 1440

BG_COLOUR = "#3C3C3C"
# TEXT_COLOUR
# SPRITE_COLOUR


pygame.init()
pygame.display.set_caption("Space Invaders")
screen  = pygame.display.set_mode((SCRN_WIDTH,SCRN_HEIGHT))
screen.fill(BG_COLOUR)
pygame.display.update()

lives = 3

while lives > 0:
    screen.fill(BG_COLOUR)
    pygame.display.update()

pygame.quit()