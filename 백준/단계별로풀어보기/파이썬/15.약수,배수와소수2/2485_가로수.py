import sys

def gcd(a,b):
    while b>0:
        a,b = b, a%b
    return a

def loadTree(n):
    lst = [int(sys.stdin.readline()) for _ in range(n)]
    
    diffs = [lst[i+1] - lst[i] for i in range(n-1)]

    g = diffs[0]
    for d in diffs[1:]:
        g = gcd(g, d)

    # 총 필요한 나무 개수 = 전체 간격 // g
    total_gaps = (lst[-1] - lst[0]) // g
    return total_gaps - (n - 1)

if __name__ == "__main__":
    print(loadTree(int(sys.stdin.readline())))
