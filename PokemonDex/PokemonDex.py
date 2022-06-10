from src.Pokemon import Pokemon
import random

# list of pokemons
pokemons = [Pokemon('Torchic', 5),
            Pokemon('Mudkip', 5),
            Pokemon('Treeko', 5),
            Pokemon("Poochyena", 2),
            Pokemon("Wurmple", 2),
            Pokemon("Wurmple", 3),
            Pokemon('Wurmple', 4)]

# Writes all pokemons from list
# for pokemon in pokemons:
#    pokemon.show_pokemon()


# Write specific pokemon with index
# pokemons[1].show_pokemon()

# random pokemon :O
#for x in range(0, 10):
#    random.choice(pokemons).show_pokemon()




# Catch pokemon tests
print("\nYou've found wild Pokemon! \n")
random.choice(pokemons).show_pokemon()
checker = False


# main method of fight?
while(checker == False):
    print('\nChoose Your action!')
    print('1. Catch!')
    print('2. Run!\n')

    choice = input('...')

    match(choice):
        case '1':
            if(random.randint(0, 10) > 5):
                print('1...')
                if(random.randint(0, 10) > 5):
                    print('2...')
                    if(random.randint(0, 10) > 5):
                        print('3...')
                        if(random.randint(0, 10) > 5):
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

