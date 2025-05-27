import sys # Dp 사용

def increasenumsum(lst):
    dp = [1] * n
    for i in range(1,n):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    print(increasenumsum(lst))