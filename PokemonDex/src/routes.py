from src.classes import WildPokemon
from src.classes import Route

def routes(name):
    match(name):
        case '201':
            _route_201() 
        case '202':
            _route_202()
        case _:
            'Error 249!'

def _route_201():
    conn = ['202']
    pokemons = WildPokemon.pokemons_route_201
    route201 = Route('201', conn, pokemons)

    route201.welcome()
    route201.action()

def _route_202():
    conn = ['201']
    pokemons = WildPokemon.pokemons_route_202
    route202 = Route('202', conn, pokemons)

    route202.welcome()
    route202.action()
    