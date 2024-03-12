n = int(input())
a = input().split()
a = set(a)

m = int(input())
b = input().split()

### O(n^2) -> timeout
#   list.count() > 0 ... O(n)
#   set.__contains__() ... O(1)
#
#
for i in range(m):
    print('1' if a.__contains__(b[i]) else '0')



    