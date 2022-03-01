a = int(input("Podaj ilosc zetonow 1 gracza:\n"))
b = int(input("Podaj ilosc zetonow 2 gracza:\n"))

if a >= b:
    A = a
    B = b
else:
    A = b
    B = a

while A != 0 or B != 0:
    if A == B:
        break
    A = A - B
    if A >= B:
        break
    if A == B:
        break
    B = B - A
    if B >= A:
        break

print(A+B)