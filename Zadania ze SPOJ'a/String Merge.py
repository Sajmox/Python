ciag3 = []

t = int(input("Wprowadz liczbe testow:\n"))

for i in range (t):
    ciag1, ciag2 = input("Wprowadz ciagi znakow, oddzielajac je spacja:\n").split()

if len(ciag1) > len(ciag2):
    for j in range (len(ciag2)):
        ciag3.append(ciag1[j])
        ciag3.append(ciag2[j])
    print(ciag3)
else:
    for j in range (len(ciag1)):
        ciag3.append(ciag1[j])
        ciag3.append(ciag2[j])
    print(ciag3)
