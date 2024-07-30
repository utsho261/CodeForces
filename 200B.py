n = int(input())
x = list(map(int,input().split()))
count = 0
for i in range(n):
    count += x[i]

print(count/n)