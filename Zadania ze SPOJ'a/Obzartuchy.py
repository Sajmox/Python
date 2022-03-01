suma = 0
n = int(input("Podaj liczbe testow:\n"))
for i in range (n):
    ile_obz = int(input("Podaj ile bedzie obzartuchow:\n"))
    ile_ciastek = int(input("Podaj ile jest ciastek w opakowaniu:\n"))
    for j in range (ile_obz):
        print("Podaj w ile sekund", j+1, "obzartuch zjada ciastko:\n")
        czas = int(input())
        ile_zje = 86400 // czas
        suma = suma + ile_zje
    ile_pudelek = suma / ile_ciastek
    if suma % ile_ciastek == 0:
        print(ile_pudelek)
    else:
        ile_pudelek = int(ile_pudelek)
        print(ile_pudelek+1)

        # 702, 2, 8 ... 712