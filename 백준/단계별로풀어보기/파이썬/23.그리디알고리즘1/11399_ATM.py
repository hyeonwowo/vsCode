import sys

def ATM(lst):
    dp = [0] * n
    dp[0] = lst[0]
    for i in range(1,n):
        dp[i] = dp[i-1] + lst[i]
    return sum(dp)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    print(ATM(sorted(lst)))