for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    value = 0
    for a in x:
        if x.count(a) == 1:
            value = a
            break
    for i in range(n):
        if x[i] == value:
            print(i+1)
            break
