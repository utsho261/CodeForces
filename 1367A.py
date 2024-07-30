n = int(input())
for _ in range(n):
    s = input()
    a = s[0]
    for i in range(1, len(s), 2):
        a += s[i]
    print(a)