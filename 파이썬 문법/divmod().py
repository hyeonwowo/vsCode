# divmod() : 몫과 나머지를 한번에 반환

quotient, remainder = divmod(10,3)
print("몫 : ",quotient)
print("나머지 : ",remainder)


# 예제1) 초를 분과 초로 나누기
seconds = 130
minutes, remaining_seconds = divmod(seconds, 60)
print(f"{minutes}분 {remaining_seconds}초")  # 2분 10초


# 예제2) 돈을 동전 단위로 분리
money = 1260
coin500, money = divmod(money, 500)
coin100, money = divmod(money, 100)
coin50, money = divmod(money, 50)
coin10, money = divmod(money, 10)

print(coin500, coin100, coin50, coin10)  # 2 2 1 1
