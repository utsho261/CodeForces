n = int(input())
p = 0
c = 0
a = list(map(int, input().split()))

for i in range(n):
    if a[i] == -1:
        if p > 0:
            p -= 1
        else:
            c += 1
    else:
        p += a[i]
print(c)