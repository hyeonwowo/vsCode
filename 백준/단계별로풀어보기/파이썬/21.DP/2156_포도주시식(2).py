import sys

def wine(lst):
    if n == 1:
        return lst[0]
    if n == 2:
        return lst[0] + lst[1]
    if n == 3:
        return max(lst[0] + lst[1], lst[1] + lst[2], lst[0] + lst[2]) # lst[0] + lst[2] 조건이 누락되어있었음
    
    dp = [0] * n
    dp[0] = lst[0]
    dp[1] = lst[0] + lst[1]
    dp[2] = max(lst[0] + lst[1], lst[1] + lst[2], lst[0] + lst[2])
    
    for i in range(3, n): # 점화식은 맞게 짬 !
        dp[i] = max(dp[i-3] + lst[i-1] + lst[i], dp[i-2] + lst[i], dp[i-1])

    return max(dp) # dp[n-1]이 더 좋은 코드

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = [int(sys.stdin.readline()) for _ in range(n)]
    print(wine(lst))