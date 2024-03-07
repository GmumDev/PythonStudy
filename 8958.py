n = int(input())
for _i in range(n):
    s = input()
    sum = 0
    point = 0
    for i in s:
        if i == 'O':
            point += 1
        elif i == 'X':
            point = 0
        sum += point

    print(sum)