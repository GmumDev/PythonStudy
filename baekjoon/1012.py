import sys
input = sys.stdin.readline

'''
T: 테스트케이스
M: 가로
N: 세로
X, Y: 배추위치

ground: 배추위치 튜플배열
'''

T = int(input())


# same as num of jirung
numOfGroup = 0

class bachu:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = Y

        # 0 for no jirung | 1 ~ for jirung
        self.group = 0 

    def getNearbys(self, arr):
        nearbys = []
        for i in arr:
            if self.x == i[0] and self.y == [1]:
                continue
            if (self.x - i[0])**2 <= 1 and (self.y - i[1])**2 <= 1:
                nearbys.append(i[0], i[1])
        return nearbys
    
    def setGroup(self, arr):
        curGroup = numOfGroup
        nearbys = self.getNearbys(arr)

        throw


for _ in range(T):
    M, N, K = input().split()
    M, N, K = int(M), int(N), int(K)

    ground = []
    jireong = 0

    for _ in range(K):
        X, Y = input().split()
        X, Y = int(X), int(Y)
        ground.append(X, Y)
    

