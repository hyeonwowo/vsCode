class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        
# node = insert() 구조를 따르는 이유
# 이미 연결되어 있는데 왜 또 연결 ? : 대부분의 경우 연결은 유지, 일부 경우(자식이 None)인 경우 새로운 노드를 리턴받아 연결
# 바뀌지 않는 경우도 있지 않나 ? : 그래도 코드의 일관성과 안정성을 위해 모든 경우에 연결
# 연결을 하는 경우에만 추가해서 연산횟수를 낮추는게 좋지 않나 ? : 연결과정이 어차피 O(1)이라 지장이 없을 뿐더러, 새로운 노드를 삽입했다는 과정을 확인하는 연산시간이 더 걸림

    # ✅ insert(key)
    def insert(self, key):
        def _insert(node, key): # 반환값 node
            if node is None:
                return Node(key) # 새로운 노드를 삽입한 결과를 부모 노드의 자식 포인터에 다시 저장
            if key < node.key:
                node.left = _insert(node.left, key) # 그냥 직관적으로 생각하면 될 듯. key보다 작으니.. 오른쪽이 아니고.. -> 키보다 작으면 왼쪽 node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            # 중복 키는 무시
            return node # 최하단에서 생성된 노드를 위쪽으로 올려주기 위한 return
        
        self.root = _insert(self.root, key) # _insert()가 **완성된 트리의 루트(예: Node(50))**를 반환해서 self.root에 연결


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
            # 삭제 노드 위치 탐색
            if node is None:
                return
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
                
            # 삭제 연산 (자식0, 자식1, 자식2  )
            else:
                # 자식이 하나
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else: # 자식이 두개일때, 오른쪽 서브트리의 최소 노드를 삭제한 자리에 삽입
                    temp = _min_value_node(node.right) 
                    node.key = temp.key # 오른쪽 서브트리 최소노드를 현재 자리에 삽입 (기존노드는 자연스럽게 지워짐)
                    node.root = _delete(node.right, temp.key) # 오른쪽 서브트리 최소노드는 지워진 자리에 가있으므로, 기존 오른쪽 서브트리 최소노드 제거 (제거 안하면 중복됨)
            return node

        self.root = _delete(self.root, key)

    # ✅ inorder() → 정렬된 key 리스트
    def inorder(self):
        result = []
        def _inorder(node):
            if node: # 노드가 존재할 때만 순회 (None이면 안함)
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
