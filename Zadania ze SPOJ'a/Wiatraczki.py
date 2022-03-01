gwiazdka = "*"
kropka = "."

n = int(input("Podaj wartosc n: "))
z = n
lista = []
if n == 0:
    raise ValueError("Wartosc nie moze byc rowna 0")
if n < 0:
    n = n * (-1)

bok = n * 2
i = n
j = n
if z > 0:
    for k in range(n):

        zmienna1 = kropka * (i - 4)
        zmienna2 = gwiazdka * j
        zmienna3 = kropka * (j - 1)
        zmienna4 = gwiazdka * (i - 3)

        rzad = zmienna1 + zmienna2 + zmienna3 + zmienna4
        lista.append(rzad)
        i += 1
        j -= 1
        print(lista[k])

    while n != 0:
        print(lista[n-1][::-1])
        n -= 1
else:
    for k in range(n):

        zmienna1 = kropka * (i - 4)
        zmienna2 = gwiazdka * j
        zmienna3 = kropka * (j - 1)
        zmienna4 = gwiazdka * (i - 3)

        rzad = zmienna1 + zmienna2 + zmienna3 + zmienna4
        lista.append(rzad)
        i += 1
        j -= 1
        print(lista[k][::-1])

    while n != 0:
        print(lista[n-1])
        n -= 1