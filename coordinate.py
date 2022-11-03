from screeninfo import get_monitors
multiX = 2560 / get_monitors()[0].width
multiY = 1440 / get_monitors()[0].height


class Coordinate:

    def __init__(self, x, y):
        self.x = round(x / multiX)
        self.y = round(y / multiY)
        self.coordinates = (self.x, self.y)
