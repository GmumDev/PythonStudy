score = float(input())


if score > 90:
    grade = 'A'
elif score > 80:
    grade = 'B'
elif score > 70:
    grade = 'C'
elif score > 60:
    grade = 'D'
else:
    grade = 'F'

print("당신의 수학점수는", grade, "이고, 성적은", score, "입니다.")

