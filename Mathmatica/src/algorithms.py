from settings import Colors
from math import sqrt

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

def newton_symbol(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def quadratic_function():
    a = int(input(f"{Colors.CYAN}Podaj a: {Colors.END}"))
    b = int(input(f"{Colors.CYAN}Podaj b: {Colors.END}"))
    c = int(input(f"{Colors.CYAN}Podaj c: {Colors.END}"))

    print(f"{Colors.LIGHT_GREEN}f(x)={a}x^2+{b}x+{c}{Colors.END}")

    delta = (b^2) - (4*a*c)

    if(delta > 0):
        x1 = round( -1*b-sqrt(delta)/2*a, 3)
        x2 = round(-1*b+sqrt(delta)/2*a, 3)

        print(f"{Colors.LIGHT_GREEN}x1 = {x1}{Colors.END}")
        print(f"{Colors.LIGHT_GREEN}x2 = {x2}{Colors.END}")
        print(f"{Colors.CYAN}Postać iloczynowa:{Colors.END}")
        print(f"{Colors.LIGHT_GREEN}f(x) = {a}(x - {x1})(x - {x2}){Colors.END}")

    elif(delta == 0):
        x1 = -1 * b / 2 * a
        print(f"{Colors.LIGHT_GREEN}x1 = x2 = {x1}{Colors.END}")
    else:
        print(f"{Colors.LIGHT_GREEN}Równanie kwadratowe nie ma rozwiązania.{Colors.END}")


    p = -1 * (b/2*a)
    q = -1 * (delta/4*a)

    print(f"{Colors.CYAN}Postać kanoniczna: {Colors.LIGHT_GREEN}\nf(x) = (a - p)^2 + q \nf(x) = ({a} - {p})^2 + {q}{Colors.END}")
