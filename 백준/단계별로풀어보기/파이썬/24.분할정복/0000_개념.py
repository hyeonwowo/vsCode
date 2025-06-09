# 분할정복 알고리즘 : 큰 문제를 작은 문제로 분할하고, 각 작은 문제를 해결한 후, 그 결과를 합쳐서 전체 문제를 해결
# 큰문제 -> 작은문제들 -> 작은문제들해결 -> 작은문제들결과합치기 -> 큰문제해결

# 분할정복의 3단계
# 1. 분할 : 문제를 더 작은 하위 문제로 나눔 (보통 자기 자신과 구조가 같은 형태) 
# 2. 정복 : 하위 문제들을 재귀적으로 해결. 하위 문제가 충분히 작아지면 직접 해결
# 3. 결합 : 하위 문제의 결과를 결합하여 원래 문제의 해답 생성

# ex) 거듭제곱계산

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
    a, n = map(int, sys.stdin.readline().split())
    print(power(a,n))