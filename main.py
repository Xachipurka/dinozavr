import pygame
import random

pygame.init()
s = 0
dx, dy = 50, 300
drx, dry = 50, 50
dryz = dry

kry, krx = random.randrange(55, 80), random.randrange(45, 65)
kx, ky = 450, 400 - kry
kxz = kx
screen = pygame.display.set_mode((470, 500))
running = True


def collision(x, y, sizeX, sizeY, x2, y2, sizeX2, sizeY2):
    if (x + sizeX >= x2 and x2 + sizeX2 >= x) and (y + sizeY >= y2 and y2 + sizeY2 >= y):
        return True
    return False


while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if dy >= 400 - dry:
                    s = 2
            elif event.key == pygame.K_DOWN:
                # if event.key
                # if dry != dryz // 2:
                dry -= dry // 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                dry *= 2

        if event.type == pygame.QUIT:
            running = False

    if kx > -60:
        kx -= 0.5
    else:
        kry, krx = random.randrange(55, 80), random.randrange(45, 65)
        kx, ky = kxz, 400 - kry
    screen.fill('black')

    if collision(dx, dy, drx, dry, kx, ky, krx, kry):
        running = False

    pygame.draw.rect(screen, (255, 255, 255), (dx, dy, drx, dry))
    pygame.draw.rect(screen, (100, 100, 100), (0, 400, 500, 200))
    pygame.draw.rect(screen, (200, 200, 200), (kx, ky, krx, kry))

    if dy < 400 - dry:
        s -= 0.01
    elif s < 0:
        s = 0
    # print(s)

    dy -= s

    pygame.display.flip()
pygame.quit()
