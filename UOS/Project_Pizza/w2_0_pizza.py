price = 3500
pizza = input("피자 이름을 입력하세요 : ")
many = input("수량을 입력하세요: 여러조각을 선택 가능합니다: ")
many = int(many)

print("=========================")
print("주문내역:", pizza, many, "개")

print("=========================")
print("합계:", price * many)

