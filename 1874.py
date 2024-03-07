n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
result = []

stack = []
nextN = 1
# first number
for i in range(a[0]):
    result.append('+')
    stack.append(nextN)
    nextN += 1
result.append('-')
stack.pop()

# second ~ 
idx = 0
while idx < n - 1:
    if a[idx] < a[idx + 1]:
        while nextN <= a[idx + 1]:
            result.append('+')
            result.append('-')
            #stack.append(nextN)
            nextN += 1
    elif stack[len(stack) - 1] == a[idx + 1]:
        result.append('-')
        stack.pop()
    else:
        result = ['NO']
        break
    print(result, stack)
    idx += 1

for i in result:
    print(i)
