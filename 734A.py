n = int(input())
s = input()
A = 0
D = 0
for i in range(n):
    if s[i] == 'A':
        A += 1
    elif s[i] == 'D':
        D += 1

if A > D:
    print("Anton")
elif D > A:
    print("Danik")
else:
    print("Friendship")