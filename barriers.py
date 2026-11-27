import pygame

block_size = 25
barrier_blocks = pygame.sprite.Group()


class BarrierBlock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.health = 5
        self.image = pygame.image.load(f"assets/barrierSprites/health{self.health}.png")
        self.size = block_size
        self.rect = pygame.Rect(x, y, self.size, self.size)

    def take_damage(self):
        self.health -= 1

        self.image = pygame.image.load(f"assets/barrierSprites/health{self.health}.png")

        if self.health == 0:
            self.kill()
            print("block destroyed")


class Barrier:
    # barriers made up of several "blocks" made using the pygame sprite class
    def __init__(self, x: int, y: int):
        # self.group =
        # coordinates for the bottom left corner of a whole barrier cluster
        self.__x_anchor = x
        self.__y_anchor = y
        self.shape = [
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
        ]
        self.sub_blocks = pygame.sprite.Group()

    def get_x(self):
        return self.__x_anchor

    def get_y(self):
        return self.__y_anchor

    def new_barrier_cluster(self):
        rect_y = self.get_y()
        for y in range(len(self.shape)):
            rect_x = self.get_x()
            for x in range(len(self.shape[y])):
                if self.shape[y][x]:
                    new_block = BarrierBlock(rect_x, rect_y)
                    # self.sub_blocks.append(new_block)
                    self.sub_blocks.add(new_block)
                rect_x += block_size

            rect_y += block_size

    def draw_barrier(self, surface: pygame.Surface):
        for block in self.sub_blocks:
            surface.blit(block.image, block.rect)
