# 메모이제이션 피보나치 수열 계산

dicta = {
    1 : 1,
    2 : 1
}

def fibo(n):
    if n in dicta:
        return dicta[n]
    else:
        result = fibo(n-1) + fibo(n-2)
        dicta[n] = result
        return result

print("fibo(10) : ",fibo(10))
print("fibo(20) : ",fibo(20))
print("fibo(30) : ",fibo(30))
print("fibo(40) : ",fibo(40))
print("fibo(50) : ",fibo(50))
print()