# 숫자 출력 기본
print(52)
print(52.123)
print()

# 변수의 자료형 출력 type()
print(type(123))
print(type(123.123))
print()

# 숫자 연산자
print("5 + 7 = ",5+7)
print("5 - 7 = ",5-7)
print("5 * 7 = ", 5*7)
print("5 / 7 = ",5/7) # 소수점까지 계산
print("5 // 7 = ",5//7) # 정수까지만 계산
print("5 % 7 = ",5%7) # 나머지 연산자
print("5 ** 7 = ",5**7) # 제곱 연산자 5^7
print() # 여기서 , 대신 + 를 쓰면 어떻게 될까 ? -> 숫자를 계산하는 연산자와 헷갈리기에 , 연산자 사용. ex) ("5 + 7"+ 5+7) 중간에 쓰인 +가 더하는건지 문자열처리인지 모른다.

# 변수 할당
pi = 3.141592
r = 10

print("pi : ",pi)
print("r : ",r)
print("2 * pi * r : ",2*pi*r)
print("pi * r * : ",pi*r*r)
print()

# 복합대입연산자
numList = [10 for i in range(6)]

numList[0] += 10
numList[1] -= 10
numList[2] *= 2
numList[3] /= 2
numList[4] %= 3
numList[5] **= 2
    #print("number2 : ",number2 += 100) # 이와 같이 대입연산자가, 바로 오는 경우 유효하지 않음

for element in numList:
    print(element)

print()

# 문자열 복합 대입 연산지
string = "hello"
print(string)

string += "! "
print(string)

string *= 3
print(string)
print()

# 사용자 입력 input()-1

string = input("type string data >> ")
print(string)
print(type(string))
print()

# 사용자 입력 input()-2

num = int(input("type num data >> "))
print(num)
print(type(num))
print()

# 사용자 입력 input()-3

numList = [None for i in range(2)]
numList[0] = int(input("type num1 data >> "))
numList[1] = int(input("type num2 data >> "))
print(numList[0], type(numList[0]), type(numList[1]), numList[1])

print(numList[0]+numList[1])
print(numList[0]-numList[1])
print(numList[0]*numList[1])
print(numList[0]/numList[1])
print(numList[0]//numList[1])
print(numList[0]%numList[1])
print(numList[0]**numList[1])
print()

# 문자열 to 숫자

string = "12345"
numString = int(string)
print(string, type(string))
print(numString, type(numString))
print()

outputA = int("52")
outputB = float("52.52")
print(outputA, type(outputA))
print(outputB, type(outputB))

# 숫자 to 문자열

num = 12345
stringNum = str(num)
print(num, type(num))
print(stringNum, type(stringNum))
print()

# 인치-센치 변환

raw_input = input("type inch data >> ")
inch = int(raw_input)

print("inch : ",inch)

cm = 2.54 * int(raw_input)
print("cm ",cm)
print()