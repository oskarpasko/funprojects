from . import search
from . import routes
from .minimap import minimap
from .settings import text_display, Colors
import time

class Pokemon:
    # constructor with variables {pokemon name, pokemon level, pokemon catch ratio}
    def __init__(self, name, level, catch_ratio):
        self.name = name
        self.level = level
        self.catch_ratio = catch_ratio

    # works method to show pokemon's data
    def show_pokemon(self):
        text_display(f'{Colors.LIGHT_GREEN}This is {self.name}, lv.{str(self.level)}!{Colors.END}')


class Route:
    def __init__(self, name, connections, pokemons):
        self.name = name
        self.connections = connections
        self.pokemons = pokemons

    def welcome(self):
        print('\n---------------------------------------------')
        text = f'{Colors.YELLOW}Welcome on Route ' + self.name + f'{Colors.END}'

        text_display(text)

        time.sleep(0.5)

    def show_description(self):
        print(f'{Colors.YELLOW}\nIn this route You can catch this pokemons: {Colors.END}')
        for pokemon in self.pokemons:
            text_display(f'{Colors.BLUE}{pokemon.name}, lv.{str(pokemon.level)}{Colors.END}\n')

    def go_to(self):
        text_display(f'{Colors.YELLOW}Which route You would like to choose?{Colors.END}')
        i = 1
        for conn in self.connections:
            text_display(f'\n{Colors.PURPLE}{str(i)}. Route {str(conn)}{Colors.END}')
            i+=1
        i = 1
        choice = input(f'{Colors.LIGHT_WHITE}\nYour choice: {Colors.END}')
        for conn in self.connections:
            if(choice == str(i)):
                routes.routes(conn)
            i+=1

    def action(self):
        while(True):
            text_display('\nWhich action You would like to chose?\n')
            time.sleep(0.5)
            text = f"""{Colors.PURPLE}1. Show description
2. Show minimap
3. Search Pokemon
4. Go To...
5. Quit game{Colors.END}\n"""

            text_display(text)

            choice = input(f'{Colors.LIGHT_WHITE}Your choice: {Colors.END}')
            match(choice):
                case '1':
                    self.show_description()
                case '2':
                    minimap.minimap()
                case '3':
                    search.search(self.pokemons)
                case '4':
                    self.go_to()
                case '5':
                    exit()
                case _:
                    print(f'{Colors.LIGHT_RED}Wrong choice!{Colors.END}')




# list of pokemons

# class with 'databases' with pokemon in each route / city

class WildPokemon:
    pokemons_route_201 = [
        Pokemon('Torchic', 5, 4),
        Pokemon('Mudkip', 5, 4),
        Pokemon('Treeko', 5, 4)
    ]

    pokemons_route_202 = [
        Pokemon("Poochyena", 2, 3),
        Pokemon('Zigzagoon', 3, 2),
        Pokemon("Wurmple", 2, 0),
        Pokemon("Wurmple", 3, 1),
        Pokemon('Wurmple', 4, 2)
    ]

    pokemons_route_203 = [
        Pokemon('Wurmple', 2, 0),
        Pokemon('Poochyena', 4, 2),
        Pokemon('Wingull', 6, 3),
        Pokemon('Marill', 7, 5),
        Pokemon('Marill', 4, 3)
    ]

    pokemons_route_204 = [
        Pokemon('Marill', 7, 5),
        Pokemon('Sableye', 10, 5),
        Pokemon('Makuhita', 11, 6),
        Pokemon('Absol', 11, 4)
    ]

    pokemons_route_205 = [
        Pokemon('Absol', 13, 5),
        Pokemon('Tropius', 16, 7),
        Pokemon('Spheal', 18, 6),
        Pokemon('Swablu', 19, 3)
    ]

    pokemons_route_206 = [
        Pokemon('Absol', 13, 5),
        Pokemon('Tropius', 16, 7),
        Pokemon('Spheal', 18, 6),
        Pokemon('Swablu', 19, 3),
        Pokemon('Manetric', 20, 6)
    ]

    pokemons_route_207 = [
        Pokemon('Beldum', 22, 7),
        Pokemon('Bagon', 22, 7)
    ]

    pokemons_route_208 = [
        Pokemon('Reyquaza', 70, 9),
        Pokemon('Kyogre', 45, 9),
        Pokemon('Groudon', 45, 9)
    ]