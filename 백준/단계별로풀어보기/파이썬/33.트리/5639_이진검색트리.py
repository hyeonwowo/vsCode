import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        def _insert(node, key):
            if node is None:
                return Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            return node
        self.root = _insert(self.root, key)
                
    def search(self, key):
        def _search(node ,key):
            if node is None:
                return False
            if node.key == key:
                return True
            elif key < node.key:
                return _search(node.left, key)
            else:
                return _search(node.right, key)
        return _search(self.root, key)
    
    def delete(self, key):
        def minval(node):
            curr = node
            while curr.left:
                curr = curr.left
            return curr
        
        def _delete(node, key):
            if node is None:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    temp = minval(node.right)
                    node.key = temp.key
                    node.right = _delete(node.right, temp.key)
            return node
                    
        self.root = _delete(self.root ,key)
        
    def postorder(self, node):
        res = []
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                res.append(node.key)
        _postorder(node)
        return res
        
if __name__ == "__main__":
    bst = BST()
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            continue
        bst.insert(int(line))
    
    result = bst.postorder(bst.root)
    for val in result:
        print(val)
