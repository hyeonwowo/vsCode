import sys # 중위, 후위순회 -> 전위순회 변경
sys.setrecursionlimit(10**6)
# 후위순회의 마지막 노드 : 루트 -> 이 루트를 기준으로 작은거, 좌측 서브트리. 큰거, 우측서브트리 -> 해당과정 반복 (노드가 한개일 때 까지)

def build(in_start, in_end, post_start, post_end): # 트리 복원
    if in_start > in_end or post_start > post_end:
        return None
    
    root_val = postorder[post_end]
    root_idx = inorder_index[root_val]
    left_size = root_idx - in_start
    
    left = build(in_start, root_idx - 1, post_start, post_start + left_size - 1)
    right = build(root_idx + 1, in_end, post_start + left_size, post_end - 1)
    
    return (root_val, left, right)

def preorder_traverse(node): # 복원한 트리 기준 전위순회 돌림
    if node is None:
        return
    res.append(node[0])
    preorder_traverse(node[1])
    preorder_traverse(node[2])

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    inorder = list(map(int, sys.stdin.readline().split()))
    postorder = list(map(int, sys.stdin.readline().split()))
    
    inorder_index = {num: i for i, num in enumerate(inorder)} # 트리 재구성시 사용
    
    root = build(0, n - 1, 0, n - 1)
    
    res = []
    preorder_traverse(root)
    print(*res)
