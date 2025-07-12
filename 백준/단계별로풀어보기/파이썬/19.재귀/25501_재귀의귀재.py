import sys
sys.setrecursionlimit(10**6)

def pelindrom(st, l, r, cnt):
    if l >= r:
        return 1, cnt
    else:
        if st[l] == st[r]:
            cnt += 1
            return pelindrom(st, l+1, r-1, cnt)
        else:
            return 0, cnt

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    
    res = []
    for _ in range(n):
        st = sys.stdin.readline().strip()
        res.append(pelindrom(st, 0, len(st)-1, 1))
        
    for ele in res:
        print(*ele)