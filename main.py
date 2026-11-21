import pygame
import barriers

############### Setup
# 4:3 aspect ratio in 1080p
SCRN_HEIGHT = 768#*0.75
SCRN_WIDTH = 1024#*0.75
# for placing score and life text
TEXT_HORIZ_PADDING = 100
TEXT_VERT_PADDING = 50 
# colours in RGB format
BG_COLOUR = (25, 25, 25) # Hex: #191919
TEXT_COLOUR = (241, 233, 218) # Hex: #F1E9DA
SPRITE_COLOUR = (5, 241, 64) # Hex: #05F140

# initialise pygame and screen
pygame.init()
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
screen  = pygame.display.set_mode((SCRN_WIDTH,SCRN_HEIGHT))
screen.fill(BG_COLOUR)

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

# setting up barriers 

b = barriers.Barrier(50,50)
b.new_barrier(screen, SPRITE_COLOUR)

pygame.display.update()
############### Gameloop
while lives > 0:
    # fill screen and add text
    screen.fill(BG_COLOUR)
    screen.blit(lives_text, livestext_rect)
    screen.blit(score_text, scoretext_rect)
    #barriers
    b.draw_barrier(surface=screen,color=SPRITE_COLOUR)
    
#render screen contents
    pygame.display.update()
    clock.tick(60)
    # handle quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

pygame.quit()