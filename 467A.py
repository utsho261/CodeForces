n = int(input())
count = 0
for _ in range(n):
    x,y = map(int,input().split())
    if y - x >= 2:
        count += 1

print(count)