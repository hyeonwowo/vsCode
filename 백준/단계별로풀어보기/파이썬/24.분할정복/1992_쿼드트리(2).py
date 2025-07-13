import sys
sys.setrecursionlimit(10**6)

def isColor(n, lst):
    color = lst[0][0]
    for i in range(n):
        for j in range(n):
            if lst[i][j] == color:
                continue
            else:
                return False
    return True

def paper(n, lst):
    if isColor(n, lst):
        color = lst[0][0]
        res.append("(")
        res.append(color)
        res.append(")")
        return
    else:
        half = n // 2
        onelst = [row[:half] for row in lst[:half]]
        twolst = [row[half:] for row in lst[:half]]
        threelst = [row[:half] for row in lst[:half]]
        fourlst = [row[half:] for row in lst[:half]]
        
        for l in [onelst, twolst, threelst, fourlst]:
            paper(half, l)        

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
    
    res = []
    paper(n, lst)
    print(res)