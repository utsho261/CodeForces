a, b = map(int, input().split())
x = 1
while 1:
    if (x * a)%10 == b or (x * a)%10 == 0:
        break
    x += 1
print(x)