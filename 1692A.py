for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print((b > a) + (c > a) + (d > a))