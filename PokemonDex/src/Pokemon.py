class Pokemon:
    # constructor with variables {pokemon name, pokemon level, pokemon catch ratio}
    def __init__(self, name, level, catch_ratio):
        self.name = name
        self.level = level
        self.catch_ratio = catch_ratio

    # works method to show pokemon's data
    def show_pokemon(self):
        print('This is ' + self.name + ', lv. ' + str(self.level) + '!')