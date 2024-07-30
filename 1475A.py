for _ in range(int(input())):
    n = int(input())
    print("YES" if n % 2 != 0 or (n & (n - 1)) != 0 else "NO")
