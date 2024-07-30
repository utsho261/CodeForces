for _ in range(int(input())):
    a, b = sorted(map(int, input().split()))

    if a == b:
        print(0)
    else:
        if (b-a)%10 == 0:
            print((b-a)//10)
        else:
            print(((b-a)//10)+1)