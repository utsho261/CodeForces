n = int(input())
A, B, C = [], [], []
num = list(map(int, input().split()))

for i in range(n):
    if num[i] == 1:
        A.append(i + 1)
    elif num[i] == 2:
        B.append(i + 1)
    elif num[i] == 3:
        C.append(i + 1)

ans = min(len(A), len(B), len(C))
print(ans)
for i in range(ans):
    print(A[i], B[i], C[i])
