n = int(input())
a = list(map(int, input().split()))
count, m = 0, 0
for i in range(n):
    if a[i] >= a[i-1]:
        count += 1
        m = max(m,count)
    else:
        count = 1
print(m)