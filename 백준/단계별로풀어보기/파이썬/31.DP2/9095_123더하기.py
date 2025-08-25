import sys

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    
    dp = [0] * 12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    for i in range(4, 12):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
    for _ in range(t):
        n = int(sys.stdin.readline())  # ✅ 사용자로부터 n 입력
        print(dp[n])  # ✅ 해당 n에 대한 값 출력
