class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

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
        def _search(node, key):
            if node is None:
                return False
            if key == node.key:
                return True
            elif key < node.key:
                return _search(node.left, key)
            else:
                return _search(node.right, key)
        return _search(self.root, key)
    
    def delete(self, key):
        def _minnode(node):
            current = node
            while current.left:
                current = current.left
            return current
    
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
                    temp = _minnode(node.right)
                    node.key = temp.key
                    node.right = _delete(node.right, temp.key)
            return node
        self.root = _delete(self.root, key)
    
    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.key)
                _inorder(node.right)
        _inorder(self.root)
        return result

if __name__ == "__main__":
    bst = BST()
    for k in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(k)

    print("Search 40:", bst.search(40))  # True
    print("Search 90:", bst.search(90))  # False
    print("Inorder:", bst.inorder())     # [20, 30, 40, 50, 60, 70, 80]

    bst.delete(70)
    print("Inorder after deleting 70:", bst.inorder())  # [20, 30, 40, 50, 60, 80]
