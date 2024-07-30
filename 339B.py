n, m = map(int, input().split())
a = list(map(int, input().split()))
count = a[0] - 1
for i in range(m-1):
    if a[i] > a[i+1]:
        count += n - (a[i] - a[i+1])
    else:
        count +=a[i+1] - a[i]
print(count)