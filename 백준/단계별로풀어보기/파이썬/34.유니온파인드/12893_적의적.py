import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    parent[b] = a

if __name__ == "__main__":
    N, M = map(int, input().split())
    parent = [i for i in range(N+1)]
    enemy = [0] * (N+1)  
    flag = 1
    for _ in range(M):
        a, b = map(int, input().split())

        ra = find(a)
        rb = find(b)

        if ra == rb:
            flag = 0
            break

        if enemy[a]:
            union(enemy[a], b)
        else:
            enemy[a] = b

        if enemy[b]:
            union(enemy[b], a)
        else:
            enemy[b] = a

    print(flag)
