import pygame
from pygame.math import Vector2
from pygame.surface import Surface

white_bakas = []
black_bakas = []
for x in range(6):
    white_bakas.append(pygame.image.load(f'bakas/W{x + 1}.png'))
    black_bakas.append(pygame.image.load(f'bakas/B{x + 1}.png'))


class SussyBaka:
    def __init__(self, screen: Surface, position: Vector2, personal_offset: int, black: bool):
        self.screen = screen
        self.position = position
        self.personal_offset = personal_offset
        self.black = black

    def draw(self, time_offset: int):
        offset = (time_offset + self.personal_offset) % 6
        if self.black:
            self.screen.blit(black_bakas[offset], self.position)
        else:
            self.screen.blit(white_bakas[offset], self.position)
