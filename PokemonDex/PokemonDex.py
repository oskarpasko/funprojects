from src.Pokemon import Pokemon
import random

pokemons = [Pokemon('Torchic', 5), Pokemon('Mudkip', 5), Pokemon('Treeko', 5)]

# Writes all pokemons from list
#for pokemon in pokemons:
#    pokemon.show_pokemon()


# Write specific pokemon with index
# pokemons[1].show_pokemon()

# random pokemon :O
random.choice(pokemons).show_pokemon()