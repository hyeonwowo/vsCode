import sys

def consqsum(numlst):
    dp = [None] * n
    dp[0] = numlst[0]
    for i in range(1,n):
        if numlst[i] < dp[i-1] + numlst[i]:
            dp[i] = dp[i-1] + numlst[i]
        else:
            dp[i] = numlst[i]
    return max(dp)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    numlst = list(map(int, sys.stdin.readline().split()))
    print(consqsum(numlst))