import pygame

import barriers

# import bullet
import config
from player import Player

############### Setup
# 4:3 aspect ratio in 1080p
SCRN_HEIGHT = config.SCRN_HEIGHT
SCRN_WIDTH = config.SCRN_WIDTH
# for placing score and life text
TEXT_HORIZ_PADDING = 100
TEXT_VERT_PADDING = 50
# colours
BG_COLOUR = "#191919"
TEXT_COLOUR = "#F1E9DA"
SPRITE_COLOUR = config.SPRITE_COLOUR

# initialise pygame and screen
pygame.init()
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCRN_WIDTH, SCRN_HEIGHT))
screen.fill(BG_COLOUR)

game_font = pygame.font.Font("assets/Silkscreen-Regular.ttf", 30)


def update_game_text(game_variables):
    # setting up text to show score & lives

    lives_text = game_font.render(
        f"Lives: {game_variables['lives']}", True, TEXT_COLOUR, BG_COLOUR
    )
    livestext_rect = lives_text.get_rect()
    livestext_rect.center = (TEXT_HORIZ_PADDING, TEXT_VERT_PADDING)

    score_text = game_font.render(
        f"Score: {game_variables['score']}", True, TEXT_COLOUR, BG_COLOUR
    )
    scoretext_rect = score_text.get_rect()
    scoretext_rect.center = (SCRN_WIDTH - TEXT_HORIZ_PADDING, TEXT_VERT_PADDING)

    return lives_text, livestext_rect, score_text, scoretext_rect


pygame.display.update()


############### Gameloop
def game_loop():

    game_variables = {"lives": 3, "score": 0}
    player = Player()

    # text setup
    lives_text, livestext_rect, score_text, scoretext_rect = update_game_text(
        game_variables
    )

    # setting up barriers
    barrier_x = SCRN_WIDTH / 8
    barrier_y = SCRN_HEIGHT - 200
    barrier_list = []
    for i in range(4):
        barrier_list.append(barriers.Barrier(x=barrier_x, y=barrier_y))
        barrier_list[i].new_barrier_cluster()
        barrier_x += SCRN_WIDTH / 5

    while game_variables["lives"] > 0:
        # fill screen and add text
        screen.fill(BG_COLOUR)
        screen.blit(lives_text, livestext_rect)
        screen.blit(score_text, scoretext_rect)

        # draw and move player
        player.move()
        player.draw(screen)

        # draw and move bullets
        for bullet in player.bullets:
            bullet.move()
            bullet.draw(screen)

        # draw barriers
        for b in barrier_list:
            b.draw_barrier(surface=screen)

        # render screen contents
        pygame.display.update()
        clock.tick(60)
        # handle quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # allow player to shoot
            if event.type == pygame.KEYDOWN:  # noqa: SIM102
                if event.key == pygame.K_SPACE:
                    player.shoot()

    show_game_over()


# create text saying "GAME OVER" & allow retry
def show_game_over():
    gameover_text = game_font.render(
        "GAME OVER\n\npress any key to retry", True, TEXT_COLOUR, BG_COLOUR
    )
    gameover_rect = gameover_text.get_rect()
    gameover_rect.center = (int(SCRN_WIDTH / 2), int(SCRN_HEIGHT / 2))

    gameover = True

    while gameover:
        screen.fill(BG_COLOUR)
        screen.blit(gameover_text, gameover_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                gameover = False
    restart()


# reset all text/ variables & restart game_loop
def restart():
    game_loop()


game_loop()
