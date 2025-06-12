import sys

def power(a,n):
    if n == 0: # 분할 (기저조건 : 더이상 쪼갤 수 없을때)
        return 1
    half = power(a, n//2) # 분할
    if n % 2 == 0:
        return half * half # 정복
    else:
        return half * half * a # 정복

if __name__ == "__main__":
    a, n, c = map(int, sys.stdin.readline().split())
    print(power(a,n) % c)
    