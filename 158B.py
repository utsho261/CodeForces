a1 = a2 = a3 = a4 = 0
n = int(input())
x = list(map(int,input().split()))

for i in range(n):
    if x[i] == 1:
        a1 += 1
    elif x[i] == 2:
        a2 += 1
    elif x[i] == 3:
        a3 += 1
    elif x[i] == 4:
        a4 += 1

sum = a4

if a3 >= a1:
    sum += a3
    a1 = 0
else:
    sum += a3
    a1 -= a3

if a2:
    if a2 % 2 == 0:
        sum += a2 // 2
        a2 = 0
    else:
        sum += (a2 - 1) // 2
        a2 = a2 % 2

if a2:
    if a1 <= 2:
        sum += 1
        a1 = 0
    else:
        sum += 1
        a1 -= 2

if a1:
    if a1 % 4 != 0:
        sum += a1 // 4 + 1
    else:
        sum += a1 // 4

print(sum)
