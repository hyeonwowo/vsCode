# 리턴

# 자료 없이 리턴하기

def return_test():
    return print("aa")

return_test()
print()

# 자료와 함께 리턴하기

def return_test():
    return 100

value = return_test()
print(value)
print(return_test())
print()


# 아무것도 리턴하지 않았을 때의 리턴값

def return_test():
    return

value = return_test()
print(value)
print()


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