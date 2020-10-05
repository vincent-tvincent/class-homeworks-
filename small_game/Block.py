class Block:
    def __init__(self,color,x,y,length,width):
        self.block = {"color": color, "visual": (x, y, length, width), "draw_x": x, "draw_y": y, "width": width,
         "length": length}
# get data set of Block

    def get_data(self):
        return self.block