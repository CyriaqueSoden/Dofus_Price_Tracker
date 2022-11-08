from screeninfo import get_monitors
multiX = get_monitors()[0].width
multiY = get_monitors()[0].height


class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.defX = self.x
        self.defY = self.y

    def next(self):
        if multiX == 2560 and multiY == 1440:
            self.y += 66
        else:
            self.y += 55

    def getCoordinates(self):
        return (self.x, self.y)

    def getRegOcrNumber(self):
        return (self.x + 10, self.y + 10)

    def reset(self):
        self.x = self.defX
        self.y = self.defY
