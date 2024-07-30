for _ in range(int(input())):
    x = int(input())
    if 1900 <= x:
        y = 1

    if 1600 <= x <= 1899:
        y = 2

    if 1400 <= x <= 1599:
        y = 3

    if 1399 >= x:
        y = 4
    print(f"Division {y}")

