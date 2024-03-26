
'''
f   | r     | n     | n1
-----------
1   | 1     | 1     | 1
2   | 6     | 2~7   | 2
3   | 12    | 8~19  | 8
4   | 16    | 20~37 | 20
5   | 24    | 38~61 | 38

f   | r     | 1 + (f-1)*6

an1 = 3f**2-9f+8 where f >= 2
'''

# 1 ~ 1,000,000,000
n = int(input())

# circle steps
f = 1

while(True):

    # n1 = start num of the circle f
    if f >= 2:
        n1 = 3*f**2 - 9*f + 8
    elif f == 1:
        n1 = 1

    # if n was in pasted circle
    if n < n1:
        print(f-1)
        break

    # go next circle
    f += 1
