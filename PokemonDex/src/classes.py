from . import search
from . import routes

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
    def __init__(self, name, connections, pokemons):
        self.name = name
        self.connections = connections
        self.pokemons = pokemons

    def welcome(self):
        print('')
        print('---------------------------------------------')
        print("Welcome on route " + self.name)

    def show_description(self):
        print('\nIn this route You can catch this pokemons: ')
        for pokemon in self.pokemons:
            print(pokemon.name + ', lv.' + str(pokemon.level))

    def go_to(self):
        i = 1
        print('\n')
        for conn in self.connections:
            print(str(i) + '. Route ' + str(conn))
            i+=1
        i = 1
        choice = input('\nWhere do You want to go? ...')
        for conn in self.connections:
            if(choice == str(i)):
                routes.routes(conn)
            i+=1

    def action(self):
        while(True):
            print('\nWhich action You would like to chose?')
            print('1. Show description')
            print('2. Search Pokemon')
            print('3. Go To...')
            print('4. Quit game')
            choice = input('...')
            match(choice):
                case '1':
                    self.show_description()
                case '2':
                    search.search(self.pokemons)
                case '3':
                    self.go_to()
                case '4':
                    exit()
                case _:
                    print('Wrong choice!')




# list of pokemons

# class with 'databases' with pokemon in each route / city

class WildPokemon:
    pokemons_route_201 = [
        Pokemon('Torchic', 5, 5),
        Pokemon('Mudkip', 5, 5),
        Pokemon('Treeko', 5, 5),
        Pokemon("Poochyena", 2, 3),
        Pokemon("Wurmple", 2, 0),
        Pokemon("Wurmple", 3, 1),
        Pokemon('Wurmple', 4, 2)
    ]

    pokemons_route_202 = [
        Pokemon('Wurmple', 2, 0),
        Pokemon('Poochyena', 4, 2)
    ]