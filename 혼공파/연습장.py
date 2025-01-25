# 함수의 기본

def print_str1(n, value):
    for i in range(n):
        print(value,end="")

def print_str2(n, *value):
    for i in range(n):
        for element in value:
            print(element,end=" ")

def print_str3(a=10,b=20,c=30):
    print("a + ","b + ","c :",a+b+c)


print_str1(3,"hello world !")
print()
print_str2(3, "hello","world","!!")
print()
print_str3(a=1,b=1,c=1)
print_str3(c=2,b=2,a=1)


# 메모이제이션 피보나치

dicta = {
    1 : 1,
    2 : 1
}

def fibo(n):
    if n in dicta:
        return dicta[n]
    else:
        output = fibo(n-1) + fibo(n-2)
        dicta[n] = output
        return output

print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))
print(fibo(6))

# 리스트 평탄화 재귀함수

def flatten(lista):
    result = []
    for element in lista:
        if isinstance(element,list):
            result += flatten(element)
        else:
            result.append(element)
    return result


lista = [[1,[[2],3]],[4,[5,6]],7,[8,9]]
print(lista)
print(flatten(lista))


# 매개변수로 받은 함수 호출

def fun_value(func):
    for i in range(10):
        func()

def print_hello():
    print("hello world !")

fun_value(print_hello)