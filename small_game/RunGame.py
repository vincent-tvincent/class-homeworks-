# Since I found a bug appeared when the character hit the edge of window, I set the limitation that every character
# can not attach the edge of the window.

from pygame import *
from WindowConstructor import *
from Player import Player
from Enemy import Enemy
import pygame

run = True # if continue the loop
pygame.init()

# construct the world map of the game
World_width= 800#Y
World_length= 800#X
World_color= (255,255,255)#RGB

# data of the player
Player_x = int(World_width/2)
Player_y = int(World_length/2)
Player_width = 45
Player_velocity = 5
Player_color =(0,102,102)
Player_accelerate = 5
Player_keys_setting = {"left": pygame.K_a,"right": pygame.K_d, "up": pygame.K_w, "down": pygame.K_s,
                       "accelerate": pygame.K_LSHIFT}
# data of the enemy
Enemy_x = 10
Enemy_y = 10
Enemy_width = Player_width
Enemy_velocity = Player_velocity
Enemy_color = (255,128,0)
Enemy_accelerate = Player_accelerate
Enemy_motivation = {"X move": "+", "Y move": "+","turn": False,"accelerate": False}
# data of blocks
Block_color = (200,200,200)
Block_1 = {"color": Block_color, "visual": (150,80,100,100),"draw_x": 150,"draw_y": 80,"width": 100, "length": 100}

# identify code of each item
ID_block = 1
ID_player = 2
ID_enemy = 3

# cancel out the bug appeared
World_length += int(2*Player_width)
World_width += int(2*Player_width)
World = pygame.display.set_mode((World_length,World_width))

# prepare the data for accessed by functions
World_data_set = {"width": World_width , "length": World_length, "color": World_color}
Player_data_set = {"window": World_data_set,"x": Player_x,"y": Player_y,"width": Player_width,"length": Player_width,
                   "velocity": Player_velocity,"color": Player_color}
Enemy_data_set = {"window": World_data_set,"x": Enemy_x,"y": Enemy_y,"width": Enemy_width,"length": Enemy_width,
                  "velocity": Enemy_velocity,"color": Enemy_color}
ID_set = {"block": ID_block,"player": ID_player, "enemy": ID_enemy}

# construct elements of the game
World_map = Window(World,World_data_set)
Player = Player(World_map,Player_data_set,Player_accelerate,ID_player,ID_block,ID_enemy)
Enemy = Enemy(World_map,Enemy_data_set,Enemy_accelerate,ID_enemy,ID_block,Enemy_motivation)
clock = pygame.time.Clock()

# functions
def make_block(x,y,length,width):
    return {"color": Block_color, "visual": (x,y,length,width),"draw_x": x,"draw_y": y,"width": width, "length": length}

def get_id(x,y):
    return World_map.get_map()[y][x]

def reverse_color(color):
    return (255 - color[0],255 - color[1],255 - color[2])

def if_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def read_move(key_setting):
    keys = pygame.key.get_pressed()
    accelerate = False
    if keys[key_setting["accelerate"]]:
        accelerate = True
        Player.color = reverse_color(Player_data_set["color"])
    else:
        Player.color = Player_data_set["color"]
    if keys[key_setting["left"]]:
        Player.get_move("left",accelerate)
    if keys[key_setting["right"]]:
        Player.get_move("right",accelerate)
    if keys[key_setting["up"]]:
        Player.get_move("up",accelerate)
    if keys[key_setting["down"]]:
        Player.get_move("down",accelerate)

def draw_frame():
    World.fill(World_data_set["color"])
    World_map.draw_rectangle(Player.get_data(),ID_player)
    World_map.draw_rectangle(Enemy.get_data(),ID_enemy)
    pygame.display.update()


# create one frame for the game
while run:
    pygame.time.delay(0)
    run = Player.if_die()
    run = if_quit()
    read_move(Player_keys_setting)
    Enemy.wandering()
    clock.tick(120)  # limit the refresh rate to 120 fps
    draw_frame()
    print("code: " + str(get_id(Block_1["draw_x"], Block_1["draw_y"])))

