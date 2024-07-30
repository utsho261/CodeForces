n, a, b, c = map(int, input().split())
arr = [-4000] * (n + 1)
arr[0] = 0

for i in range(1, n + 1):
    x, y, z = -4000, -4000, -4000
    if i >= a:
        x = arr[i-a]
    if i >= b:
        y = arr[i-b]
    if i >= c:
        z = arr[i-c]
    arr[i] = 1 + max(x, y, z)

print(arr[n])