money = 255
rate = 4.1
duration = 12

'''
만기수 총 금액을 계산하여 화면에 출력
심화 - 정기예금 금액과 이자율의 데이터 값은 표준입력 함수를 사용하여 프로그램을 작성하세요
'''
print("정기예금 금액: ", money, "만원")
print("이자율(연이율): ", rate, "%")
print("기간: ", duration, "개월")
print("만기후 총 금액: ", money + money * rate * 0.01, "만원")