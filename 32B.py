s = input()
i = 0
while i < len(s):
    if s[i] == '.':
        print(0, end='')
        i += 1
    else:
        print(1 if s[i+1] == '.' else 2, end='')
        i += 2
