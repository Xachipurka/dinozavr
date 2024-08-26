import time
import pygame
import random


with open('record.txt', 'r', encoding='utf-8') as file:
    record = float(file.readline())

pygame.init()
time_start = time.perf_counter()
s = 0
dx, dy = 50, 300
drx, dry = 70, 70
dryz = dry
time_tex1 = time.perf_counter()
tex_number = 0

kry, krx = [random.randrange(40, 55)], [random.randrange(30, 40)]
kx, ky = [450], [400 - kry[0]]
screen = pygame.display.set_mode((470, 500))
running = True
time_random = random.randrange(2, 4)


def collision(x, y, sizeX, sizeY, x2, y2, sizeX2, sizeY2):
    if (x + sizeX >= x2 and x2 + sizeX2 >= x) and (y + sizeY >= y2 and y2 + sizeY2 >= y):
        return True
    return False

tex_cact = pygame.image.load("cact.PNG")

tex_din = [pygame.image.load("din1.PNG"), pygame.image.load("din2.PNG"), pygame.image.load('din.jpeg'), pygame.image.load('din3.PNG')]
tex_din[0] = pygame.transform.scale(tex_din[0], (drx, dry))
tex_din[1] = pygame.transform.scale(tex_din[1], (drx, dry))
tex_din[2] = pygame.transform.scale(tex_din[2], (drx, dry))
tex_din[3] = pygame.transform.scale(tex_din[3], (drx, dry / 2))

tex_bird = [pygame.image.load("bird1.PNG"), pygame.image.load("bird2.PNG")]
tex_bird[0] = pygame.transform.scale(tex_bird[0], (50, 20))
tex_bird[1] = pygame.transform.scale(tex_bird[1], (50, 20))


time1 = time.perf_counter()

font = pygame.font.Font(None, 20)

sitting = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if dy >= 400 - dry:
                    s = 2
            elif event.key == pygame.K_DOWN:
                dry -= dry // 2
                sitting = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                dry *= 2
                sitting = False

        if event.type == pygame.QUIT:
            running = False
    time2 = time.perf_counter()

    if time2 - time1 > time_random:
        if random.randrange(3) == 0:
            kry.append(20)
            krx.append(50)
            kx.append(450)
            ky.append(340)
        else:
            kry.append(random.randrange(50, 80))
            krx.append(random.randrange(40, 60))
            kx.append(450)
            ky.append(400 - kry[-1])
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

    screen.fill('black')

    for i in range(len(kry)):
        if collision(dx, dy, drx, dry, kx[i], ky[i], krx[i], kry[i]):
            running = False

    time_tex2 = time.perf_counter()
    if time_tex2 - time_tex1 > 0.1:
        time_tex1 = time.perf_counter()
        if tex_number == 0:
            tex_number = 1
        elif tex_number == 1:
            tex_number = 0

    if sitting:
        screen.blit(tex_din[3], (dx, dy))
    else:
        screen.blit(tex_din[tex_number], (dx, dy))

    pygame.draw.rect(screen, (100, 100, 100), (0, 400, 500, 200))

    for i in range(len(kry)):
        if ky[i] == 340:
            t = int((time.perf_counter() - time_start) / 0.3) % 2
            screen.blit(tex_bird[t], (kx[i], ky[i]))
        else:
            tex_cact1 = pygame.transform.scale(tex_cact, (krx[i], kry[i]))
            screen.blit(tex_cact1, (kx[i], ky[i]))

    if dy < 400 - dry:
        s -= 0.01
        tex_number = 2
    elif s < 0:
        s = 0
        if tex_number != 3:
            tex_number = 0


    dy -= s
    time_current = time.perf_counter() - time_start

    text_time = font.render(f'Time: {round(time_current,  1)}', True, (255, 255, 255))
    text_record = font.render(f'Record: {record}', True, (255, 255, 255))

    screen.blit(text_time, (20, 30))
    screen.blit(text_record, (370, 30))



    pygame.display.flip()
pygame.quit()
time_current = round(time.perf_counter() - time_start, 1)
if time_current > record:
    with open('record.txt', 'w', encoding='utf-8') as file:
        file.write(str(time_current))