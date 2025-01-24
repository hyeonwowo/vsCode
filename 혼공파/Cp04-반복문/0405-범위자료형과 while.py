# 범위 - 특정한 횟수만큼 반복해서 돌리고 싶을 때, for 반복문과 범위를 조합하여 사용

print(list(range(0,5)))
print(list(range(0,10,2)))

    # range()의 매개변수로는 반드시 "정수"
#print(list(range(0,10/5))) # 에러발생




# for 반복문과 범위

for i in range(5):
    print("반복변수 : ",str(i))
print()

for i in range(5,10):
    print("반복변수 : ",str(i))
print()

for i in range(0,10,3):
    print("반복변수 : ",str(i))
print()



# 리스트와 range() 조합

array = [1,2,3,4,5]

for i in range(len(array)):
    print(f"{i+1} repeat : {array[i]}")
print()



# for 반복문 : 반대로 반복

for i in range(4, 0-1, -1): # 4부터 0까지
    print(f"현재 반복 변수: {i}")



# 중첩 반복문 피라미드 (1)

for i in range(5):
    print("*" * i)
print()


# 중첩 반목문 피라미드 (2)

for i in range(5):
    print(" "*(4-i)+"*"*(i+1)) # "+" 대신 "," 사용시 공백 하나가 더 추가돼서 원하지 않는 결과가 발생함.


# 중첩 반복문 피라미드 (3)

for i in range(5):
    print(" "*(4-i)+"*"*(2*i+1))
