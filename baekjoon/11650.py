import sys
input = sys.stdin.readline

'''
문제
2차원 평면 위의 점 N개가 주어진다. 
좌표를 x좌표가 증가하는 순으로, 
x좌표가 같으면 y좌표가 증가하는 순서로 
정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. 
(-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 
위치가 같은 두 점은 없다.

'''

n = int(input())
xy = []

for i in range(n):
    xy.append(input().split())
    xy[i][0] = int(xy[i][0])
    xy[i][1] = int(xy[i][1])


xy.sort(key=lambda item: (item[0], item[1]))

for i in xy:
    print(i[0], i[1])