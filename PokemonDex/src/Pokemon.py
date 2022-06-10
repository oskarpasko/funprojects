class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def show_pokemon(self):
        print('This is ' + self.name + ', lv. ' + self.level + '!')