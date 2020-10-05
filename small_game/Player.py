import pygame
import copy
class Player:

    def __init__(self,map,data,accelerate,code,block_code,enemy_code = -1):
        self.x = data["x"]
        self.y = data["y"]
        self.width = data["width"]
        self.velocity = data["velocity"]
        self.color = data["color"]
        self.accelerate = accelerate
        self.code = code
        self.block_code = block_code
        self.enemy_code = enemy_code
        self.window = data["window"]
        self.map = map

    def print_data(self,velocity):
        print("x: " + str(self.x)+ " " + "y: " + str(self.y) + "\n" + "velocity: " + str(velocity))
# if have no block at front

    def can_move(self,dimension,direction = "+"):
        if dimension == "x" and direction == "+":
            return self.map.get_point(self.x + int(self.width/2) + 1,self.y) != self.block_code
        elif dimension == "x" and direction == "-":
            return self.map.get_point(self.x - int(self.width/2) - 1, self.y) != self.block_code
        elif dimension == "y" and direction == "+":
            return self.map.get_point(self.x, self.y + int(self.width/2) + 1) !=self.block_code
        elif dimension == "y" and direction == "-":
            return self.map.get_point(self.x, self.y - int(self.width/2) - 1) !=self.block_code
# if caught by enemy

    def if_die(self):
        if self.enemy_code >0:
            block = self.map.scan(self.x,self.y,self.width)
            for i in block:
                if i == self.enemy_code():
                    return False
        return True
# get options

    def get_move(self,direction,accelerate):
        velocity = self.velocity
        if accelerate:
            velocity *= self.accelerate
            print("accelerate activated ")
            self.print_data(velocity)

        if direction == "left":
            self.move("x",velocity,"-")
            print("get left move")
            self.print_data(velocity)
        if direction == "right":
            self.move("x",velocity)
            print("get right move")
            self.print_data(velocity)
        if direction == "up":
            self.move("y",velocity,"-")
            print("get up move")
            self.print_data(velocity)
        if direction == "down":
            self.move("y",velocity)
            print("get down move")
            self.print_data(velocity)


    def __linear_move(self,dimension,velocity,direction = "+"):
        displacement = velocity
        if direction == "-":
            displacement = -displacement
        if dimension == "x" and self.can_move(dimension,direction):
            self.x += displacement
        elif dimension == "y" and self.can_move(dimension,direction):
            self.y += displacement
# move the player

    def move(self,dimension,velocity,direction = "+"):
        length = self.window["length"]
        width = self.window["width"]
        if dimension == "x":
            if self.x + velocity > length - self.width:
                self.x = length - self.width
            else:
                self.__linear_move(dimension, self.velocity, direction)
            if self.x - velocity < self.width:
                self.x = self.width
            else:
                self.__linear_move(dimension, velocity, direction)
        elif dimension == "y":
            if self.y + velocity > width - self.width:
                self.y = width - self.width
            else:
                self.__linear_move(dimension, velocity, direction)
            if self.y - velocity < self.width:
                self.y = self.width
            else:
                self.__linear_move(dimension, velocity, direction)

# get the data set of this object

    def get_data(self):
        return {"x":self.x, "y":self.y, "width":self.width,"length": self.width,"color":self.color,
                "velocity":self.velocity, "code":self.code,"visual": (self.x-int(self.width/2),
                                                                      self.y-int(self.width/2),self.width,self.width),
                "draw_x":self.x-int(self.width/2),"draw_y":self.y-int(self.width/2)}




        


