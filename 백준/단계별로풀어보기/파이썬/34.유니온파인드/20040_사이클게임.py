import sys # 2144ms

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    roota, rootb = find(a), find(b)
    if size[roota] < size[rootb]:
        parent[roota] = rootb
        size[rootb] += size[roota]
    else:
        parent[rootb] = roota
        size[roota] += size[rootb]

def connected(a, b):
    roota, rootb = find(a), find(b)
    if roota == rootb:
        return True # Cycle
    else:
        return False # No Cycle

if __name__ == "__main__":
    v, e = map(int, sys.stdin.readline().split())
    parent = [i for i in range(v)]
    size = [1] * v
    cnt = []
    
    for i in range(1,e+1):
        v, w = map(int, sys.stdin.readline().split())
        if connected(v, w):
            cnt.append(i)
        union(v, w)
    
    if len(cnt) == 0:
        print(0)
    else:
        print(cnt[0])