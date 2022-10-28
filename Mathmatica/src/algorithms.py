from .settings import Colors

def exponentation():
    base = int(input(f'{Colors.CYAN}Enter base: {Colors.END}')) 
    exponent = int(input(f'{Colors.CYAN}Enter exponent: {Colors.END}'))
    result = 1

    if(exponent >= 0):
        for x in range (0, exponent):
            result *= base
        print(f"{Colors.LIGHT_GREEN}{base}^{exponent} = {result}{Colors.END}")
    else:
        exponent *= -1
        for x in range (0, exponent):
            result *= base
        print(f"{Colors.LIGHT_GREEN}{base}^({-1*exponent}) = {1/result}{Colors.END}")

def factorial(a):
    if(a<2):
        return 1
    return a * factorial(a-1)
