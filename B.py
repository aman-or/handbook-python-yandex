class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x1, y1):
        self.x += x1
        self.y += y1

    def length(self, point):
        return round(((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** (1 / 2), 2)