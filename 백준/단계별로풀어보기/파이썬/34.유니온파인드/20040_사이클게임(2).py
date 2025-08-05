import sys # 612ms
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    roota, rootb = find(a), find(b)
    if roota == rootb:
        return True  # 사이클 발생
    if size[roota] < size[rootb]:
        parent[roota] = rootb
        size[rootb] += size[roota]
    else:
        parent[rootb] = roota
        size[roota] += size[rootb]
    return False

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    parent = [i for i in range(n)]
    size = [1] * n

    for i in range(1, m + 1):
        a, b = map(int, sys.stdin.readline().split())
        if union(a, b):  # 여기서 cycle 여부를 한 번에 처리! + if문 내에서 함수 처리가 가능하다
            print(i)
            break
    else:
        print(0)
