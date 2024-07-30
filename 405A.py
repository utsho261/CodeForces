n = int(input())
x = list(map(int,input().split()))
x.sort()
for i in range(n):
    print(x[i],end=' ')
    