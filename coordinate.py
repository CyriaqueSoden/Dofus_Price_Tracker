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

        if multiX == 2560 and multiY == 1440:
            return (self.x - 170, self.y)
        else:
            return (self.x - 122, self.y)

    def reset(self):
        self.x = self.defX
        self.y = self.defY
