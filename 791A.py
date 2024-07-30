x,y = map(int,input().split())
year = 0
while(1):
    year += 1
    x *= 3
    y *= 2

    if x > y :
        print(year)
        break