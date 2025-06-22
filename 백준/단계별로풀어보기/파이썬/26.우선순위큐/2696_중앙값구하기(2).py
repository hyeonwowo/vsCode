import sys
import heapq
# bst의 left < key < right 성질을 이용하고자 하였지만, 이건 안됨.. 넣는 순서에 따라 root값이 다 다름 -> heapq를 사용해야함
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node
    
    def middle(self):
        return self.root.key

if __name__ == "__main__":
    bst = BST()
    bst.insert(3)
    bst.insert(4)
    bst.insert(1)
    bst.insert(2)
    bst.insert(5)
    print(bst.middle())
    