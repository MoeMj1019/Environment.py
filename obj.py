class obj:
    def __init__(self, X=0, Y=0, ID=0):
        self.x = X
        self.y = Y
        self.id = ID

    def xUP(self, var):
        self.x += var
    def xDown(self, var):
        self.x -= var

    def yUP(self, var):
        self.y += var
    def yDown(self, var):
        self.y -= var

    def getX(self):
        return self.x
    def getY(self):
        return self.Y
