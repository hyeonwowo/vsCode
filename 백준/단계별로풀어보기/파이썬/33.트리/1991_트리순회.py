import sys

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
    
    def delete(self, key):
        def minval(node):
            current = node
            while current.left:
                current = current.left
            return current
        
        def _delete(node, key):
            if node is None:
                return
            elif node.key < key:
                node.left = _delete(node.left, key)
            elif node.key > key:
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
    
    def search(self, key):
        def _search(node, key):
            if node is None:
                return False
            if node.key == key:
                return True
            elif key < node.key:
                return _search(node.left, key)
            else:
                return _search(node.right, key)
        
        return _search(self.root, key)
    
    def inorder(self):
        res = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                res.append(node.key)
                _inorder(node.right)
        _inorder(self.root)
        return res

if __name__ == "__main__":
    n = int(sys.stdin.readline().split())
    bst = BST()
    for _ in range(7):
        pass