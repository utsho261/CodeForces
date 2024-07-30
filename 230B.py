n = int(input())
x = list(map(int, input().split()))
count = 0
for i in range(n):
    for j in range(1,x[i]+1):
        if x[i]%j == 0:
            count += 1
    if count == 3:
        print("YES")
    else:
        print("NO")
    count = 0