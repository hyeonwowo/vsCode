import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        n = int(sys.stdin.readline())
        coin = list(map(int, sys.stdin.readline().split()))
        total = int(sys.stdin.readline())
        
        dp = [0] * (total+1)
        dp[0] = 1
        
        for c in coin: # 동전을 먼저 순회 - 하앗ㅇ 동전의 사용 순서를 오름차순으로 고정
            for i in range(c, total+1):
                dp[i] += dp[i-c]
                
        print(dp[-1])