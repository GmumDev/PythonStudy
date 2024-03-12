import math
m, n = map(int, input().split())
prime = []

for i in range(m, n+1):
    if i == 1: continue
    flag = True
    for k in range(2, int(math.sqrt(i))+1):
        if i % k == 0:
            flag = False
            break
    if flag:
        prime.append(i)
for i in prime:
    print(i)