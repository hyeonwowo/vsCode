class Node: # 이진트리는 pop하는게 아니라, 빠른 탐색을 위해 사용
    def __init__(self, key, value=None):
        self.key = key # 노드를 정렬하고 탐색하는 기준값 (ex) 학번, 아이디, 이름)
        self.value = value if value is not None else key # 만약 value가 주어졌다면 그 값을 쓰고, 아니면 key를 그대로 value로 저장
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # ✅ insert(key, value)
    def insert(self, key, value=None): # 새로운 노드 BST에 삽입
        def _insert(node, key, value):
            if node is None:
                return Node(key, value)
            if key < node.key:
                node.left = _insert(node.left, key, value)
            elif key > node.key:
                node.right = _insert(node.right, key, value)
            else:
                node.value = value  # 키 중복이면 값만 업데이트
            return node

        self.root = _insert(self.root, key, value)

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

    # ✅ get(key) → value
    def get(self, key):
        def _get(node, key):
            if node is None:
                return None
            if key == node.key:
                return node.value
            elif key < node.key:
                return _get(node.left, key)
            else:
                return _get(node.right, key)
        return _get(self.root, key)

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
            else:  # key == node.key
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = _min_value_node(node.right)
                node.key = temp.key
                node.value = temp.value
                node.right = _delete(node.right, temp.key)
            return node

        self.root = _delete(self.root, key)

    # ✅ inorder() → 리스트로 반환
    def inorder(self): # 이진탐색트리의 내용을 중위순회, 정렬된 리스트로 반환
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
