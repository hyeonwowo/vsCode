import sys # 시간초과

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    
    # 원본 dp (연속합)
    dp = lst[:]  # 깊은 복사 !!
    for i in range(1, n):
        dp[i] = max(lst[i], dp[i-1] + lst[i])
    maxval = max(dp)
    
    # 원소 하나 제거하면서 검사
    for i in range(n):
        temp_lst = lst[:i] + lst[i+1:]   # i번째 제거한 새로운 리스트
        dp = temp_lst[:]                 # 깊은 복사 !!
        for j in range(1, n-1):
            dp[j] = max(temp_lst[j], dp[j-1] + temp_lst[j])
        maxval = max(maxval, max(dp))
        
    print(maxval)
