n = int(input())
x = set(map(int, input().split()[1:]))
y = set(map(int, input().split()[1:]))
z = x.union(y)
if len(z) == n:
    print( "I become the guy.")
else:
    print("Oh, my keyboard!")