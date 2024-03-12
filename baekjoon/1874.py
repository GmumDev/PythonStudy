n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
actions = []
stack = []
nextN = 1
NO = False
for i in range(len(a)):
    if nextN <= a[i]:
        while nextN <= a[i]:
            actions.append('+')
            stack.append(nextN)
            nextN+=1
        stack.pop()
        actions.append('-')
    elif stack[len(stack) - 1] == a[i]:
        actions.append('-')
        stack.pop()
    else:
        NO = True
if NO:
    print('NO')
else:
    for i in actions:
        print(i)

