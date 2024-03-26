print("------------------------------")
print("-----------[메뉴판]-----------")
print("------------------------------")
print("--1--페퍼로니피자------￦3000--")
print("--2--치즈피자----------￦3400--")
print("--3--고구마피자--------￦3600--")
print("--4--포테이토피자------￦3200--")
print("--5--파인애플피자------￦3500--")
print("------------------------------")
pizza = input("피자 이름을 입력해주세요 :")

pizza1='페퍼로니피자'
pizza2='치즈피자'
pizza3='고구마피자'
pizza4='포테이토피자'
pizza5='파인애플피자'

price1=3000
price2=3400
price3=3600
price4=3200
price5=3500

if pizza == pizza1:
    price = price1
elif pizza == pizza2:
    price = price2
elif pizza == pizza3:
    price = price3
elif pizza == pizza4:
    price = price4
elif pizza == pizza5:
    price = price5
else:
    print("잘못된 피자 이름입니다. 프로그램을 종료합니다.")

pizza_cnt = int(input("주문할 " + pizza + " 개수를 입력하세요:"))

print("주문한", pizza, pizza_cnt, "개의 가격은 ￦", pizza_cnt*price, "입니다.")