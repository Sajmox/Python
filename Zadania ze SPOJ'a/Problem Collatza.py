pierwszy_wyraz = int(input("Podaj pierwszy wyraz ciagu:"))
wynik = 0
i = 0
while pierwszy_wyraz != 1:
    if pierwszy_wyraz % 2 == 0:
        pierwszy_wyraz = pierwszy_wyraz / 2
    else:
        pierwszy_wyraz = (3 * pierwszy_wyraz) + 1

    i += 1

print(i)