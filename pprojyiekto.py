from random import *
import matplotlib.pyplot as plt
import numpy as np
from graphics import *
import time
from Stick_man import *
from Tier_1 import *
from obj import *
from threading import Thread


# class obj:
#     def __init__(self, X=0, Y=0, ID=0):
#         self.x = X
#         self.y = Y
#         self.id = ID
#
#     def xUP(self, var):
#         self.x += var
#     def xDown(self, var):
#         self.x -= var
#
#     def yUP(self, var):
#         self.y += var
#     def yDown(self, var):
#         self.y -= var
#
#     def getX(self):
#         return self.x
#     def getY(self):
#         return self.Y
#
#
#
# class A(obj):
#     def __init__(self, X=0, Y=0, ID=0 , Size = 3, Body = [],C_Body=[]):
#         super().__init__(X=X, Y=Y, ID=ID)
#         #self.x = X
#         #self.y = Y
#         #self.id = ID
#         self.size = Size
#         self.c_body = C_Body
#
#         def bd(Size):
#             body = [(self.x,self.y)]
#             while True:
#                 x_from,y_from= body[-1]
#                 Size -= 1
#                 if Size < 1:
#                     break
#                 possible_next = [(x_from +1 , y_from),
#                                       (x_from -1 , y_from),
#                                       (x_from , y_from +1),
#                                       (x_from , y_from- 1)]
#                 for pos in possible_next:
#                     if pos[0] < 0 or pos[1] < 0:
#                         possible_next.remove(pos)
#                 for pos_to in possible_next:
#                     for pos_from in body:
#                         if pos_to == pos_from:
#                             if pos_to in possible_next:
#                                 possible_next.remove(pos_to)
#                 rnd = choice(possible_next)
#                 body.append(rnd)
#
#             return body
#
#         if Body == []:
#             self.body = bd(Size)
#         else:
#             self.body = Body
#
#     def move_randome(self):
#         b = np.array(self.body)
#         direction = [np.array([0,1]),
#                      np.array([0,-1]),
#                      np.array([1,0]),
#                      np.array([-1,0])]
#         rnd = choice(direction)
#         #print(rnd)
#         for i in range(len(b)):
#             b[i] += rnd
#         self.body = b
#         return rnd
#
#     def draw(self, window , dis = 10 , radius=5 , colors = ["black","blue","red"]):
#         self.c_body = []
#         rnd_color = choice(colors)
#         for x,y in self.body:
#             c = Circle(Point(x*dis,y*dis),radius)
#             c.setFill(rnd_color)
#             self.c_body.append(c)
#         #win = GraphWin("THEEE",1000,1000)
#
#         for circ in self.c_body:
#             circ.draw(window)
#         #return win
#
#     def move_circ(self,dis = 10 , count = 10, sleep = 0):
#         counter = 0
#         while True:
#             rnd = self.move_randome()
#             for circ in self.c_body :
#                 circ.move(rnd[0]*dis,rnd[1]*dis)
#                 time.sleep(sleep)
#             if count == 0:
#                 counter -= 1
#             else:
#                 counter += 1
#             if counter > count:
#                 break
#         #win.close()
#
# class Stick_man(A):
#     def __init__(self, X=0, Y=0, ID=0 , Size = 3):
#         super().__init__(X=X, Y=Y, ID=ID)
#         sticker_body = [(1.5,9),(4.5,9),(2,8),(4,8),(2.5,7),(3.5,7),(1,6),(3,6),(5,6),(1.5,5),(3,5),(4.5,5),(2,4),(3,4),(4,4),(3,3),(3,2),(2,1),(3,1),(4,1),(3,0)]
#         self.body = []
#         for x,y in sticker_body:
#             x_new = x + self.x
#             y_new = y + self.y
#             self.body.append((x_new, y_new))
#     pass



def main():
    x = A(X=25, Y=25, Size=10)
    #x.draw()
    le_body= x.body
    print(le_body)
    plt.scatter([x for x,_ in le_body], [y for _,y in le_body])
    plt.grid(True)
    #plt.axis('equal')
    plt.axis('square')
    plt.show()

    x.move_randome()

    le_body = x.body
    print(le_body)
    plt.scatter([x for x, _ in le_body], [y for _, y in le_body])
    plt.grid(True)
    # plt.axis('equal')
    plt.axis('square')
    plt.show()

def main1():

    win = GraphWin("THEEE",1000,1000)

    x = A(X=60, Y=40, Size=150)
    x1= A(X=20, Y=20, Size=40)
    x2 = A(X=20, Y=60, Size=30)
    x3 = A(X=70, Y=20, Size=20)
    x4 = A(X=75, Y=60, Size=60)
    x5 = A(X= 20, Y=40, Size=10)

    objects = [x,x1,x2,x3,x4,x5]
    #objects = [x]
    colors = ["black","red","blue","yellow","green","gray","orange"]
    #colors = ["black"]

    for object in objects:
        object.draw(window = win,colors= colors)

    while True:
        for object in objects:
            object.move_circ(count=1)

    win.close()

def main2():
    win = GraphWin("THEEE", 1000, 1000)

    objects = []
    for _ in range(500):
        x_rnd = randint(0,100)
        y_rnd = randint(0,100)
        obj = Stick_man(X=x_rnd, Y=y_rnd)
        objects.append(obj)

    colors = ["black", "red", "blue", "yellow", "green", "gray", "orange"]
    # colors = ["black"]

    for object in objects:
        object.draw(window=win, colors=colors)

    while True:
        for object in objects:
            object.move_circ(count=1)

    # a = []
    # for i, object in enumerate(objects):
    #     #a.append(Thread(target=))
    #     #a.append(Thread(target=object.move_circ))
    #     #a[i].start()
    #     pass
    #
    # for i in a:
    #     i.join()

    win.close()

#def main3()
if __name__ == "__main__":
    #main()
    #main1()
    main2()

    #x = input()



