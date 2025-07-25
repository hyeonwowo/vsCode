class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # ✅ insert(key)
    def insert(self, key):
        def _insert(node, key): # 반환값 node
            if node is None:
                return Node(key) # 새로운 노드를 삽입한 결과를 부모 노드의 자식 포인터에 다시 저장
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            # 중복 키는 무시
            return node

        self.root = _insert(self.root, key)

    # ✅ search(key) → bool
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

    # ✅ delete(key)
    def delete(self, key):
        def _min_value_node(node):
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
                temp = _min_value_node(node.right) # 자식이 두개일때, 오른쪽 서브트리의 최소 노드를 삭제한 자리에 삽입
                node.key = temp.key
                node.right = _delete(node.right, temp.key)
            return node

        self.root = _delete(self.root, key)

    # ✅ inorder() → 정렬된 key 리스트
    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.key)
                _inorder(node.right)
        _inorder(self.root)
        return result

# ✅ 사용 예시
if __name__ == "__main__":
    bst = BST()
    for k in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(k)

    print("Search 40:", bst.search(40))  # True
    print("Search 90:", bst.search(90))  # False
    print("Inorder:", bst.inorder())     # [20, 30, 40, 50, 60, 70, 80]

    bst.delete(70)
    print("Inorder after deleting 70:", bst.inorder())  # [20, 30, 40, 50, 60, 80]
