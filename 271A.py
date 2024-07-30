y = int(input())
while(1):
    y += 1
    x = str(y)
    if x[0] != x[1] and x[0] != x[2] and x[0] != x[3] and x[1] != x[2] and x[1] != x[3] and x[2] != x[3] :
        print(x)
        break