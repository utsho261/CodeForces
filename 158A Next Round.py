x, y = map(int, input().split())
l = list(map(int, input().split()))
count = 0
for i in range(0,x):
    if l[y-1] == 0 and l[i] == l[y-1]:
        count += 0
    elif l[y-1] <= l[i]:
        count += 1
    else:
        count += 0

print(count)
