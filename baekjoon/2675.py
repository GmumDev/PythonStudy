a = int(input())

for i in range(a):
    s = input()
    arr = s.split()
    for c in arr[1]:
        print(c*int(arr[0]), end='')
    print()

