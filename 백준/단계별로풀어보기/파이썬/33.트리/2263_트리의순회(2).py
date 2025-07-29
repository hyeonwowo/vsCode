import sys
sys.setrecursionlimit(10**6)

def build(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return None
    
    root_val = postorder[post_end]
    root_idx = inorder_index[root_val]
    left_size = root_idx - in_start
    
    left = build(in_start, root_idx - 1, post_start, post_start + left_size - 1)
    right = build(root_idx + 1, in_end, post_start + left_size, post_end - 1)
    
    return (root_val, left, right)

def preorder_traverse(node):
    if node is None:
        return
    res.append(node[0])
    preorder_traverse(node[1])
    preorder_traverse(node[2])

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    inorder = list(map(int, sys.stdin.readline().split()))
    postorder = list(map(int, sys.stdin.readline().split()))
    
    inorder_index = {num: i for i, num in enumerate(inorder)}
    
    root = build(0, n - 1, 0, n - 1)
    
    res = []
    preorder_traverse(root)
    print(*res)
