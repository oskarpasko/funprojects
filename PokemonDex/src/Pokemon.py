class Pokemon:
    def __init__(self, name, level, catch_ratio):
        self.name = name
        self.level = level
        self.catch_ratio = catch_ratio

    def show_pokemon(self):
        print('This is ' + self.name + ', lv. ' + str(self.level) + '!')