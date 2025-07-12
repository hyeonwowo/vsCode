import sys
sys.setrecursionlimit(10**6)

def star(n):
    if n == 0:
        return ['*']

    else:
        prev = star(n-1)
        res = []
        
        # 상단
        for i, row in enumerate(prev):
            res.append(row + " " * i + row)
    
        # 하단
        for row in prev:
            res.append(row)
             
        return res
    
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print('\n'.join(star(n)))