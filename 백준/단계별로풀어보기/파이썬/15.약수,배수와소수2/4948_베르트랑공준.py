import sys
import math

def count_primes_between(n):
    m = 2 * n
    is_prime = [True] * (m + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, math.isqrt(m) + 1):
        if is_prime[i]:
            for j in range(i * i, m + 1, i):
                is_prime[j] = False
    return sum(1 for i in range(n + 1, m + 1) if is_prime[i])

def main():
    lst = []
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        lst.append(count_primes_between(n))
    
    print('\n'.join(map(str, lst)))

if __name__ == "__main__":
    main()
