import pygame

pygame.init()

x = 0
y = 0
drx, dry = 50, 50
screen = pygame.display.set_mode((470, 500))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y >= 400 - dry:
                    y -= 250
            elif event.key == pygame.K_DOWN:
                dry -= dry // 2
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    pygame.draw.rect(screen, (255, 255, 255), (x, y, drx, dry))
    pygame.draw.rect(screen, (0, 255, 0), (0, 400, 500, 200))

    if y < 400 - dry:
        y += 1


    pygame.display.flip()
pygame.quit()