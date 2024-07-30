s = input()
s1 = 'hello'
x = 0
for i in range(len(s)):
    if x < len(s1) and s[i] == s1[x]:
        x += 1

if x == len(s1):
    print("YES")
else:
    print("NO")