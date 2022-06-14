from . import search

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
    def __init__(self, name, connections, description, pokemons):
        self.name = name
        self.connections = connections
        self.desctription = description
        self.pokemons = pokemons

    def show_description(self):
        print(self.desctription)

    def action(self):
        print('Which action You would like to chose?')
        print('1. Search Pokemon')
        choice = input('...')
        match(choice):
            case '1':
                search.search(self.pokemons)
                pass
            case _:
                print('Wrong choice!')

    def go_to(self):
        pass



# list of pokemons

# class with 'databases' with pokemon in each route / city

class WildPokemon:
    pokemons_test_route = [
        Pokemon('Torchic', 5, 5),
        Pokemon('Mudkip', 5, 5),
        Pokemon('Treeko', 5, 5),
        Pokemon("Poochyena", 2, 3),
        Pokemon("Wurmple", 2, 0),
        Pokemon("Wurmple", 3, 1),
        Pokemon('Wurmple', 4, 2)
    ]