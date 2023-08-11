a, b, c = int(input()), int(input()), int(input()) #сколько чисел из 3-х совпадают
if a == b:
    if b == c:
        print(3)
    else:
        print(2)
else:
    if a == c:
        print(2)
    else:
        if b == c:
            print(2)
        else:
            print(0)