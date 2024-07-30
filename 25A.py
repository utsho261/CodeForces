n = int(input())
x = list(map(int, input().split()))
even = 0
odd = 0
for i in range(n):
    if x[i]%2 == 0:
        even += 1
        even_index = i + 1
    else:
        odd += 1
        odd_index = i + 1

if even == 1:
    print(even_index)
else:
    print(odd_index)