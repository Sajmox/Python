from math import sqrt
t = int(input("Podaj liczbe testow:\n"))
nazwa = []
x = []
y = []
wspolrzedne = []
odleglosc = []
wspolrzedne_nowa = []
nazwa_nowa = []

for i in range (t):
    n = int(input("Ile punktow chcesz podac?\n"))

    for j in range (n):
        nazwa1, x1, y1 = input("Podaj nazwe punktu oraz wspolrzedne punktu, oddzielajac dane spacją:\n").split()
        nazwa.append(nazwa1)
        x1 = int(x1)
        y1 = int(y1)
        x.insert(x1,j)
        y.insert(y1,j)
        x1 = str(x1)
        y1 = str(y1)
        wspolrzedne1 = x1 + " , " + y1
        wspolrzedne.append(wspolrzedne1)
        odleglosc.append(sqrt(x[j]**2 + y[j]**2))

    for j in range (n):
        index = odleglosc.index(max(odleglosc))
        del odleglosc[index]
        wspolrzedne_nowa.append(wspolrzedne[index])
        del wspolrzedne[index]
        nazwa_nowa.append(nazwa[index])
        del nazwa[index]


    for j in range (n):
        print(nazwa_nowa[j], wspolrzedne_nowa[j])
