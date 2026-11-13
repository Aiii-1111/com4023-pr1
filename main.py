import pygame 

# 4:3 aspect ratio in 1080p
SCRN_HEIGHT = 1080 
SCRN_WIDTH = 1440
TEXT_HORIZ_PADDING = 100
TEXT_VERT_PADDING = 50 

BG_COLOUR = "#3C3C3C"
TEXT_COLOUR = "#F1E9DA"


pygame.init()
pygame.display.set_caption("Space Invaders")
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

while lives > 0:
    # fill screen and add text
    screen.fill(BG_COLOUR)
    screen.blit(lives_text, livestext_rect)
    screen.blit(score_text, scoretext_rect)
    #render screen
    pygame.display.update()

pygame.quit()