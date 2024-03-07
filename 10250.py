t = int(input())
for _i in range(t):
    h, w, n = map(int, input().split())
    xx = 1 + (n-1)//h
    yy = n%h
    if yy == 0:
        yy = h
    print(f'{yy}%02d' % xx)