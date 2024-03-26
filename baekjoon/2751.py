import sys
input = sys.stdin.readline

# '''
# 퀵 정렬의 동작방식은 다음과 같다. 
# 가령 예를 들어 배열 [5, 6, 1, 4, 2, 3, 7]이 있고, 피봇을 임의로 4를 선택했다 가정하자. 
# 이후 4를 기준으로 작은 것은 왼쪽으로 큰 것은 오른쪽으로 보내 [1, 2, 3] < 4 < [5, 6, 7]를 생성한다. 
# 다시 왼쪽에서부터 임의의 피봇 2를 설정하여 [1] < 2 < [3]을 생성하고 
# 오른쪽에선 임의의 피봇 6를 설정하여 [5] < 6 < [7]로 나눈다. 
# 만약 배열 길이가 1이 된다면 가장 정렬 완료된 것이므로 분할된 배열을 합쳐 줌으로써 정렬을 마친다.
# '''
# n = int(input())

# mylist = []

# # input O(n)
# for _ in range(n):
#     mylist.append(int(input()))

# # quicksort
# def quicksort(arr : list):
#     l, eq, r = [], [], []

#     if len(arr) <= 1:
#         return arr

#     # pivot = middle
#     piv = arr[len(arr)//2]

#     for i in arr:
#         if i < piv:
#             l.append(i)
#         elif i > piv:
#             r.append(i)
#         else:
#             eq.append(i)
            
#     return quicksort(l) + eq + quicksort(r)

# sorteds = quicksort(mylist)

# for i in sorteds:
#     print(i)


# #---------------------------------------------------------------

# '''
# 이건 무슨 정렬이죠
# tree sort. O(nlogn)이라는데
# timeout 임
# '''
# n = int(input())
# class Node:
#     def __init__(self, value) -> None:
#         self.value = value
#         self.l = None
#         self.r = None
#     def setChildValue(self, newval):
#         if newval < self.value:
#             if self.l == None:
#                 self.l = Node(newval)
#             else:
#                 self.l.setChildValue(newval)
#         else:
#             if self.r == None:
#                 self.r = Node(newval)
#             else:
#                 self.r.setChildValue(newval)
#     def printAscend(self):
#         if self.l != None:
#             self.l.printAscend()

#         print(self.value)

#         if self.r != None:
#             self.r.printAscend()

# for i in range(n):
#     if i == 0:
#         root = Node(int(input()))
#     else:
#         root.setChildValue(int(input()))

# root.printAscend()

# n = int(input())

# li = []

# for i in range(n):
#     li.append(int(input()))

# for i in sorted(li):
#     print(i)