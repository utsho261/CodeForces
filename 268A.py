n = int(input())
a = []

for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)

c = 0
for i in range(n):
    for j in range(n):
     if a[i][0] == a[j][1]:
            c += 1


print(c)
