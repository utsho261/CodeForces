n = int(input())
a = list(map(int, input().split()))
count = 0
minimum = maximum = a[0]

for i in range(1, n):
    if a[i] < minimum: # 50<100, 1
        minimum = a[i] # 50
        count += 1
    elif a[i] > maximum: #200>100,2
        maximum = a[i] # 200
        count += 1

print(count)
