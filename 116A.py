n = int(input())
count = 0
m = 0
for i in range(n):
    x,y = map(int,input().split())
    if i == 0:
        x = 0
    if i-1 == n:
        y = 0
    count -= x
    count += y
    m = max(m,count)

print(m)