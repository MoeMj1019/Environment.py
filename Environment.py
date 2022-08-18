from graphics import *
from time import *

class Environment:
    def __init__(self, window = GraphWin("sample",500,500), option = 0):
        self.window = window
        self.option = option


a = Environment()
circ = Circle(Point(50,50),30)
circ.draw(a.window)
a.window.getMouse()
a.window.close()


print(help(GraphWin))