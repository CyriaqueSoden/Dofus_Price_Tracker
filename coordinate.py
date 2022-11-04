

class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.defX = self.x
        self.defY = self.y

    def next(self):
        self.y += 55

    def getCoordinates(self):
        return (self.x, self.y)

    def reset(self):
        self.x = self.defX
        self.y = self.defY

    def __repr__(self):
        return (self.x, self.y)
