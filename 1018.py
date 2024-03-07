n, m = map(int, input().split())
board = ['' for row in range(n)]
ideal = [
    ['BWBWBWBW',
     'WBWBWBWB',
     'BWBWBWBW',
     'WBWBWBWB',
     'BWBWBWBW',
     'WBWBWBWB',
     'BWBWBWBW',
     'WBWBWBWB',],
    ['WBWBWBWB',
     'BWBWBWBW',
     'WBWBWBWB',
     'BWBWBWBW',
     'WBWBWBWB',
     'BWBWBWBW',
     'WBWBWBWB',
     'BWBWBWBW',]

]
for row in range(n):
    board[row] = input()

min = 2500
for k in range(2):
    for nn in range(n-8+1):
        for mm in range(m-8+1):
            cnt = 0
            for j in range(8):
                for i in range(8):
                    if board[nn + j][mm + i] != ideal[k][j][i]:
                        cnt += 1
            if min > cnt:
                min = cnt
print(min)