class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = tuple()
        self.d = tuple()

    def perimeter(self):
        x = self.b[0] - self.a[0]
        y = self.b[1] - self.a[1]
        self.c = (self.a[0] + x, self.a[1])
        self.d = (self.b[0], self.b[1] + y)
        length_ab = abs(self.b[0] - self.a[0])
        length_bc = abs(self.c[1] - self.b[1])
        return round(2 * (length_ab + length_bc), 2)

    def area(self):
        x = self.b[0] - self.a[0]
        y = self.b[1] - self.a[1]
        self.c = (self.a[0] + x, self.a[1])
        self.d = (self.b[0], self.b[1] + y)
        length_ab = abs(self.b[0] - self.a[0])
        length_bc = abs(self.c[1] - self.b[1])
        return round(length_ab * length_bc, 2)


if __name__ == '__main__':

    rect = Rectangle((7.52, -4.3), (3.2, 3.14))
    print(rect.area())
