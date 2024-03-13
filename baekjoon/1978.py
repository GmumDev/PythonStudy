import math
n = int(input())
s = input().split()

def isPrime(n:int):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

cnt = 0
for i in s:
    if isPrime(int(i)):
        cnt += 1
print(cnt)


