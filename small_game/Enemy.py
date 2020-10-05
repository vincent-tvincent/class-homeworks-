from Player import Player
import random
class Enemy(Player):
    def __init__(self,map,data,accelerate,code,block_code,motivation):
        super().__init__(map,data,accelerate,code,block_code)
        self.motivation = motivation
        self.status = ("+","-","*")
    def random_move(self):
        return self.status[random.randint(0,len(self.status) - 1)]
    def move(self,x_direction,y_direction):
        velocity = self.velocity
        x_move = True
        y_move = True
        if self.motivation["accelerate"]:
            velocity *= self.accelerate
        if x_direction == "*":
            x_move = False
        if y_direction == "*":
            y_move = False
        if x_move:
            super().move("x",velocity,x_direction)
        if y_move:
            super().move("y",velocity,y_direction)

    def hit_edge(self):
        x_move = True
        y_move = True
        if self.motivation["X move"] != "*":
            x_move = self.can_move("x",self.motivation["X move"])
        if self.motivation["Y move"] != "*":
            y_move = self.can_move("y",self.motivation["Y move"])
        return x_move and y_move

    def wandering(self):
        if self.motivation["turn"]:
            self.motivation["X move"] = self.random_move()
            self.motivation["Y move"] = self.random_move()
            self.motivation["turn"] = False
        else:
            self.motivation["turn"] = self.hit_edge()
        self.move(self.motivation["X move"],self.motivation["Y move"])








