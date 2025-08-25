import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    
    one_deminsion = [0] * (n+1)
    one_deminsion[0] = 1
    for i in range(1, n+1):
        one_deminsion[i] = one_deminsion[i-1] + (i+1)
        if one_deminsion[i] > n:
            break
        
    idx = 0
    three_deminsion = [0] * (n+1)
    three_deminsion[0] = 1
    for i in range(1, n+1):
        three_deminsion[i] = three_deminsion[i-1] + one_deminsion[i]
        if three_deminsion[i] > n:
            idx = i-1 # 특정구간까지의 idx를 기억해뒀다가
            break
    
    coins = three_deminsion[1:idx+1] # 바로 저장
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = i
        for num in coins:     
            if num > i: break
            if dp[i - num] + 1 < dp[i]:
                dp[i] = dp[i - num] + 1

    print(dp[n])
        