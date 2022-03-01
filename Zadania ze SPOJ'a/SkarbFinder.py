wertykalnie = 0
horyzontalnie = 0

print("Podaj liczbe wskazowek:\n")

n = int(input())

for i in range (n):
    print("Podaj wspolrzedne wskazowki nr ", i + 1, ":")
    kierunek, kroki = input().split()
    kierunek = int(kierunek)
    kroki = int(kroki)

    if kierunek == 0:
        wertykalnie += kroki
    if kierunek == 1:
        wertykalnie -= kroki
    if kierunek == 2:
        horyzontalnie -= kroki
    if kierunek == 3:
        horyzontalnie += kroki

print(wertykalnie)
print(horyzontalnie)

if wertykalnie == 0 and horyzontalnie == 0:
    print("Skarb znajduje sie w studni.")

if wertykalnie > 0:
    print("Nalezy wykonac ", wertykalnie, " krokow na polnoc")

if wertykalnie < 0:
    print("Nalezy wykonac ", wertykalnie * (-1), " krokow na poludnie")

if horyzontalnie > 0:
    print("Nalezy wykonac ", horyzontalnie, " krokow na wschod")

if horyzontalnie < 0:
    print("Nalezy wykonac ", horyzontalnie * (-1), " krokow na zachod")