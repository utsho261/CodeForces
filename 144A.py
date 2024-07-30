n = int(input())
a = list(map(int, input().split()))
max = 0
min = 101
maxi = 0
mini = 0

for i in range(n):
    if a[i] > max:
        max = a[i]
        maxi = i
    if a[i] <= min:
        min = a[i]
        mini = i
if maxi>mini:
    result = maxi + (n - 1 - mini) - 1
else:
    result = maxi + (n - 1 - mini)
print(result)
