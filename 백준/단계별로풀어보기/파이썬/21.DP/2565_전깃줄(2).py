import sys

def electline(line):
    dp = [1] * n
    lst = [b for _,b in line]
    for i in range(1,n):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[j]+1, dp[i])
    return n - max(dp)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    line = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(electline(sorted(line)))