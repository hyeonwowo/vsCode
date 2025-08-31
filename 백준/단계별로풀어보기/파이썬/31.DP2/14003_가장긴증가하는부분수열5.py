import sys # dp - 시간초과 발생

def longest(lst):
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp, max(dp)

def findpath(dp, maxval):
    res = []
    curr = maxval
    
    for i in range(n-1,-1,-1):
        if curr == 0:
            break
        if curr == dp[i]:
            res.append(lst[i])
            curr -= 1
    return reversed(res)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    
    dp, maxval = longest(lst)
    res = findpath(dp, maxval)
    
    print(maxval)
    print(*list(res))