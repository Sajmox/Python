n = int(input("Podaj ile liczb chcesz policzyc:\n"))
i = 1
while i <= n:
    print("Podaj", i, " liczbe:\n")
    a = input()
    a = str(a)
    b = a[::-1]
    x = 1
    while a != b:
        x += 1
        a = int(a)
        b = int(b)
        a = a + b
        a = str(a)
        b = a[::-1]
    print(a," ",x)
