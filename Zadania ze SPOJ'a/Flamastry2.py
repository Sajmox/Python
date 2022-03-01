a = input()
x = 1
print(a[x-1])
while x < len(a):
    b = 1
    if a[x] == a[x-1]:
        if x < len(a):
            while a[x] == a[x-1]:
                b += 1
                x += 1
                if x == len(a):
                    break
            print(b)

    else:
        print(a[x])
        x += 1
