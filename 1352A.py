t = int(input())
for _ in range(t):
    n = int(input())
    a = []

    if n % 10 != 0:
        a.append(n % 10)
        n -= n % 10
    if n % 100 != 0:
        a.append(n % 100)
        n -= n % 100
    if n % 1000 != 0:
        a.append(n % 1000)
        n -= n % 1000
    if n % 10000 != 0:
        a.append(n % 10000)
    if n>=10000 and n%10000 == 0:
        a.append(n)

    print(len(a))
    for i in a:
        print(i, end=' ')
    print()
