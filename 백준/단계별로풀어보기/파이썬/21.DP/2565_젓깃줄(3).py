import sys

def electline(line):
    lst = [b for _,b in line]
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if lst[j] < lst[i]:
                dp[i] = max(dp[j] + 1, dp[i])
    return n - max(dp)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    line = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(electline(sorted(line)))