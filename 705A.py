n = int(input())

a = []

for i in range(n):
    if i % 2 == 0:
        a.append("I hate")
    else:
        a.append("I love")
    if i < n - 1:
        a.append("that")

a.append("it")
print(" ".join(a))
