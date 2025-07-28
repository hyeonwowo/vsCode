import sys

def preorder(node):
    res = []
    def _preorder(node):
        if node != '.':
            res.append(node)
            _preorder(tree[node][0])
            _preorder(tree[node][1])
    _preorder(node)
    return res

def inorder(node):
    res = []
    def _inorder(node):
        if node != '.':
            _inorder(tree[node][0])
            res.append(node)
            _inorder(tree[node][1])
    _inorder(node)
    return res

def postorder(node):
    res = []
    def _postorder(node):
        if node != '.':
            _postorder(tree[node][0])
            _postorder(tree[node][1])
            res.append(node)
    _postorder(node)
    return res
    

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    tree = {}
    for _ in range(n):
        parent, child1, child2 = sys.stdin.readline().split()
        tree[parent] = (child1, child2)
    
    print(*preorder('A'),sep='')
    print(*inorder('A'),sep='')
    print(*postorder('A'),sep='')
    