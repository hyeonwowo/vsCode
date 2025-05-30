import sys

def tile(n):
    dp = [0] * (n+2) # (n+1)로 초기화시, 인덱스에러 발생. 만약 n == 1인 경우, 아리에서 초기화한 dp[2] 라는 인덱스는 존재하지 않기에 인덱스 에러 발생. n == 1, dp[0] dp[1]... dp[2]는 존재하지 않으니 인덱스 에러 발생
    dp[1],dp[2] = 1,2
    
    for n in range(3,n+1):
        dp[n] = (dp[n-1] + dp[n-2]) % 15746 # 여기서 % 15746을 수행해야만, 메모리초과 발생 방지
    
    return dp[n] # 여기서 % 15746 수행시, 메모리초과
    
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(tile(n))