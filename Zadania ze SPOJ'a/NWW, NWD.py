a = int(input("Podaj pierwsza liczbe:\n"))
b = int(input("Podaj druga liczbe:\n"))

def nwd(a,b):
    while a != b:
        if a > b:
            a = a - b
        if b > a:
            b = b - a
    return a

def nww(a,b):
    return a * b / nwd(a,b)

print(nwd(a,b))
print(nww(a,b))