n = int(input())

if 12 <= n <= 1000000:
    if n % 2 == 0:
        print(4, n - 4)
    else:
        print(9, n - 9)
