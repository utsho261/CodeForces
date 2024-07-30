a = input()
b = input()
c = input()
d = list(a + b)

if len(c) == len(d):
    for i in c:
        if i in d:
            d.remove(i)
        else:
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")
