import sys

def triangle(n):
    dp = [0] * (n+3) # (n+1)로 초기화시 만약 n이 1이면, dp[0] dp[1]까지 초기화, dp[2], dp[3]은 없기에 인덱스에러 발생
    dp[1] = dp[2] = dp[3] = 1

    for n in range(4, n+1):
        dp[n] = dp[n-2] + dp[n-3]
    return str(dp[n])

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    result = []
    for _ in range(n):
        result.append(triangle(int(sys.stdin.readline())))
    print('\n'.join(result))
    