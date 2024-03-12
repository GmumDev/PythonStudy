arr = input().split()
result = ''
for i in range(0, len(arr) - 1):
    if int(arr[i]) < int(arr[i+1]):
        if result == 'descending':
            result = 'mixed'
            break
        result = 'ascending'
    elif int(arr[i]) > int(arr[i+1]):
        if result == 'ascending':
            result = 'mixed'
            break
        result = 'descending'
print(result)