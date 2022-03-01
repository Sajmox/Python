t = int(input("Podaj ile chcesz wykonac testow:\n"))
i = 1
while i <= t:
    j = 0
    n = int(input("Podaj ile liczb chcesz dodac:\n"))
    a = (input("Podaj liczby oddzielajac je spacja:\n"))
    a = a.split(' ')
    if len(a) == n:
        while j < n:
            a[j] = int(a[j])
            j += 1
        print(sum(a))
        i += 1
    else:
        print("Podaj wlasciwa ilosc liczb")