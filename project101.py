import matplotlib.pyplot as plt
from Stick_man import *
from Tier_1 import *
from Environment import Environment
from time import *

def test_0(*args,**kwargs):
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

def test_1(*args,**kwargs):

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
    win.getMouse()
    win.close()

def test_2(*args,**kwargs):
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

def test_3(*args,**kwargs):
    win = GraphWin("THEEE", 1000, 1000)

    objects = []
    for _ in range(500):
        x_rnd = randint(0, 100)
        y_rnd = randint(0, 100)
        obj = Stick_man(X=x_rnd, Y=y_rnd)
        objects.append(obj)

    colors = ["black", "red", "blue", "yellow", "green", "gray", "orange"]
    # colors = ["black"]

    for object in objects:
        object.draw(window=win, colors=colors)

    # a = []
    # for i, object in enumerate(objects):
    #     #a.append(Thread(target=))
    #     #a.append(Thread(target=object.move_circ))
    #     #a[i].start()
    #     pass
    #
    # for i in a:
    #     i.join()

def test_4(*args,**kwargs):
    colors = ["black", "red", "blue", "yellow", "green", "gray", "orange"]
    objects = []
    for _ in range(2):
        x_rnd = randint(5, 45)
        y_rnd = randint(5, 45)
        stickMan = Stick_man(X=x_rnd, Y=y_rnd,colors=colors)
        tier_1_obj = Tier_1(X=y_rnd, Y=x_rnd, Size=x_rnd+y_rnd/2,colors=colors)
        objects.append(stickMan)
        objects.append(tier_1_obj)

    x = Tier_1(X=10,Y=20,Size=30)
    objects.append(x)

    win = GraphWin("stickman",500,500)

    a = Environment(pixel_objects=objects,window=win,option=1)
    a.window.getMouse()
    a.close()
if __name__ == "__main__":
    #test_0()
    #test_1()
    #test_2()
    #test_3()
    test_4()
