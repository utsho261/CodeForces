x,y = map(int,input().split())
a = 0
b = 0
z = list(map(int,input().split()))
for i in range(x):
    if y >= z[i] :
        a += 1
    else:
        b += 2

print(a+b)

