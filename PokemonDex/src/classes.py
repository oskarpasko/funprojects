class Pokemon:
    # constructor with variables {pokemon name, pokemon level, pokemon catch ratio}
    def __init__(self, name, level, catch_ratio):
        self.name = name
        self.level = level
        self.catch_ratio = catch_ratio

    # works method to show pokemon's data
    def show_pokemon(self):
        print('This is ' + self.name + ', lv. ' + str(self.level) + '!')


class Route:
    def __init__(self, name, connections, description):
        self.name = name
        self.connections = connections
        self.desctription = description

    def show_description(self):
        print(self.desctription)

    def action(self):
        print('Which action You would like to chose?')

    def go_to(self):
        pass