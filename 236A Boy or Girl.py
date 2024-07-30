x = input()
result = ''
for i in range(len(x)):
    if x[i] not in result:
        result += x[i]

if len(result)%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
