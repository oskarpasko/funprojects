import random
from src.wild_pokemon import WildPokemon

# wild_pokeon -> should be one of databases from WildPokemon class in wild_pokemon.py


def fight(wild_pokemons):
    # Start Battle!!!!!

    # randomize pokemon
    print("\nYou've found wild Pokemon! \n")
    appeard_pokemon = random.choice(wild_pokemons)
    pokemon_catch_ratio = appeard_pokemon.catch_ratio
    checker = False

    # print pokemon datas
    appeard_pokemon.show_pokemon()

    # main method of fight
    while(checker == False):
        print('\nChoose Your action!')
        print('1. Catch!')
        print('2. Run!\n')

        choice = input('...')  # user's input

        match(choice):
            case '1':

                # catch mechanics
                if(random.randint(0, 10) > pokemon_catch_ratio):
                    print('1...')
                    if(random.randint(0, 10) > pokemon_catch_ratio):
                        print('2...')
                        if(random.randint(0, 10) > pokemon_catch_ratio):
                            print('3...')
                            if(random.randint(0, 10) > pokemon_catch_ratio):
                                print("You've just caught new pokemon!")
                                checker = True
                            else:
                                print("That was 3!")
                        else:
                            print("Try again!")
                    else:
                        print("Ugh, try again!")
                else:
                    print("Ohhh, try again!")
            case '2':
                print("You've run away!")
                checker = True
            case _:
                print("Wrong choice!")
