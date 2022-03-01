from math import sqrt,pi
R = float(input("Podaj promien sfery:\n"))
O = float(input("Podaj odleglosc miedzy srodkami sfer:\n"))
r = float(((R)**2))-((O/2)**2)
print(r)
S = float(pi * r)
print(S)