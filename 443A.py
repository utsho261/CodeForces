a = input()
s = ''
for i in range(len(a)):
    if 'a' <= a[i] <= 'z':
        s += a[i]
x = list(set(s))
print(x)
s1 = ''.join(x)
print(len(s1))
