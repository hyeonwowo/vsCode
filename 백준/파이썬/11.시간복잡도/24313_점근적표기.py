import sys

def is_big_o(a1, a0, c, n0):
    for n in range(n0, 101):  # n0 이상 모든 n (문제 조건: n ≤ 100)
        fn = a1 * n + a0
        gn = c * n
        if fn > gn:
            return 0
    return 1

if __name__ == "__main__":
    a1, a0 = map(int, sys.stdin.readline().split())
    c = int(sys.stdin.readline())
    n0 = int(sys.stdin.readline())
    print(is_big_o(a1, a0, c, n0))
