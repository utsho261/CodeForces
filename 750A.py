n, k = map(int, input().split())
x = 0
count = 0
for i in range(1,n+1):
    x += i*5
    if 240 >= k+x:
        count += 1
    else:
        break
print(count)