x, y = map(int, input().split())

for _ in range(y):
    if str(x)[-1] == '0':
        x = x // 10

    else:
        x = x - 1
print(x)