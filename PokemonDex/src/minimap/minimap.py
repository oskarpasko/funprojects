from ..settings import Colors

def minimap():
    print(f'{Colors.LIGHT_CYAN}\n       |')
    print('      208')
    print('       |')
    print('--207--+--206--+ ')
    print('       |       | ')
    print('      203     205')
    print('       |       |')
    print('--202--+--204--+')
    print('       |')
    print('      201')
    print(f'       |{Colors.END}')

    if __name__ == '__main__':
        minimap()