szesnastkowa = []
def zmiana_na_16(x):
    wynik = " "
    wynik_dzielenia = 1
    while wynik_dzielenia != 0:
        wynik_dzielenia = x // 16
        reszta = x % 16
        if reszta == 10:
            reszta = "A"
        if reszta == 11:
            reszta = "B"
        if reszta == 12:
            reszta = "C"
        if reszta == 13:
            reszta = "D"
        if reszta == 14:
            reszta = "E"
        if reszta == 15:
            reszta = "F"
        x = wynik_dzielenia
        szesnastkowa.append(reszta)
    szesnastkowa.reverse()
    for j in range (len(szesnastkowa)):
        szesnastkowa[j] = str(szesnastkowa[j])
    for k in range (len(szesnastkowa)):
        wynik = wynik + szesnastkowa[k]

    print(wynik)

t = int(input("Podaj liczbe testow:\n"))
for i in range(t):
    print("Podaj ", i + 1, " liczbe:\n")
    liczba = int(input())
    print("Ta liczba w systemie 16 wynosi:\n")
    zmiana_na_16(liczba)
