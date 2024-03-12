arr = [0 for i in range(10)]
result = 1
for i in range(3):
    result *= int(input())
result = str(result)
for i in range(10):
    arr[i] = result.count(str(i))
    print(arr[i])