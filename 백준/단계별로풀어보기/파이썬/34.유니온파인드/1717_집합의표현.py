import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축 : 세로가 아닌 가로로 (부모노드에서 루트노드로, 한줄씩 루트노드로 가지 않고 한번에 루트로 물림)
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if size[rootX] < size[rootY]:
            parent[rootX] = rootY
            size[rootY] += size[rootX]
        else:
            parent[rootY] = rootX
            size[rootX] += size[rootY]
            
if __name__ == "__main__":
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    size = [1] * (n + 1)

    result = []
    for _ in range(m):
        cmd, a, b = map(int, input().split())
        if cmd == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                result.append("YES")
            else:
                result.append("NO")

    print('\n'.join(result))
