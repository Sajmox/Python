while True:
    n = int(input("Podaj ilosc elementow zbioru n:\n"))
    k = int(input("Podaj ilosc elementow podzbioru k:\n"))
    if n < k:
        print("n musi byc wieksze od k\n")
        continue
    if n == k:
        print(1)
        break
    def silnia(x):

        wynik1 = x
        while x != 2:
            wynik1 = wynik1 * (x-1)
            x -= 1
        return wynik1

    wynik2 = silnia(n) / (silnia(k) * (silnia(n-k)))

    if wynik2 < 10**9:
        print(wynik2)
        break
    else:
        print("Podaj mniejsze wartosci")