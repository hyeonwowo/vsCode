import sys
sys.setrecursionlimit(10**7)

N = int(input())
parents = list(map(int, input().split()))
remove_node = int(input())

# 1. 자식 리스트 만들기
children = [[] for _ in range(N)]
root = -1

for i in range(N):
    if parents[i] == -1:
        root = i
    else:
        children[parents[i]].append(i)

# 2. 삭제될 노드 표시
removed = [False] * N

def dfs(u):
    removed[u] = True
    for v in children[u]:
        dfs(v)

# 루트를 삭제하는 경우
if remove_node == root:
    print(0)
    exit()

dfs(remove_node)

# 3. 리프 노드 개수 세기
leaf_count = 0
for i in range(N):
    if removed[i]:
        continue

    # 제거되지 않은 자식이 있는지 확인
    is_leaf = True
    for v in children[i]:
        if not removed[v]:
            is_leaf = False
            break

    if is_leaf:
        leaf_count += 1

print(leaf_count)
