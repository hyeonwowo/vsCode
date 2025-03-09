class BST: # 이진탐색트리 : 자식1 < 부모 < 자식2
    class Node:
        def __init__(self, key, val): # key, value = 노드번호, 값
            self.key, self.val = key, val # 노드 번호, 값 초기화
            self.left = self.right = None # 첫 노드 생성시 : ㅇ = ㅇ = ㅇ 모두 같은 값으로 초기화 가능
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
            # 해당 위치에 새로운 노드 삽입
            if x == None: # 도달한 자리에 아무것도 없으면, 그 자리에 삽입
                return self.Node(key, val) # 노드 삽입
            # 위치 탐색 과정
            if key < x.key: # 새로운 키가, 현재 노드 위치 키보다 작으면
                x.left = putOnNode(x.left, key, val) # *** 중요 ***
            elif key > x.key: # 새로운 키가, 현재 노드 위치 키보다 크면
                x.right = putOnNode(x.right, key, val) # 우측노드로 이동해서 순환호출 사용
            else: # 키 중복시
                x.val = val # 새로운키 == 현재키, value값 업데이트
            x.count = self.sizeOnNode(x.left) + 1 + self.sizeOnNode(x.right) # x기준 자식노드의 총합 (좌측자식들 + 자기자신 + 우측자식들)
            return x # return x를 해주는 이유 : 재귀적으로 변경된 노드를 부모 노드에 올바르게 연결
        self.root = putOnNode(self.root, key, val)

    def min(self): # 최소"키"값 - 맨 왼쪽
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
            if x == None: # case1) 중요 ! - key > x.key일 때 사용하는 중요한 조건, return t 값의 결과를 다룸
                return None # t = floorOnNode(x.right, key) : 리턴값 1
            
            if key == x.key:
                return x # t = floorOnNode(x.right, key) : 리턴값 2
            
            elif key < x.key:
                return floorOnNode(x.left, key) # t = floorOnNode(x.right, key) : 리턴값 3
            
            else: # key > x.key : 트리거 발동 - 트리거가 발동된 키를 기준으로 해당 키보다 큰 키가 있으면, 그 키에서 다시 트리거 발동, 해당 키보다 큰 키가 없으면 트리거 발동없이 해당키 리턴
                t = floorOnNode(x.right, key) # 서브트리의 탐색 결과를 반환해줌 (t가 받아줌)
                if t == None: # case1) 리턴값 : 파고들다가 조건 만족시 리턴해주는 역할
                        return x # 자기 자신보다 더 큰 노드가 없을 때, 자기 자신 반환
                else: # t != None # 파고드는 역할
                        return t # 서브트리에서 찾은 최대값
            
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
            else:
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
                return self.sizeOnNode(x.left) + 1 + rankOnNode(x.right, key) # 왼쪽 서브트리 + 자기자신 + 오른쪽 서브트리(오른쪽 서브트리엔 key보다 큰 값이 있을 수 있으므로, rankOnNode(x.right, key) 호출)
            else: # key == x.key
                return self.sizeOnNode(x.left) 
        return rankOnNode(self.root, key)

    def select(self, idx): # 트리에서 idx번째로 작은 원소를 찾음 : 트리를 "오름차순 정렬된 배열"처럼 사용하여, k번째 작은 원소를 찾을 수 있도록 설계
        def selectOnNode(x, idx): # idx-th element on the subtree rooted at x
            if x == None: # 재귀함수의 종료조건
                return None # idx-th element does not exist
            if idx < self.sizeOnNode(x.left): # idx가 현재 노드의 "왼쪽 서브트리 크기보다 작다면" : idx번째 원소는 왼쪽 서브트리 안에 있음 -> 왼쪽으로 이동
                return selectOnNode(x.left, idx)
            elif idx > self.sizeOnNode(x.left): # idx가 현재 노드의 "왼쪽 서브트리 크기보다 크다면" : 왼쪽 서브트리 크기(sizeOnNode(x.left)+1)을 빼고, 오른쪽 서브트리에서 탐색
                return selectOnNode(x.right, idx - self.sizeOnNode(x.left) - 1) # 오른쪽 서브트리 내부에서, idx - 왼쪽 서브트리 - 자기자신을 제외한 크기번째 요소를 찾는거임.
            else: 
                return x.key # idx == self.sizeOnNode(x.left)
        return selectOnNode(self.root, idx)        

    # 재귀호출의 세가지 조건 : 종료조건, 재귀호출, 상태변화
    def inorder(self): # 트리를 중위순회하여 정렬된 리스트 반환        
        def inorderOnNode(x, q):
            if x == None: # 종료조건
                return
            inorderOnNode(x.left, q) # 재귀 호출 : 왼쪽 서브트리, 상태변화 : x.left
            q.append(x.key) # 현재 노드 처리 : 상태변화
            inorderOnNode(x.right, q) # 재귀 호출 : 오른쪽 서브트리, 상태변화 : x.right
        q = []
        inorderOnNode(self.root, q)
        return q

    # 트리에서 노드 삭제시 고려할 세가지 경우
    # 1) 삭제할 노드가 리프 노드 (자식이 없음) -> 그냥 삭제하면 됨
    # 2) 삭제할 노드가 한개의 자식을 가짐 -> 자식 노드와 교체
    # 3) 삭제할 노드가 두개의 자식을 가짐 -> 오른쪽 서브트리의 최소값을 찾아서 대체
    def delete(self, key): # 주어진 key를 삭제
        def minOnNode(x): # 오른쪽 서브트리에서 가장 작은 노드를 찾는 함수 -> 왼쪽으로 쭉쭉쭉 -> 해당 서브트리에서 최소값
            if x == None: 
                return None
            else:            
                while x.left != None:
                    x = x.left
            return x
        def deleteOnNode(x, key): # 삭제 연산 수행, 각 호출마다 부모와 연결할 x를 부르는 것임.
            if x == None: # 트리에 key가 없을 경우
                return None
            if key < x.key: x.left = deleteOnNode(x.left, key) # key가 현재 노드보다 작으면 왼쪽으로 이동. (삭제할 노드를 찾아가는 연산)
            elif key > x.key: x.right = deleteOnNode(x.right, key) # key가 현재 노드보다 크면 오른쪽으로 이동. (삭제할 노드를 찾아가는 연산)
            else: # key가 현재 노드의 값과 일치하면 삭제 수행
                # 삭제할 노드의 자식이 하나인 경우
                if x.right == None: # 삭제할 노드의 한쪽 자식이 None이면, 남은 자식을 부모 노드와 연결하여 대체
                    return x.left
                if x.left == None: #                        "                                  
                    return x.right
                # 삭제할 노드가 자식이 둘 있는 경우
                t = x # t : 삭제할 노드를 임시로 저장
                x = minOnNode(t.right) # x : t를 삭제하고 대체할 노드 (우측 서브트리에서 최소값)
                x.right = deleteOnNode(t.right, x.key) # 오른쪽 서브트리에서 최소값을 찾아 삭제 x와 교체 (t가 삭제된 위치에 해당 최소값이 들어갈텐데 만약 그대로 존재한다면 중복 발생)
                x.left = t.left # 삭제한 노드의 왼쪽 서브트리는 유지하며
            x.count = self.sizeOnNode(x.left) + 1 + self.sizeOnNode(x.right) # 삭제 후 현재 노드의 서브트리 크기(count)를 업데이트
            return x # 부모와의 연결
        self.root = deleteOnNode(self.root, key) # 삭제후 새로운 루트 노드를 반영

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


