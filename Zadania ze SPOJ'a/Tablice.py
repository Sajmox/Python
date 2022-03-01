t = int(input("Wprowadz liczbe testow:\n"))
tablica = []
for i in range (t):
    print("Ile liczb chcesz podac w ", i + 1, " tescie:")
    n = int(input())
    for j in range (n):
        print("Podaj ", j + 1, " liczbe:\n")
        x = int(input())
        tablica.insert(j,x)
        j += 1
    tablica.reverse()
    print(tablica)
