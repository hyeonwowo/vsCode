class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert key into the tree
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        # 중복은 무시
        return node

    # Search key in the tree
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    # Inorder traversal (sorted order)
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    # Find min value
    def find_min(self):
        node = self.root
        if not node:
            return None
        while node.left:
            node = node.left
        return node.key

    # Find max value
    def find_max(self):
        node = self.root
        if not node:
            return None
        while node.right:
            node = node.right
        return node.key
    
if __name__ == "__main__":
    bst = BinarySearchTree()
    for num in [10, 5, 20, 3, 7, 15, 30]:
        bst.insert(num)

    print("Inorder Traversal:", bst.inorder())  # [3, 5, 7, 10, 15, 20, 30]
    print("Search 7:", bst.search(7))           # True
    print("Search 100:", bst.search(100))       # False
    print("Min:", bst.find_min())               # 3
    print("Max:", bst.find_max())               # 30

