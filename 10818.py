n = int(input())
min = 1000000
max = -1000000
arr = input().split()
for i in range(n):
    if int(arr[i]) < min:
        min = int(arr[i])
    if int(arr[i]) > max:
        max = int(arr[i])
print(min, max)