n, x = map(int, input().split())
s = input().split()
for i in range(n):
    if int(s[i]) < x:
        print(s[i], end=' ')