n = int(input())
x = list(map(int,input().split()))
count = 0
for i in range(n):
   if x[i] == 1:
       count = 1


if count == 1:
    print("HARD")
else:
    print("EASY")