import sys

def mostincrease():
    dp = [1] * n
    res = []
    for i in range(n):
        for j in range(i):
            if lst[j] < lst[i]:
                prev = dp[i]
                dp[i] = max(dp[i], dp[j]+1)
                if dp[i] == prev+1:
                    res.append(lst[i])
    return res

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    print(*mostincrease())