import pygame
import config
import invaders
import importlib ### Ignore this, it will be removed
import sys

##########################
### This is purely for me because my computer keeps caching
### some pygame renders / objects every time I run it
if pygame.get_init():
    pygame.quit()

importlib.reload(config)
importlib.reload(invaders)
##########################

try:
    ############### Setup
    # 4:3 aspect ratio in 1080p
    # Updated this to use a config.py so variables can be accessed by any .py file
    SCRN_HEIGHT = config.SCRN_HEIGHT
    SCRN_WIDTH = config.SCRN_WIDTH
    # for placing score and life text
    TEXT_HORIZ_PADDING = 100
    TEXT_VERT_PADDING = 50
    # colours
    BG_COLOUR = "#191919"
    TEXT_COLOUR = "#F1E9DA"
    SPRITE_COLOUR = "#05F140"

    # initialise pygame and screen
    pygame.init()
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    screen  = pygame.display.set_mode((SCRN_WIDTH,SCRN_HEIGHT))
    screen.fill(BG_COLOUR)
    pygame.display.update()

    # setting up text to show score & lives
    game_font = pygame.font.Font("assets/Silkscreen-Regular.ttf", 30)

    lives = 3
    score = 0

    lives_text = game_font.render(f"Lives: {lives}", True, TEXT_COLOUR, BG_COLOUR)
    livestext_rect = lives_text.get_rect()
    livestext_rect.center = (TEXT_HORIZ_PADDING, TEXT_VERT_PADDING)

    score_text = game_font.render(f"Score: {score}", True, TEXT_COLOUR, BG_COLOUR)
    scoretext_rect = score_text.get_rect()
    scoretext_rect.center = (SCRN_WIDTH-TEXT_HORIZ_PADDING, TEXT_VERT_PADDING)
    grid = invaders.Grid()
    ############### Gameloop
    running = True
    while running and lives > 0:
        # fill screen and add text
        screen.fill(BG_COLOUR)
        screen.blit(lives_text, livestext_rect)
        screen.blit(score_text, scoretext_rect)

        grid.render()
        grid.move()
        #render screen contents
        pygame.display.update()
        clock.tick(15)
        # handle quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
finally:
    pygame.quit()
    # sys.exit()
