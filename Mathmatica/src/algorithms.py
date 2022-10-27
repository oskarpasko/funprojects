from .settings import Colors, print_colored

def exponentation():
    base = int(input('Enter base: ')) 
    exponent = int(input('Enter exponent: '))
    result = 1

    if(exponent >= 0):
        for x in range (0, exponent):
            result *= base
        print(f"{base}^{exponent} = {result}")
    else:
        exponent *= -1
        for x in range (0, exponent):
            result *= base
        print(f"{base}^{-1*exponent} = {1/result}")
