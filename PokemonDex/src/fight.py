import random, time
from .settings import Colors, text_display
# wild_pokeon -> should be one of databases from WildPokemon class in wild_pokemon.py


def fight(wild_pokemons):
    # Start Battle!!!!!

    # randomize pokemon
    text_display(f"{Colors.GREEN}You've found wild Pokemon! \n{Colors.END}")
    appeard_pokemon = random.choice(wild_pokemons)
    pokemon_catch_ratio = appeard_pokemon.catch_ratio
    checker = False

    # print pokemon datas
    appeard_pokemon.show_pokemon()

    # main method of fight
    while(checker == False):
        print(f'{Colors.YELLOW}\nChoose Your action!{Colors.END}')
        text = f'{Colors.PURPLE}1. Catch\n2 Run!{Colors.END}'
        text_display(text)

        choice = input(f'{Colors.LIGHT_WHITE}\nYour choice: {Colors.END}')  # user's input

        match(choice):
            case '1':
                # catch mechanics
                if(random.randint(0, 10) > pokemon_catch_ratio):
                    time.sleep(0.5)
                    text_display(f'{Colors.LIGHT_BLUE}1...{Colors.END}')
                    if(random.randint(0, 10) > pokemon_catch_ratio):
                        time.sleep(0.5)
                        text_display(f'{Colors.LIGHT_BLUE}2...{Colors.END}')
                        if(random.randint(0, 10) > pokemon_catch_ratio):
                            time.sleep(0.5)
                            text_display(f'{Colors.LIGHT_BLUE}3...{Colors.END}')
                            if(random.randint(0, 10) > pokemon_catch_ratio):
                                time.sleep(0.5)
                                text_display(f"{Colors.LIGHT_GREEN}\nYou've just caught new pokemon!{Colors.END}\n")
                                checker = True
                            else:
                                time.sleep(0.5)
                                text_display(f"{Colors.BLUE}That was 3!{Colors.END}")
                        else:
                            time.sleep(0.5)
                            text_display(f"{Colors.BLUE}Try again!{Colors.END}")
                    else:
                        time.sleep(0.5)
                        text_display(f"{Colors.BLUE}Ugh, try again!{Colors.END}")
                else:
                    time.sleep(0.5)
                    text_display(f"{Colors.BLUE}Ohhh, try again!{Colors.END}")
            case '2':
                text_display(f"{Colors.LIGHT_BLUE}You've run away!{Colors.END}\n")
                checker = True
            case _:
                print(f"{Colors.LIGHT_RED}Wrong choice!{Colors.END}")

if __name__ == '__main__':
    fight()