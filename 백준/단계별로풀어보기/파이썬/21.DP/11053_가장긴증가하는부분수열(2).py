import sys

def increasenumsum(lst):
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if lst[j] < lst[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    maxlen = max(dp)
    idx = dp.index(maxlen)

    lis = []
    while idx != -1:
        lis.append(lst[idx])
        idx = prev[idx]
    lis.reverse()

    return lis

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    print(increasenumsum(lst))
