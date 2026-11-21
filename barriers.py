import pygame

class Barrier(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.health = 5
        #coordinates for the bottom left corner of a whole barrier cluster
        self.__x_anchor = x
        self.__y_anchor = y
        self.shape = [[True,True,True,True,True],
                    [True,False,False,False,True]]
        self.block_size = 25
        self.sub_blocks = []
        
    def get_x(self):
        return self.__x_anchor
    def get_y(self):
        return self.__y_anchor
    
    def new_barrier_cluster(self, surface: pygame.Surface, color: str):
        rect_y = self.get_y()
        for y in range(len(self.shape)):
            rect_x = self.get_x()
            for x in range(len(self.shape[y])):
                if self.shape[y][x]:
                    self.sub_blocks.append(pygame.draw.rect(surface=surface, color=color, rect=pygame.Rect(rect_x,rect_y,self.block_size,self.block_size)))
                rect_x += self.block_size
            rect_y += self.block_size
    
    def draw_barrier(self, surface, color):
        for i in range(len(self.sub_blocks)):
            pygame.draw.rect(surface=surface, color=color, rect=self.sub_blocks[i])
            
    def take_damage(self):
        self.health -=1