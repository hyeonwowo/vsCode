import sys # dp - 시간초과 (이분탐색으로 풀어야함)

def electronicLine(n, lst):
    dp = [1] * n
    
    for i in range(1,n):
        for j in range(i):
            if lst[j] < lst[i]:
                dp[i] = max(dp[j]+1, dp[i])
    return max(dp)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    
    print(n - electronicLine(n, lst))