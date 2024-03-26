'''
# na = 20 인풋으로
# nb = 5 인풋으로
# 더하기의 결과값 result1
# 빼기 결과값 result2
# 곱하기 결과값 result3
# 나누기 결과값 result4
'''
na = int(input("정수 입력 na: "))
nb = int(input("정수 입력 nb: "))
result1 = na + nb
result2 = na - nb
result3 = na * nb
result4 = na / nb

print(na, "(na)", "+", nb, "(nb)", "=", result1)
print(na, "(na)", "-", nb, "(nb)", "=", result2)
print(na, "(na)", "×", nb, "(nb)", "=", result3)
print(na, "(na)", "÷", nb, "(nb)", "=", result4)