import sys

def mostincrease():
    dp = [1] * n
    prev = [-1] * n
    
    for i in range(n):
        for j in range(i):
            if lst[j] < lst[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
                  
    idx = dp.index(max(dp))
    path = []  
    while idx != -1:
        path.append(lst[idx])
        idx = prev[idx]

    return max(dp), list(reversed(path))

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    maxval, path = mostincrease()
    print(maxval)
    print(*path)