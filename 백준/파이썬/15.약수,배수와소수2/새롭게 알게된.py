# 소수구하기 알고리즘
import math

def findnum(k):
    for i in range(2, math.isqrt(k) + 1): # 입력한 수의 절반의 위치까지만 연산 수행
        if k % i == 0: return False
    return True