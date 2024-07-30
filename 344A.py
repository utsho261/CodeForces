n = int(input())
x = int(input())
count = 1
for i in range(n-1):
    y = int(input())
    if y == x:
        pass
    else:
        count += 1
        x = y
print(count)