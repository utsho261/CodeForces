n = int(input())
count=0
for _ in range(n):
    y = input()
    if "++" in y:
        count = count + 1
    elif "--" in y:
        count = count - 1

print(count)
