# 반복문 팩토리얼

def factorial(n):
    value = 1
    for i in range(1,n+1):
        value *= i
    return value

print("factorial(3) : ",factorial(3))
print()

# 재귀함수 팩토리얼

def factorial_rec(n):
    if n == 1:
        return n
    else:
        return n * factorial_rec(n-1)

print("factorial(1) : ",factorial_rec(1))
print("factorial(2) : ",factorial_rec(2))
print("factorial(3) : ",factorial_rec(3))
print("factorial(4) : ",factorial_rec(4))
print("factorial(5) : ",factorial_rec(5))
print()


# 재귀함수 피보나치(1)

def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
print("fibo(1) : ",fibo(1))
print("fibo(2) : ",fibo(2))
print("fibo(3) : ",fibo(3))
print("fibo(4) : ",fibo(4))
print("fibo(5) : ",fibo(5))
print()


# 재귀함수 피보나치(2) - 연산 카운트

counter = 0

def fibo(n):
    print(f"fibo({n})을 구합니다.")
    global counter
    counter += 1

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

fibo(10)
print("fibo(10) counter : ",counter) # 이미 계산한 것도 또 계산 -> 메모리, 시간 낭비
print()


# 재귀함수 피보나치(3) - 메모이제이션

dicta = {
    1 : 1,
    2: 1
}

def fibo(n):
    if n in dicta:
        return dicta[n]
    else:
        output = fibo(n-1) + fibo(n-2)
        dicta[n] = output
        return output

print("fibo(10) : ",fibo(10))
print("fibo(20) : ",fibo(20))
print("fibo(30) : ",fibo(30))
print("fibo(40) : ",fibo(40))
print("fibo(50) : ",fibo(50))
print()