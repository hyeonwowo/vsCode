import sys

def consqsum(numlst):
    dp = [None] * n
    dp[0] = numlst[0]
    for i in range(1,n): # 이전 Dp값 + 현재 numlst 값 < 현재 Numlst 값이면, dp 업데이트 (이전 dp값 + 현재 numlst값이면, 이전 Dp값(이전 인덱스까지의 최댓값)이 도움이 안된다는거임. 그래서 새롭게 갱신해줌)
        dp[i] = max(dp[i-1] + numlst[i], numlst[i]) # 중요개념 ! : 최댓값 = 최댓값 + 최댓값 + ... + 최댓값. 최댓값은 작은 최댓값의 합으로 이루어진다
    return dp

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    numlst = list(map(int, sys.stdin.readline().split()))
    print(consqsum(numlst))