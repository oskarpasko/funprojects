from src.classes import WildPokemon
from src.classes import Route

conn = ['202', '203', '204']
des = 'You are on route 201 in this area are not any Pokemons'
pokemons = WildPokemon.pokemons_test_route
route201 = Route('201', conn, des, pokemons)

route201.show_description()
route201.action()
