import pygame

pygame.init()
max_x = 1000
max_y = 620
win = pygame.display.set_mode((max_x, max_y))
pygame.display.set_caption("Chase")
x = 100
y = 100
baddyX = 300
baddyY = 300

baddyX1 = 600
baddyY1= 500
vel = 6
baddyVel = 4
run = True
run1 = True
width = 20
daddy_width = 40

def draw_game():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, width))
    pygame.draw.rect(win, (255, 0, 0), (baddyX, baddyY, daddy_width, daddy_width))
    pygame.draw.rect(win, (255, 0, 0), (baddyX1, baddyY1, daddy_width, daddy_width))

    pygame.display.update()


while run and run1:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x - vel < 0:
            x=0
        else:
            x -= vel

    draw_game()
