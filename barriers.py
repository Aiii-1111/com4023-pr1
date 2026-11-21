import pygame

class Barrier(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.health = 5
        self.x = x
        self.y = y
        self.shape = [[True,True,True,True],
                    [True,False,False,True]]
        self.size = 50
        self.rect_base = pygame.Rect(x, y, self.size, self.size)
        self.subrects = []
        
    def new_barrier(self, surface: pygame.Surface, color: str):
        for y in range(len(self.shape)):
            for x in range(len(self.shape[y])):
                if self.shape[y][x]:
                    self.subrects.append(pygame.draw.rect(surface=surface, color=color, rect=self.rect_base))
        print(self.subrects)
    
    def draw_barrier(self, surface, color):
        for i in range(len(self.subrects)):
            pygame.draw.rect(surface=surface, color=color, rect=self.subrects[i])