from src.fight import fight

# method with pokemon searching mechanics

# pokemon_in_route -> should be one of databases from WildPokemon class in wild_pokemon.py
def search(pokemon_in_route):
    exit = 0

    # searching loop
    while(exit == 0):
        print('1.Search')
        print('2.Leave')
        choice = input('...')

        match(choice):
            case '1':
                fight(pokemon_in_route)
            case '2':
                exit = 1
            case _:
                print('Wrong choice!')