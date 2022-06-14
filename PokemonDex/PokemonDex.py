from src.search import search
from src.wild_pokemon import WildPokemon
from src.classes import Route

conn = ['202', '203', '204']
des = 'You are on route 201 in this area are not any Pokemons'
route201 = Route('201', conn, des)

route201.show_description()
route201.action()

search(WildPokemon.pokemons_test_route)
