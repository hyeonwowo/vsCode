import sys
import math

def find_primes(n, m): # n ~ m까지의 소수 찾기
    is_prime = [True] * (m + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(math.sqrt(m)) + 1): # 처음부터 ~ m까지 소수 찾기
        if is_prime[i]:
            for j in range(i * i, m + 1, i):
                is_prime[j] = False

    # n부터 m까지의 소수만 출력
    result = [str(i) for i in range(n, m + 1) if is_prime[i]] # n ~ m까지 소수 탐색
    return '\n'.join(result)

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    print(find_primes(n, m))
