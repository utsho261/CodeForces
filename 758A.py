n = int(input())
x = list(map(int, input().split()))
count = 0
m = max(x)
for i in range(n):
    count += m - x[i]
print(count)