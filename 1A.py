x = input()
m,n,a = map(int,x.split())
if(m%a==0):
    r1 = m/a
else:
    r1 = int(m/a) + 1
if(n%a==0):
    r2 = n/a
else:
    r2 = int(n/a) + 1
print(int(r1*r2))