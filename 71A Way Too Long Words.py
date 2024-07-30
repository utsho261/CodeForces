n = int(input())

for _ in range(n):
    w = input()
    if len(w) > 10:
        result = w[0] + str(len(w) - 2) + w[-1]
        print(result)

    else:
        print(w)
