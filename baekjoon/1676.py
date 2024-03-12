def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input())
k = factorial(n)
k = str(k)
cnt = 0
for i in range(len(k)):
    if k[len(k) - i - 1] == '0':
        cnt += 1
    else:
        break
print(cnt)