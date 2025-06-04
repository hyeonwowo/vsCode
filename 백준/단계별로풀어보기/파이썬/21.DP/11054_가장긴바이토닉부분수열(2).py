import sys

def longestbitonic(lst):
    updp = upbitonic(lst)
    downdp = downbitnoin(lst)
    maxdpval = 0
    
    for i in range(n):
        cand = updp[i] + downdp[i] - 1
        if cand > maxdpval:
            maxdpval = cand
    return maxdpval

def upbitonic(lst):
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

def downbitnoin(lst):
    dp = [1] * n
    for i in range(n-1, -1,-1):
        for j in range(n-1,i,-1):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    print(longestbitonic(lst))
    
    # print(upbitonic(lst))
    # print(downbitnoin(lst))