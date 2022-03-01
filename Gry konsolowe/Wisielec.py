import os
clear = lambda: os.system("cls")

print("Siema, zagramy w wisielca\n")
print("Podaj nick:\n")
nick = input()

literki = []
zycia = 6
lista1 = []
haslo = "sekret"

for i in range(len(haslo)):                                     # tworzenie listy
    lista1.append("_")


while zycia > 0:                                                # gramy dopoki zycia sie nie skoncza

    clear()
    print("Pozostalo ",zycia," zyc,\n")
    print("Sprobuj zgadnac literke:\n")
    print(" ".join(lista1))
    print(" ")
    print("Użyte literki:")
    print(" ".join(literki))
    litera = input()                                            # pobranie litery od uzytkownika
    literki.append(litera)

    if litera in haslo:                                         # sprawdzanie czy litera jest w hasle
        for i in range(len(haslo)):
            if litera == haslo[i]:
                lista1[i] = litera                              # jesli tak to zamienia element listy
    else:
        zycia -= 1                                              # w przeciwnym wypadku tracisz zycie
    if not "_" in lista1:
        clear()
        print(" ". join(lista1))
        print("Gratulacje ",nick,", haslo to: ",haslo)
        a = input()
        break
if zycia == 0:
    print(" ")
    print("Skonczyły Ci się życia, spróbuj jeszcze raz")
    a = input()