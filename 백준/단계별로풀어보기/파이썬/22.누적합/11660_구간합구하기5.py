import sys

def prefix_sum(lst, n):
    prefix = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + lst[i-1][j-1]
    return prefix

def query_sum(query, s):
    x1,y1,x2,y2 = query
    result = s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1]
    return result

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    query = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    s = prefix_sum(lst, n)
    
    for element in query:
        print(query_sum(element,s))