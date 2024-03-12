
n = int(input())
arr = []
for i in range(n):
    arr.append(input())
s = set(arr)
arr = list(s)

arr.sort(key=lambda x : (len(x), x))

for i in arr:
    print(i)