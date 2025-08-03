import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    roota, rootb = find(a), find(b)
    if roota == rootb:
        return size[roota] # size[rootb]도 사용해도 됨
    else:
        if size[roota] > size[rootb]:
            parent[rootb] = roota
            size[roota] += size[rootb]
            return size[roota]
        else:
            parent[roota] = rootb
            size[rootb] += size[roota]
            return size[rootb]
        
if __name__ == "__main__":
    T = int(sys.stdin.readline())
    res = []
    
    for _ in range(T):
        m = int(sys.stdin.readline())
        
        nametoid = {}
        parent = {}
        size = {}
        idx = 1
        
        for _ in range(m):
            p1, p2 = map(int, sys.stdin.readline().split())
            
            if p1 not in nametoid:
                nametoid[p1] = idx
                parent[idx] = idx
                size[idx] = 1
                idx += 1
            
            if p2 not in nametoid:
                nametoid[p2] = idx
                parent[idx] = idx
                size[idx] = 1
                idx += 1
                
            union(nametoid[p1], nametoid[p2])
            res.append(max)
            
    print(res)