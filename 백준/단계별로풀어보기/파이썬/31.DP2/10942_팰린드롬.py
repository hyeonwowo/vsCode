import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    
    dp = [1] * n 
    for i in range(1, n):
        dp[i] = 
        # 자기 위치까지의 펠린드롬 길이를 구하기
    
    # ls : 1 2 1 3 1 2 1
    # dp : 1 1 3 1 3 5 6
    query = int(sys.stdin.readline())
    res = []
    for _ in range(query):
        s, e = map(int, sys.stdin.readline().split())
        res.append(dp[0]) 
        
    print('\n'.join(map(str, res)))