import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    roota, rootb = find(a), find(b)
    if roota != rootb:
        if size[roota] < size[rootb]:
            parent[roota] = rootb
            size[rootb] += size[roota]
        else:
            parent[rootb] = roota
            size[roota] += size[rootb]

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    
    parent = [i for i in range(n + 1)]
    size = [1] * (n + 1)

    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j in range(1, n + 1):
            if row[j - 1] == 1:
                union(i, j)

    plan = list(map(int, input().split()))
    root = find(plan[0])
    flag = True
    for city in plan[1:]:
        if find(city) != root:
            flag = False
            break

    print("YES" if flag else "NO")
