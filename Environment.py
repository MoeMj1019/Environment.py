from graphics import *
from time import *
from random import *

class Environment:
    def __init__(self, window = None, option = 0,pixel_objects = None , visual_objects = None):
        self.option = option

        if window:
            self.window = window
        else:
            self.window = GraphWin("sample",500,500)

        if pixel_objects:
            self.pixel_objects = pixel_objects
        else:
            self.pixel_objects = []

        if visual_objects:
            self.visual_objects = visual_objects
        else:
            self.visual_objects = []
        for obj in self.pixel_objects:
            rnd_color = choice(obj.colors)
            for x, y in obj.body:
                c = Circle(Point(x * 10, y * 10), 5)
                c.setFill(rnd_color)
                self.visual_objects.append(c)

        for obj in self.visual_objects:
            obj.draw(self.window)

        self.draw_map(self.option)

    def close(self):
        self.window.close()

    def draw_map(self,var):
        width = self.window.getWidth()
        hight = self.window.getHeight()

        if var == 0:
            frame = []
            for x, y in zip(range(int(width / 10)), range(int(hight))):
                rect = Rectangle(Point(x * 10, y * 10), Point(x * 10 + 10, y * 10 + 10))
                frame.append(rect)
            for r in frame:
                r.draw(self.window)

        if var == 1:
            frame=[]
            # y1 = hight- hight/3
            # y2 = hight- 2 * hight / 3
            y1 = int(hight*0.3)
            y2 = y1 + 20
            for x in range(int(width*0.1),int(width*0.9),10):
                rect1 = Rectangle(Point(x,y1),Point(x + 10 , y1 + 10))
                rect2 = Rectangle(Point(x, y2), Point(x + 10, y2 + 10))
                rect1.setFill("brown")
                rect2.setFill("brown")
                frame.append(rect1)
                frame.append(rect2)
            for obj in frame:
                obj.draw(self.window)


# def test():
#     a = Environment()
#     # circ = Circle(Point(50,50),30)
#     # circ.draw(a.window)
#     a.window.getMouse()
#     a.window.close()
# #print(help(GraphWin))