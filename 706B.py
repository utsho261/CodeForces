from bisect import bisect_right

n = int(input())
x = sorted(map(int, input().split()))
q = int(input())

for _ in range(q):
    m = int(input())
    count = bisect_right(x, m)
    print(count)
