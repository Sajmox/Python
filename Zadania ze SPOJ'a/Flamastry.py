a = input()
x = 1

while x < len(a):
    b = 1
    if a[x] == a[x-1]:
        if x > 1:
            if not a[x-1] == a[x-2]:
                while a[x] == a[x-1] and x < len(a):
                    x += 1
                    b += 1
                    if x == len(a):             #AAABB
                        break
                    print(b)
            else:
                print(a[x-1])
                while a[x] == a[x-1] and x < len(a):
                    x += 1
                    b += 1
                    if x == len(a):
                        break
                    print(b)

    else:
        if x > 1:
            if a[x-1] == a[x-2]:
                print(a[x])
                x += 1
            else:
                print(a[x-1])
                x += 1
        if x < 2:
            print(a[x-1])
