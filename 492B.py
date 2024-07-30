n, l = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

max_diff = 2 * max(a[0], l - a[-1])
for i in range(1, n):
    if (a[i] - a[i-1]) > max_diff:
        max_diff = max(max_diff, a[i] - a[i-1])

print((max_diff / 2))