import pygame
#initialise pygame
pygame.init()

#create game window
screen = pygame.display.set_mode((800, 600))
#game title 
pygame.display.set_caption("Space Invaders")

#player starting position
player_x = 375
player_y = 500
#player speed
player_speed = 0.25

#creating the loop so the window stays
running = True

while running:
    #player movement left and right
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 750:
        player_x += player_speed
    #exit code for closing the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    #draw player
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, 50, 30))

    pygame.display.flip()

pygame.quit()