while(True):
    a = input()
    lth = len(a)
    idx = 0
    result = 'yes'
    if a == '0':
        break
    while lth > idx*2:
        if a[idx] != a[lth - idx - 1]:
            result = 'no'
            break
        idx += 1
    print(result)

