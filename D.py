class Programmer:
    def __init__(self, surname_name, lv):
        self.time = 0
        self.lv_name = ['Junior', 'Middle', 'Senior', 'Upper']
        self.surname_name = surname_name
        self.lv = lv
        self.coin = 0
        self.coin_res = 0
        self.time_res = 0

    def work(self, time):
        self.time = time

    def rise(self):
        if self.lv != 'Upper':
            self.lv = self.lv_name[self.lv_name.index(self.lv) + 1]

    def info(self):
        if self.lv == self.lv_name[0]:
            self.coin_res += 10 * self.time
            self.time_res += self.time
        elif self.lv == self.lv_name[1]:
            self.coin_res += 15 * self.time
            self.time_res += self.time
        elif self.lv == self.lv_name[2]:
            self.coin_res += 20 * self.time
            self.time_res += self.time
        else:
            self.coin += 1
            self.coin_res += self.time * (self.coin + 20)
            self.time_res += self.time
        return f'{self.surname_name} {self.time_res}ч. {self.coin_res}тгр.'


