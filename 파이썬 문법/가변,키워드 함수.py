# 가변 매개변수 함수

def func(n, *values):
    for i in range(n): # 반복 횟수
        for value in values: # 출력문
            print(value) # print(value,end="") 사용으로 줄바꿈 없이 print 출력 가능.
        print()

func(5,"hello","world","!")


# 키워드 매개변수 함수
# 함수 응용 - 주어진 변수의 합 더하기(1)

def sum(start,end):
    value = 0
    for i in range(start,end+1):
        value += i
    return value

print("0 - 100 : ",sum(0,100))
print("0 - 50 : ",sum(0,50))
print("0 - 10 : ",sum(0,10))
print("100 - 100 : ",sum(100,100))
print()

# 함수 응용 - 주어진 변수의 합 더하기(2)

def sum(start=0, end=100, step=1):
    value = 0
    for i in range(start,end,step):
        value += i
    return value

print("sum A : ",sum(0,100,10))
print("sum B : ",sum(end = 100))
print("sum C : ",sum(end=100,step=2))
print()