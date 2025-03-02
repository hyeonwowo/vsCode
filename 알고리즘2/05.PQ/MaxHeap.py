class MaxHeap:
    def __init__(self):
        self.pq = ['']  # pq[0]은 사용하지 않음 (힙의 인덱스를 1부터 시작하도록 설정 - 리스트의 첫번째 요소에 공백 문자열을 삽입함으로서 인덱스 [1] 부터 사용)

    def insert(self, key):
        self.pq.append(key) # 힙에 새 원소 추가
        idx = len(self.pq)-1 # 삽입된 원소의 인덱스 : 마지막 인덱스를 얻기 위함 - 0(x) 1(o) 2(0) 새로 추가된 2는 전체 크기 -1

        while idx>1 and self.pq[idx//2] < key: # 부모 노드보다 크면 swap
            self.pq[idx], self.pq[idx//2] = self.pq[idx//2], self.pq[idx]
            idx = idx//2 # 부모 노드 인덱스로 이동

    def delMax(self): # 최대값(root)과 마지막 원소를 swap
        self.pq[1], self.pq[len(self.pq)-1] = self.pq[len(self.pq)-1], self.pq[1] # 최대치와 최소치 스왑 후 -> Pop을 통해 빼내기 (pop은 맨 마지막 인덱스를 빼기때문에 선 swap후 방출)
        max = self.pq.pop() # 최대값 빼내기

        idx = 1 # 루트부터 시작
        while 2*idx <= len(self.pq)-1: # 자식노드가 있을 때
            idxChild = 2*idx # 왼쪽 자식 노드 - 오른쪽 자식 노드가 없을 가능성이 크니까 일단 왼쪽 자식부터 선택

            if idxChild<len(self.pq)-1 and self.pq[idxChild] < self.pq[idxChild+1]: # 오른쪽 자식 노드가 존재하고 더 크면 오른쪽 자식 선택
                idxChild = idxChild+1 # 오른쪽 자식 선택

            if self.pq[idx] >= self.pq[idxChild]: # 부모가 더 크면 종료 (힙 속성 만족)
                break

            self.pq[idx], self.pq[idxChild] = self.pq[idxChild], self.pq[idx] # 부모와 더 큰 자식 노드 교환
            idx = idxChild # 자식 노드로 이동하여 계속 비교
        
        return max # 최대값 반환

    def size(self):
        return len(self.pq) - 1 # pq[0]을 사용하지 않으므로 크기는 -1 보정

    def isEmpty(self):
        return len(self.pq) <= 1 # pq[0]만 남아있으면 빈 힙

if __name__ == "__main__":    
    maxPQ = MaxHeap()
    maxPQ.insert('P')
    print(maxPQ.pq)
    maxPQ.insert('Q')
    print(maxPQ.pq)
    maxPQ.insert('E')
    print(maxPQ.pq)
    maxPQ.insert('X')
    print(maxPQ.pq)
    maxPQ.insert('A')
    print(maxPQ.pq)
    maxPQ.insert('M')
    print(maxPQ.pq)
    maxPQ.insert('P')
    print(maxPQ.pq)
    maxPQ.insert('L')
    print(maxPQ.pq)
    maxPQ.insert('E')
    print(maxPQ.pq)    
    print()
    
    print(maxPQ.delMax())
    print(maxPQ.pq)
    print(maxPQ.delMax())
    print(maxPQ.pq)
    print(maxPQ.delMax())
    print(maxPQ.pq)
    print(maxPQ.delMax())
    print(maxPQ.pq)
    print(maxPQ.delMax())
    print(maxPQ.pq)
    print(maxPQ.delMax())
    print(maxPQ.pq)
    print(maxPQ.delMax())
    print(maxPQ.pq)
    print(maxPQ.delMax())
    print(maxPQ.pq)
    print(maxPQ.delMax())
    print(maxPQ.pq)


    