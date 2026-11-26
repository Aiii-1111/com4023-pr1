import pygame
import numpy as np
import config

ROWS = config.INV_ROWS
COLS = config.INV_COLS
screen = pygame.display.set_mode((config.SCRN_WIDTH, config.SCRN_HEIGHT))

### using the actual values for the real screen resolution and size of the invaders in the actual game
### Screen Dimension / Grid Dimension
# grid_width_ratio = 256 / 176
# grid_height_ratio = 224 / 80
pre_grid_width = config.SCRN_WIDTH * 0.6
pre_grid_height = config.SCRN_HEIGHT * 0.25

# Calculates the size for the invaders based on how many chunks the grid needs to be divided into
## assume gaps are 33% invader width
invader_w = int(pre_grid_width / (COLS + (COLS - 1) * 0.3))
invader_h = int(pre_grid_height / (ROWS + (ROWS - 1) * 0.3))
# Calculates the size for the gaps inbetween invaders
gap_x = int(invader_w * 0.3)
gap_y = int(invader_h * 0.3)
# Actual grid size based purely on invaders and gaps
grid_width = (COLS * invader_w) + ((COLS - 1) * gap_x)
grid_height = (ROWS * invader_h) + ((ROWS - 1) * gap_y)

## x/y coords point to top left of grid
grid_x = (config.SCRN_WIDTH - grid_width) // 2 # middle of the grid is middle of the screen
grid_y = int(config.SCRN_HEIGHT * 0.1) # 10% down the screen

class Invader:
    def __init__(self):
        self.x = 0
        self.y = 0
    def set_pos(self, x, y):
        self.x = grid_x + x * (invader_w + gap_x)
        self.y = grid_y + y * (invader_h + gap_y)
    def render(self):
        pygame.draw.circle(screen, pygame.Color(255,255,255,255), (self.x, self.y), invader_h / 4, width=0)


class Grid:
    def __init__(self):
        self.grid = np.empty((ROWS,COLS), dtype=object)
        for r in range(ROWS):
            for c in range(COLS):
                self.grid[r,c] = Invader()
                self.grid[r,c].set_pos(c,r)
        # self.stepx = invader_w + gap_x
        # self.stepy = invader_h + gap_y
        self.direction = 1
        self.speed = 1
        self.stepx = 0
        self.stepy = 0
        self.tick = 0
        self.moveCount = 0

    def speedup(self):
        if self.speed >= 3:
            self.speed = 3
        else:
            self.speed += 1

    def move(self):
        if (self.moveCount == 4) or ((self.moveCount - 4) % 8 == 0): ## Only when the invader reaches the edge will the group go down
            self.stepy += 1
            self.stepx -= 1 * self.direction # This is needed to stop the invader from moving across the x axis when going down...
            self.direction = -1 * self.direction ## This changes the direction when going down
        for r in range(ROWS):
            for c in range(COLS):
                self.grid[r,c].set_pos(c + self.stepx,r + self.stepy)
        self.moveCount += 1
        print(f"move count is {self.moveCount}")
    def trigger_move(self, tick=0):

        self.tick = tick
        match (self.speed):
            case 1:
                if (self.tick % 55 == 0):
                    self.stepx += (1 * self.direction)
                    print(f"stepx = {self.stepx}")
                    self.move()



    def render(self):
        for a in self.grid:
            for b in a:
                b.render()
    def stdout(self):
        print(self.grid)
        for r in self.grid:
            for c in r:
                print(c.x, c.y)






# print(f"invader size: {invader_w}x{invader_h}, gaps: {gap_x}x{gap_y}, start position: ({grid_x}, {grid_y})")
#
# mygrid = Grid()
# mygrid.stdout()
