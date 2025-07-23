import sys # 수열 출력하기

def mostdecrease(lst):
    dp = [1] * n
    res = []
    for i in range(n):
        for j in range(i):
            if lst[i] < lst[j]:
                res.append(i)
                dp[i] = max(dp[i], dp[j] + 1)
    return res

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    print(mostdecrease(lst))