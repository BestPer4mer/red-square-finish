import pygame

pygame.init()

win = pygame.display.set_mode((1280,720))

pygame.display.set_caption("Preppers Canada Fam")

x = 200
y = 250
width = 60
height = 50
vel = 5

run = True
while run:
    print('sfd')
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0),(x, y, width, height))
    pygame.display.update()

input('Please ENTER to exit')


