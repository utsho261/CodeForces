x = input()
x = x.lower()
v = 'aoyeui'
x1 = ''

for i in range(len(x)):
    if x[i] not in v:
        x1 += x[i]

for i in range(len(x1)):
    print(f".{x1[i]}", end="")
