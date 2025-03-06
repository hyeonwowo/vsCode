class BST: # 이진탐색트리 : 자식1 < 부모 < 자식2
    class Node:
        def __init__(self, key, val): # key, value = 노드번호, 값
            self.key = key # 노드 번호, 값 초기화
            self.val = val
            self.left = None # 첫 노드 생성시
            self.right = None 
            self.count = 1 # 해당 노드를 루트로 하는 서브트리의 노드 개수 저장

    def __init__(self): # 초기화 - 루트노드 생성
        self.root = None
    
    def get(self, key): # key값에 따른 value 얻어오기
        x = self.root # 루트 노드
        while x != None: # 노드가 없으면, return None
            if key < x.key: # 탐색하려는 키가, 현재 키보다 작으면
                x = x.left # 왼쪽 노드로
            elif key > x.key: # 탐색하려는 키가, 현재 키보다 크면
                x = x.right # 오른쪽 노드로
            else: # 탐색키 == 현재키
                return x.val  # 현재 노드 value값 반환
        return None # The key was NOT found

# *** 중요 ***
# putOnNode(x.left, key, val)를 호출하는 이유:
# 왼쪽 서브트리로 내려가면서 탐색 및 삽입을 재귀적으로 수행하기 위해.

# x.left = putOnNode(x.left, key, val)로 값을 다시 저장하는 이유:
# 새롭게 삽입된 노드(혹은 수정된 서브트리)를 현재 노드와 연결하기 위해.

    def put(self, key, val): # 새로운 키 삽입
        def putOnNode(x, key, val): # 순환호출 사용
            if x == None: # 도달한 자리에 아무것도 없으면, 그 자리에 삽입
                return self.Node(key, val) # 노드 삽입
            if key < x.key: # 새로운 키가, 현재 노드 위치 키보다 작으면
                x.left = putOnNode(x.left, key, val) # *** 중요 ***
            elif key > x.key: # 새로운 키가, 현재 노드 위치 키보다 크면
                x.right = putOnNode(x.right, key, val) # 우측노드로 이동해서 순환호출 사용
            else: 
                x.val = val # 새로운키 == 현재키, value값 업데이트
            x.count = self.sizeOnNode(x.left) + 1 + self.sizeOnNode(x.right) # x기준 자식노드의 총합 (좌측자식들 + 자기자신 + 우측자식들)
            return x
        self.root = putOnNode(self.root, key, val)

    def min(self): # 최소키값 - 맨 왼쪽
        if self.root == None: 
            return None
        else:
            x = self.root
            while x.left != None:
                x = x.left
            return x.key
    
    def max(self): # 최대키값 - 맨 오른쪽
        if self.root == None: 
            return None
        else:            
            x = self.root
            while x.right != None:
                x = x.right
            return x.key

    def floor(self, key): # 주어진 키보다 작거나 같은 트리 내부 최대값 탐색 - 좌1, 우n
        def floorOnNode(x, key): # 순환함수
            if x == None: 
                return None # t = floorOnNode(x.right, key) : 리턴값 1
            if key == x.key: 
                return x # t = floorOnNode(x.right, key) : 리턴값 2
            elif key < x.key:
                return floorOnNode(x.left, key) # t = floorOnNode(x.right, key) : 리턴값 3

            t = floorOnNode(x.right, key)
            if t != None: 
                return t # 현위치 노드의 우측 서브 트리에서 가장 큰 노드 (서브트리에서 최우측 노드)
            else: # t == None
                return x
            
        x = floorOnNode(self.root, key)
        if x == None: 
            return None
        else: # x != None
            return x.key

    def ceiling(self, key): # 주어진 키도다 크거나 같은 트리 내부 최소값 탐색 - 우1, 좌n
        def ceilingOnNode(x, key): 
            if x == None: 
                return None
            if key == x.key:
                return x
            elif x.key < key: 
                return ceilingOnNode(x.right, key)

            t = ceilingOnNode(x.left, key)
            if t != None: 
                return t
            else: 
                return x
            
        # 함수 시작
        x = ceilingOnNode(self.root, key)
        if x == None: 
            return None
        else: 
            return x.key

    def sizeOnNode(self, x): # 주어진 노드 x를 루트로 하는 서브트리 노드 개수 반환
        if x == None: 
            return 0
        else: 
            return x.count # 각 노드마다 x.count가 저장되어있음.

    def size(self): # 트리 전체 노드 개수 반환
        return self.sizeOnNode(self.root) # 해당 노드 기준으로 모든 자식노드 수 반환

    def rank(self, key): # key 보다 작은 노드 개수 반환
        def rankOnNode(x, key): # rank(key) on the subtree rooted at x
            if x == None: # 재귀함수의 종료조건
                return 0
            if key < x.key: 
                return rankOnNode(x.left, key)
            elif key > x.key: # key보다 현재 노드가 작다면, 현재노드를 포함한 서브트리 모두의 전체 노드는, key보다 작음
                return self.sizeOnNode(x.left) + 1 + rankOnNode(x.right, key) # 왼쪽 서브트리 + 자기자신 + 오른쪽 서브트리
            else: 
                return self.sizeOnNode(x.left) # key == x.key
        return rankOnNode(self.root, key)

    def select(self, idx): # 트리에서 idx번째로 작은 원소를 찾음
        def selectOnNode(x, idx): # idx-th element on the subtree rooted at x
            if x == None: # 재귀함수의 종료조건
                return None # idx-th element does not exist
            if idx < self.sizeOnNode(x.left): 
                return selectOnNode(x.left, idx)
            elif idx > self.sizeOnNode(x.left): 
                return selectOnNode(x.right, idx - self.sizeOnNode(x.left) - 1)
            else: 
                return x.key # idx == self.sizeOnNode(x.left)
        return selectOnNode(self.root, idx)        

    def inorder(self): # 트리를 중위순회하여 정렬된 리스트 반환        
        def inorderOnNode(x, q):
            if x == None: 
                return
            inorderOnNode(x.left, q)
            q.append(x.key)
            inorderOnNode(x.right, q)
        q = []
        inorderOnNode(self.root, q)
        return q

    def delete(self, key): # 주어진 key를 삭제
        def minOnNode(x): # Find node with minimum key from the subtree rooted at x
            if x == None: 
                return None
            else:            
                while x.left != None:
                    x = x.left
            return x
        def deleteOnNode(x, key):
            if x == None: 
                return None
            if key < x.key: x.left = deleteOnNode(x.left, key)
            elif key > x.key: x.right = deleteOnNode(x.right, key)
            else:
                if x.right == None: 
                    return x.left
                if x.left == None: 
                    return x.right
                t = x
                x = minOnNode(t.right)
                x.right = deleteOnNode(t.right, x.key)
                x.left = t.left
            x.count = self.sizeOnNode(x.left) + 1 + self.sizeOnNode(x.right)
            return x
        self.root = deleteOnNode(self.root, key)

if __name__ == "__main__":  
    bst = BST() 
    print(bst.size())
    print("min", bst.min())
    print("max", bst.max())
    print()

    print("put")
    bst.put("a",1)
    bst.put("c",2)
    bst.put("e",3)
    bst.put("b",4)
    bst.put("c",5) # 같은 키가 들어오면 업데이트
    print(bst.size()) # size는 그래서 4
    print()

    print("get")
    print(bst.get("a"))
    print(bst.get("b"))
    print(bst.get("c"))
    print(bst.get("d"))
    print(bst.get("e"))
    print(bst.floor("a"))
    print(bst.floor("b"))   
    print()

    print("ceiling") 
    print(bst.ceiling("a"))
    print(bst.ceiling("b"))
    print(bst.ceiling("c"))
    print(bst.ceiling("d"))
    print(bst.ceiling("e"))
    print(bst.ceiling("f"))
    print()

    print("min", bst.min())
    print("max", bst.max())
    print()

    print("rank")
    print(bst.rank("a"))
    print(bst.rank("b"))
    print(bst.rank("c"))
    print(bst.rank("d"))
    print(bst.rank("e"))
    print(bst.rank("f"))
    print()

    print("select")
    print(bst.select(-1))
    print(bst.select(0))
    print(bst.select(1))
    print(bst.select(2))
    print(bst.select(3))
    print(bst.select(4))
    print(bst.select(5))
    print(bst.select(6))
    print()

    print("inorder traversal")
    bst2 = BST()
    bst2.put("S",1)
    bst2.put("E",2)
    bst2.put("Y",3)
    bst2.put("A",4)
    bst2.put("R",5)
    bst2.put("C",6)
    bst2.put("H",7)
    bst2.put("M",8)
    print()

    for k in bst2.inorder():
        print(k)
    print(bst2.rank("H"))
    print(bst2.select(4))
    print()

    print("delete")
    bst2.delete("C")
    print(bst2.inorder())   
    print()

    bst2.delete("E")
    print(bst2.inorder())   
    print()

    bst2.delete("Y")
    print(bst2.inorder())   
    print()

    bst2.delete("S")
    print(bst2.inorder())   
    print()

    bst2.delete("F") # Delete a key not in BST, so BST remains the same
    print(bst2.inorder())   


