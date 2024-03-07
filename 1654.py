k, n = map(int, input().split())
lines = []
sum = 0
for i in range(k):
    lines.append(int(input()))
    sum += lines[i]
maxLen = sum // n
cnt = 0

while(cnt < n):
    cnt = 0
    for i in range(k):
        cnt += lines[i] // maxLen
    maxLen -= 1
        

print(maxLen+1)