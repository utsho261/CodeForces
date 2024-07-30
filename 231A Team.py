count=0
n = int(input())
for _ in range(n):
    x = input()
    a,b,c=map(int,x.split())
    if (a==0 or a==1) and (b==0 or b==1) and (c==0 or c==1):
        if (a+b+c) >= 2:
            count = count + 1
print(count)
