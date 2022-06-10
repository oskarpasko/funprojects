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
for x in range(0, 10):
    random.choice(pokemons).show_pokemon()
