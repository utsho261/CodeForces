n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    r = a % b
    if r == 0:
        print(0)
    else:
        print(b - r)
