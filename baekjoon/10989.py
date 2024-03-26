import sys
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
# 5초 8MB 
input = sys.stdin.readline

n = int(input())

mylist = []

for i in range(n):
    mylist.append(int(input()))

for i in sorted(mylist):
    print(i)

# 메모리초과
    

