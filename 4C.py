n = int(input())
x = {}

for i in range(n):
    s = input()
    if s not in x:
        x[s] = 0
        print("OK")
    else:
        x[s] += 1
        print(f"{s}{x[s]}")
