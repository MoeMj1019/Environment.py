from Tier_1 import *

class Stick_man(Tier_1):
    def __init__(self, X=0, Y=0, ID=0 , Size = 3, colors = ["black"]):
        super().__init__(X=X, Y=Y, ID=ID,colors=colors)
        sticker_body = [(1.5,9),(4.5,9),(2,8),(4,8),(2.5,7),(3.5,7),(1,6),(3,6),(5,6),(1.5,5),(3,5),(4.5,5),(2,4),(3,4),(4,4),(3,3),(3,2),(2,1),(3,1),(4,1),(3,0)]
        self.body = []
        for x,y in sticker_body:
            x_new = x + self.x
            y_new = y + self.y
            self.body.append((x_new, y_new))
    pass
