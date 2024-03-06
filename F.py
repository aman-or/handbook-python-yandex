class Rectangle:
    def __init__(self, a, b):
        self.left_down = [min(a[0], b[0]), min(a[1], b[1])]
        self.up_right = [max(a[0], b[0]), max(a[1], b[1])]

    def perimeter(self):
        return round((self.up_right[0] - self.left_down[0]) * 2 +
                     (self.up_right[1] - self.left_down[1]) * 2, 2)

    def area(self):
        return round((self.up_right[0] - self.left_down[0]) *
                     (self.up_right[1] - self.left_down[1]), 2)

    def get_pos(self):
        return round(self.left_down[0], 2), round(self.up_right[1], 2)

    def get_size(self):
        return round(self.up_right[0] - self.left_down[0], 2), round(self.up_right[1] - self.left_down[1], 2)

    def move(self, dx, dy):
        self.left_down[0] += dx
        self.left_down[1] += dy
        self.up_right[0] += dx
        self.up_right[1] += dy

    def resize(self, width, height):
        self.up_right[0] = self.left_down[0] + width
        self.left_down[1] = self.up_right[1] - height


if __name__ == '__main__':
    rect = Rectangle((7.52, -4.3), (3.2, 3.14))
    print(rect.get_pos(), rect.get_size())
    rect.resize(23.5, 11.3)
    print(rect.get_pos(), rect.get_size())
