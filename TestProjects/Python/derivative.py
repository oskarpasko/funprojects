# ========== Liczenie pochodnych ========== #
#from sympy import *

#x = Symbol('x')
#f = (x+1)*(x-1)**4
#f_prime = f.diff(x)
#f_prime_prime = f_prime.diff(x)

#print(f)
#print(f_prime)
#print(f_prime_prime)
#print(f.evalf(subs={x:3}))
#print(f_prime.evalf(subs={x:3}))
# ========== Koniec Pochodnych ========== #

from sympy import *

a, o, t = symbols('a o t') # symbole
f = a*sin(o*t) # wzor funkcji
predkosc = f.diff(t) # 1. pochodna
przyspieszenie = predkosc.diff(t) # 2. pochodna

print(predkosc)
print(przyspieszenie)

result_predkosc = predkosc.evalf(subs={a:0.2, o:(2*pi), t:1 })
result_przyspieszenie = przyspieszenie.evalf(subs={a:0.2, o:(2*pi), t:1 })

print(round(result_predkosc, 2))
print(round(result_przyspieszenie, 2))

