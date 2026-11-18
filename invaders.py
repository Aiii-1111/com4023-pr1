import pygame
import numpy as np
import config

### using the actual values for the real screen resolution and size of the invaders in the actual game
grid_width_ratio = 256 / 176
grid_height_ratio = 224 / 80

x_interv = (config.SCRN_WIDTH - 12) // 11
y_interv = config.SCRN_HEIGHT // (2*5)

interv = min(x_interv,y_interv) # Finds the smallest default interval and uses that for both (usually y will be smallest)



class invader:
    def __init__(Self, i, j):
        # Assuming top left is 0,0
        Self.size = (16,16)
class grid:
    def __init__(Self):
        Self.grid = np.full((5,11),"_")
        Self.direction = 1
        Self.speed = 1
    def speedup(Self):
        Self.speed += 1
