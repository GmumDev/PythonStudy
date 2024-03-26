n = int(input())

# n = 3x + 5y, x + y = k가 최소. y = k - x. 
# n = 3x + 5k - 5x = -2x + 5k. 
# x, y >= 0 정수. k >= 1 자연수
# 3 ≤ n ≤ 5000 자연수

x, y = 0, n//5

while (n - 5*y) % 3 != 0 and y > 0:
    y -= 1

x = (n - 5*y)//3

if n - 5*y - 3*x != 0:
    print(-1)
else:
    print(x + y)