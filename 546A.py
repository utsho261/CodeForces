x,y,z = map(int,input().split())

count = 0
for i in range(1,z+1):
    count = count + (x*i)

if count > y:
    print(count-y)
else:
    print(0)