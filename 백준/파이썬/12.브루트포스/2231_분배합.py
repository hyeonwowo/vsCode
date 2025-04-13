import sys

def divideSum(k):
    # for 루프를 돌려서 해당 n을 만족시키는 수가 나오자마자 리턴
    for n in range(100,1000):
        n100,n10,n1 = divide(n)
        result = n + n100 + n10 + n1
        if k == result:
            return n
    return 0

def divide(n):
    n100,n = n//100, n%100
    n10,n = n//10, n%10
    n1 = n
    return n100, n10, n1

if __name__ == "__main__":
    print(divideSum(int(input())))