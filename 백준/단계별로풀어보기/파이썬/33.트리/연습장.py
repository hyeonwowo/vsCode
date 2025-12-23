class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value if value is not None else key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, key, value=None):
        def _insert(node, key, value):
            if node == None:
                return Node(key, value)
            if key < node.key:
                node.left = _insert(node.left, key, value)
            elif key > node.key:
                node.right = _insert(node.right, key, value)
            else:
                node.value = value
            return node
        
        self.root = _insert(self.root, key, value)
        
    def search(self, key):
        def _search(node, key):
            if key == node.key:
                return True
            elif key < node.key:
                return _search(node.left, key)
            elif key > node.key:
                return _search(node.right ,key)
            else:
                return False
        return _search(self.root, key)
    
    def get(self, key):
        def _get(node, key):
            if key == node.key:
                return node.value
            elif key < node.key:
                return _get(node.left, key)
            elif key > node.key:
                return _get(node.right, key)
            else:
                return None
        return _get(self.root, key)
    
    def delete(self, key):
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current
        
        def _delete(node, key):
            if node == None:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if node.left == None:
                    return node.right
                elif node.right == None:
                    return node.left
                else:
                    temp = _min_value_node(node.right)
                    node.key = temp.key
                    node.value = temp.value
                    node.right = _delete(node.right, temp.key)
                return node
    
        self.root = _delete(self.root, key)
        
    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append((node.key, node.value))
                _inorder(node.right)
        _inorder(self.root)
        return result

if __name__ == "__main__":
    bst = BST()
    bst.insert(50, "A")
    bst.insert(30, "B")
    bst.insert(70, "C")
    bst.insert(20, "D")
    bst.insert(40, "E")
    bst.insert(60, "F")
    bst.insert(80, "G")

    print("Search 40:", bst.search(40))  # True
    print("Get 60:", bst.get(60))        # F
    print("Inorder:", bst.inorder())     # [(20, 'D'), (30, 'B'), (40, 'E'), ...]

    bst.delete(70)
    print("Inorder after deleting 70:", bst.inorder())
