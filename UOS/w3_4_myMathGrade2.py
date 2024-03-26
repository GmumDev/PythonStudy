score = float(input("수학ㄷ 점수를 입력하세요."))
if score >= 60:
    if score >= 70:
        if score >= 80:
            if score >= 90:
                grade = 'A'
            else:
                grade = 'B'
        else:
            grade = 'C'
    else:
        grade = 'D'
else:
    grade = 'F'

print("당신의 수학점수는", grade, "이고, 성적은", score, "입니다.")

