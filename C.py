class RedButton:
    def __init__(self):
        self.i = 0

    def click(self):
        print('Тревога!')
        self.i += 1

    def count(self):
        return self.i