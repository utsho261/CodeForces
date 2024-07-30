n = int(input())

if n % 2 == 0:
    count = n // 2
else:
    count = -(n + 1) // 2

print(count)
