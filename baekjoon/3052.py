arr = [0 for i in range(10)]
rem = [0 for i in range(10)]
cnt = []
for i in range(10):
    arr[i] = int(input())
    rem[i] = arr[i]%42
    if cnt.count(rem[i]) == 0:
        cnt.append(rem[i])

print(len(cnt))