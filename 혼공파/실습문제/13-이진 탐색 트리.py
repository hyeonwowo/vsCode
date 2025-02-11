# 10. 이진 검색 트리(Binary Search Tree) 구현
# 문제: 기본적인 이진 검색 트리(BST) 클래스를 구현하세요.

# insert(value): 노드 삽입
# search(value): 값 존재 여부 확인
# inorder_traversal(): 중위 순회 출력

class Node:
    def __init__(self, key): # 새 노드 생성시, left - right는 빈상태
        self.key = key # 노드에 지정된 값
        self.left = None # 왼쪽 자식 노드
        self.right = None # 오른쪽 자식 노드

class BST:
    def __init__(self): # root : 트리의 루트 노드 (초기값은 : None, 빈트리)
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None: # 해당 자리가 비어있을 때
            return Node(key) # key값을 가진 새로운 노드 생성 - left,right 는 None
        if key < node.key: # 기존 노드보다 값이 작을 때 -> 왼쪽으로 이동
            node.left = self._insert_recursive(node.left, key) 
        else: # 기존 노드보다 값이 클 때 -> 오른쪽으로 이동
            node.right = self._insert_recursive(node.right, key)
        return node

    def inorder(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.key, end=" ")
            self._inorder_recursive(node.right)

if __name__=="__main__":
    tree = BST()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(2)
    tree.insert(7)
    tree.inorder()  # 2 5 7 10 15 출력