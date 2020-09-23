import pygame
import random
pygame.init()
max_x = 1000 # width of window
max_y = 620 # height of window
win = pygame.display.set_mode((max_x, max_y))
pygame.display.set_caption("Chase")
x = 100 # x coordinate
y = 100 # y coordinate
baddyX = 300 # block 0 x start point
baddyY = 300 # block 0 y start point

baddyX1 = 600 # block 1 x start point
baddyY1 = 500 # block 1 y start point
vel = 6 # volicity of player  
baddyVel = 25 #velocity of blocks
run = True
run1 = True
width = 20 # width of player
daddy_width = 40 # block width


def draw_game():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, width))
    pygame.draw.rect(win, (255, 0, 0), (baddyX, baddyY, daddy_width, daddy_width))
    pygame.draw.rect(win, (255, 0, 0), (baddyX1, baddyY1, daddy_width, daddy_width))

    pygame.display.update()


while run and run1:
    pygame.time.delay(10)

    move_of_baddy = random.randint(0,4)
    move_of_baddy1 = random.randint(0,4)

    if move_of_baddy == 0 and baddyX + baddyVel  < max_x:
        baddyX += baddyVel
    elif move_of_baddy == 1 and baddyX - baddyVel > 0:
        baddyX -= baddyVel
    elif move_of_baddy == 2 and baddyY + baddyVel < max_y:
        baddyY += baddyVel
    elif move_of_baddy == 3 and baddyY - baddyVel > 0:
        baddyY -= baddyVel

    if move_of_baddy1 == 0 and baddyX1 + baddyVel < max_x:
        baddyX1 += baddyVel
    elif move_of_baddy1 == 1 and baddyX1 - baddyVel > 0:
        baddyX1 -= baddyVel
    elif move_of_baddy1 == 2 and baddyY1 + baddyVel < max_y:
        baddyY1 += baddyVel
    elif move_of_baddy1 == 3 and baddyY1 - baddyVel > 0:
        baddyY1 -= baddyVel

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    #read keyboard and do operation
    if keys[pygame.K_a]:
        if x - vel < 0:
            x = 0
        else:
            x -= vel

    if keys[pygame.K_d]:
        if x + vel > max_x:
            x = max_x
        else:
            x += vel

    if keys[pygame.K_w]:
        if y - vel < 0:
            y = 0
        else:
            y -= vel

    if keys[pygame.K_s]:
        if y + vel > max_y:
            y = max_y
        else:
            y += vel



    draw_game()
