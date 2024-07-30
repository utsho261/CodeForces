x = input()
y = input()

z = ['0' if x[i] == y[i] else '1' for i in range(len(x))]
print(''.join(z))
