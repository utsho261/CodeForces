n = int(input())
x = list(map(int, input().split()))

s = sum(x)
x.sort(reverse=True)

s1 = 0
count = 0

for i in x:
    s1 += i
    count += 1
    if s1 > s - s1:
        break

print(count)
