def exponentation():
    base = int(input('Enter base: '))
    exponent = int(input('Enter exponent: '))
    result = 1

    for x in range (0, exponent):
        result *= base

    print(result)