import pygame
from PIL import Image
from pygame.math import Vector2

from sussy_baka import SussyBaka

pygame.init()
pygame.display.set_caption("SusApple")

WIDTH = 1600
HEIGHT = 900

BAKA_ROWS = 40
BAKA_COLS = 40

screen = pygame.display.set_mode((WIDTH, HEIGHT))
alpha_surf = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
clock = pygame.time.Clock()

running = False
FPS = 60

bakas = []
for baka_num in range(1200):
    x = baka_num % BAKA_ROWS
    y = baka_num // BAKA_COLS
    bakas.append(SussyBaka(screen, Vector2(x * 40, y * 30), baka_num + y, False))

time = 0.1
start_time = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            running = True
            start_time = pygame.time.get_ticks() / 1000
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    if running:
        frame = str(round(time * 30))
        with Image.open(f'frames/{frame.zfill(7)}.png') as image:
            pixels = image.load()
            for baka_num in range(1200):
                x = baka_num % BAKA_ROWS
                y = baka_num // BAKA_COLS
                pixel = pixels[x, y]
                if pixel[0] + pixel[1] + pixel[2] < 384:  # extremely advanced color detection
                    bakas[baka_num].black = True
                else:
                    bakas[baka_num].black = False

        for baka in bakas:
            baka.draw(round(time * 20))

        screen.blit(alpha_surf, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)
        time = pygame.time.get_ticks() / 1000 - start_time
