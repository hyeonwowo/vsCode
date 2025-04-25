import sys

def bridge(n):
    res = []
    for _ in range(n):
        res.append(bino_coef(*map(int,sys.stdin.readline().split())))
    return '\n'.join(map(str,res))

def bino_coef(n, r):
    n, r = max(n,r), min(n,r)
    cache = [[0 for _ in range(r+1)] for _ in range(n+1)] # 이항계수 전체 피라미드를 만들지는 않음. 목표로 삼은 (n,r)에 도달하기 위해 필요한 범위만큼만 테이블 생성

    for i in range(n+1):
        cache[i][0] = 1
    for i in range(r+1):
        cache[i][i] = 1

    for i in range(1, n+1):
        for j in range(1, r+1):
            cache[i][j] = cache[i-1][j] + cache[i-1][j-1]
    return cache[n][r]


if __name__ == "__main__":
    print((bridge(int(input()))))