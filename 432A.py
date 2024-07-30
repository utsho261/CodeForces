n, k = map(int, input().split())
s = list(map(int, input().split()))

count = 0
s.sort()

for i in range(n):
    if s[i] + k <= 5:
        count += 1

print(count // 3)
