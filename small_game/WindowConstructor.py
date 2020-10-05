import pygame
import numpy
class Map:
    def __init__(self,x,y):
        self.map = numpy.zeros((y,x)).astype("int64")

    def __set_range(self,start,length,max):
        if start + length > max:
            return range(start,max)
        else:
            return range(start,start + length)

# make a rectangle area on the map

    def make_rectangle_block(self,data,number):
        for Y in self.__set_range(data["draw_y"],data["width"],len(self.map)):
            for X in self.__set_range(data["draw_x"],data["length"],len(self.map[Y])):
                    self.map[Y][X] = number

# get the identify code at one point

    def get_point(self,x,y):
        return self.map[y][x]

# get if one point is full with assigned identify code

    def found_item(self,x,y,code):
        if self.map[y][x] == code:
            return True
        return False

# get a data set of a gaven region

    def scan(self,x,y,width):
        result = ()
        for Y in self.__set_range(y,width,len(self.map)):
            for X in self.__set_range(x,width,len(self.map[Y])):
                    result += self.map[Y][X]
        return result


class Window(Map):
    def __init__(self,window,data):
        self.length = data["length"]
        self.width = data["width"]
        self.color = data["color"]
        self.window = window
        super().__init__(self.length,self.width)
# construct one object on the world map

    def draw_rectangle(self,data,code):
        pygame.draw.rect(self.window,data["color"],data["visual"])
        self.make_rectangle_block(data,code)
# get the map of the world

    def get_map(self):
        return self.map
# get data set of this object

    def get_data(self):
        return {"length": self.length,"width": self.width, "color": self.color}









