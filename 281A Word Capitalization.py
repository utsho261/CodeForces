x = input()
if x[0] == x[0].upper():
    print(x)
else:
    x = x[0].upper() + x[1:]
    print(x)