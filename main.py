import time
import pygame
import random

pygame.init()
s = 0
dx, dy = 50, 300
drx, dry = 50, 50
dryz = dry

kry, krx = [random.randrange(40, 60)], [random.randrange(20, 40)]
kx, ky = [450], [400 - kry[0]]
kxz = kx.copy()
screen = pygame.display.set_mode((470, 500))
running = True
time_random = random.randrange(1, 5)


def collision(x, y, sizeX, sizeY, x2, y2, sizeX2, sizeY2):
    if (x + sizeX >= x2 and x2 + sizeX2 >= x) and (y + sizeY >= y2 and y2 + sizeY2 >= y):
        return True
    return False


time1 = time.perf_counter()

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if dy >= 400 - dry:
                    s = 2
            elif event.key == pygame.K_DOWN:
                dry -= dry // 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                dry *= 2

        if event.type == pygame.QUIT:
            running = False
    time2 = time.perf_counter()

    if time2 - time1 > time_random:
        kry.append(random.randrange(55, 80))
        krx.append(random.randrange(55, 80))
        kx.append(450)
        ky.append(400 - kry[-1])
        kxz.append(kx[-1])
        time1 = time.perf_counter()
        time_random = random.randrange(1, 4)
    for i in range(len(kry) - 1, -1, -1):
        if kx[i] > -60:
            kx[i] -= 0.5
        else:
            del krx[i]
            del kry[i]
            del kx[i]
            del ky[i]
            del kxz[i]

    screen.fill('black')

    for i in range(len(kry)):
        if collision(dx, dy, drx, dry, kx[i], ky[i], krx[i], kry[i]):
            running = False

    pygame.draw.rect(screen, (255, 255, 255), (dx, dy, drx, dry))
    pygame.draw.rect(screen, (100, 100, 100), (0, 400, 500, 200))

    for i in range(len(kry)):
        pygame.draw.rect(screen, (200, 200, 200), (kx[i], ky[i], krx[i], kry[i]))

    if dy < 400 - dry:
        s -= 0.01
    elif s < 0:
        s = 0

    dy -= s

    pygame.display.flip()
pygame.quit()
