
tscore = float(input())

if tscore > 900:
    print("당신의 토익 점수는", tscore, "상위권 점수입니다.")
elif tscore > 700:
    print("당신의 토익 점수는", tscore, "중위권 점수입니다.")
else: 
    print("당신의 토익 점수는", tscore, "하위권 점수입니다.")

print("if 문 종료됨")