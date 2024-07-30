n = int(input())
x = list(map(int, input().split()))
s = d = 0

left = 0
right = n - 1

for i in range(n):
    if i % 2 == 0:
        if x[left] > x[right]:
            s += x[left]
            left += 1
        else:
            s += x[right]
            right -= 1
    else:
        if x[left] > x[right]:
            d += x[left]
            left += 1
        else:
            d += x[right]
            right -= 1

print(f"{s} {d}")
