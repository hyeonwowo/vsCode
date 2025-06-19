import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
    def insert(self, key):
        return self._insert(self.root, key)
    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node
    def search(self, key):
        return self._search(self.root, key)
    def _search(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        elif key > node.key:
            return self._search(node.right, key)
    def find_min(self, key):
        node = self.root
        if not node:
            return None
        while node.left:
            node = node.left
        return node.key
    def find_max(self, key):
        node = self.root
        if not node:
            return None
        while node.right:
            node = node.right
        return node.key
    
if __name__ == "__main__":
    bst = BST()
    for num in [10,5,20,3,7,15,30]:
        bst.insert(num)
        
        