# 7. 재귀(Recursion) 활용
# 문제: n번째 피보나치 수를 반환하는 재귀 함수 fibonacci(n)을 작성하세요.
# (예: fibonacci(5) → 5, fibonacci(10) → 55)

def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__=="__main__":
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(4))
    print(fibonacci(5))
    print(fibonacci(6))
    print(fibonacci(7))