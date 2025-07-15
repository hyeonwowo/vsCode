import sys
input = sys.stdin.readline

MOD = 1000000007
MAX = 4000000

# 팩토리얼과 역원 배열 미리 계산
fact = [1] * (MAX + 1)
inv_fact = [1] * (MAX + 1)

# 팩토리얼 계산
for i in range(2, MAX + 1):
    fact[i] = fact[i - 1] * i % MOD

# 역원 계산 (페르마의 소정리 이용)
inv_fact[MAX] = pow(fact[MAX], MOD - 2, MOD)
for i in range(MAX - 1, 0, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

# 입력
n, k = map(int, input().split())

# 이항 계수 계산
if k < 0 or k > n:
    print(0)
else:
    result = fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
    print(result)
