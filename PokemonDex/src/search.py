from src.fight import fight
from src.settings import Colors, text_display

# method with pokemon searching mechanics

# pokemon_in_route -> should be one of databases from WildPokemon class in wild_pokemon.py


def search(pokemon_in_route):
    exit = 0

    # searching loop
    while(exit == 0):
        text_display(f'{Colors.YELLOW}Choose Your action.{Colors.END}')
        text = f'{Colors.PURPLE}\n1. Search\n2. Leave{Colors.END}'
        text_display(text)
        choice = input(f'{Colors.LIGHT_WHITE}\nYour choice: {Colors.END}')

        match(choice):
            case '1':
                fight(pokemon_in_route)
            case '2':
                exit = 1
            case _:
                print(f'{Colors.LIGHT_RED}Wrong choice!{Colors.END}')

if __name__ == '__main__':
    search()
