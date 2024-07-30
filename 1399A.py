for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    if n == 1:
        print("YES")
    else:
        for i in range(n-1):
            if abs(a[i+1] - a[i]) > 1:
                print("NO")
                break
        else:
            print("YES")
