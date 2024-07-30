x = input()
LowerL = 0
UpperL = 0
for i in range(len(x)):
    if x[i] == x[i].lower():
        LowerL += 1
    else:
        UpperL += 1

if LowerL > UpperL:
    x = x.lower()
    print(x)
elif LowerL < UpperL:
    x = x.upper()
    print(x)
else:
    x = x.lower()
    print(x)