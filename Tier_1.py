from random import *
import numpy as np
from graphics import *
import time
from obj import *

class Tier_1(obj):
    def __init__(self, X=0, Y=0, ID=0 , Size = 3, Body = [],C_Body=[]):
        super().__init__(X=X, Y=Y, ID=ID)
        self.size = Size
        self.c_body = C_Body

        def bd(Size):
            body = [(self.x,self.y)]
            while True:
                x_from,y_from= body[-1]
                Size -= 1
                if Size < 1:
                    break
                possible_next = [(x_from +1 , y_from),
                                      (x_from -1 , y_from),
                                      (x_from , y_from +1),
                                      (x_from , y_from- 1)]
                for pos in possible_next:
                    if pos[0] < 0 or pos[1] < 0:
                        possible_next.remove(pos)
                for pos_to in possible_next:
                    for pos_from in body:
                        if pos_to == pos_from:
                            if pos_to in possible_next:
                                possible_next.remove(pos_to)
                rnd = choice(possible_next)
                body.append(rnd)

            return body

        if Body == []:
            self.body = bd(Size)
        else:
            self.body = Body

    def move_randome(self):
        b = np.array(self.body)
        direction = [np.array([0,1]),
                     np.array([0,-1]),
                     np.array([1,0]),
                     np.array([-1,0])]
        rnd = choice(direction)
        for i in range(len(b)):
            b[i] += rnd
        self.body = b
        return rnd

    def draw(self, window , dis = 10 , radius=5 , colors = ["black","blue","red"]):
        self.c_body = []
        rnd_color = choice(colors)
        for x,y in self.body:
            c = Circle(Point(x*dis,y*dis),radius)
            c.setFill(rnd_color)
            self.c_body.append(c)
        for circ in self.c_body:
            circ.draw(window)

    def move_circ(self,dis = 10 , count = 0, sleep = 0):
        counter = 0
        while True:
            rnd = self.move_randome()
            for circ in self.c_body :
                circ.move(rnd[0]*dis,rnd[1]*dis)
                time.sleep(sleep)
            if count == 0:
                counter -= 1
            else:
                counter += 1
            if counter > count:
                break
        #win.close()