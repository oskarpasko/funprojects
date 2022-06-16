from src.classes import WildPokemon
from src.classes import Route

def routes(name):
    match(name):
        case '201':
            _route_201() 
        case '202':
            _route_202()
        case '203':
            _route_203()
        case '204':
            _route_204()
        case '205':
            _route_205()
        case '206':
            _route_206()
        case '207':
            _route_207()
        case '208':
            _route_208()
        case _:
            'Error 249!'

def _route_201():
    conn = ['202', '203', '204']
    pokemons = WildPokemon.pokemons_route_201
    route201 = Route('201', conn, pokemons)

    route201.welcome()
    route201.action()

def _route_202():
    conn = ['201', '203', '204']
    pokemons = WildPokemon.pokemons_route_202
    route202 = Route('202', conn, pokemons)

    route202.welcome()
    route202.action()

def _route_203():
    conn = ['201', '202', '204', '206', '207', '208']
    pokemons = WildPokemon.pokemons_route_202
    route202 = Route('203', conn, pokemons)

    route202.welcome()
    route202.action()

def _route_204():
    conn = ['201', '202', '203', '205']
    pokemons = WildPokemon.pokemons_route_202
    route202 = Route('204', conn, pokemons)

    route202.welcome()
    route202.action()

def _route_205():
    conn = ['204', '206']
    pokemons = WildPokemon.pokemons_route_202
    route202 = Route('205', conn, pokemons)

    route202.welcome()
    route202.action()

def _route_206():
    conn = ['203', '206', '207', '208']
    pokemons = WildPokemon.pokemons_route_202
    route202 = Route('206', conn, pokemons)

    route202.welcome()
    route202.action()

def _route_207():
    conn = ['203', '206', '208']
    pokemons = WildPokemon.pokemons_route_202
    route202 = Route('207', conn, pokemons)

    route202.welcome()
    route202.action()

def _route_208():
    conn = ['203', '206', '207']
    pokemons = WildPokemon.pokemons_route_202
    route202 = Route('208', conn, pokemons)

    route202.welcome()
    route202.action()
    