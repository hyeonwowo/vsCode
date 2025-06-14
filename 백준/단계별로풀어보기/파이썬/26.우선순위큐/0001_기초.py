# 우선순위 큐 구현 (최소힙)
import sys

class PriorityQueue:
    def __init__(self):
        self.heap = [] # 내부 리스트를 사용하여 힙구조 표현
    
    def empty(self):
        return len(self.heap) == 0 # 우선순위 큐가 비어 있는지 확인
    
    def push(self, value): # 맨 끝에 요소를 추가하고, 부모와 위치를 바꿔가며 제자리를 찾아감
        self.heap.append(value) # 새 값을 힙에 추가한 후 위로 올라가며 정렬
        self.heap_up(len(self.heap) - 1) # 추가된 인덱스는 전체길이 - 1 (1-based indexing [] [ㅇ] [ㅇ] [ㅇ] [ㅇ] : 전체길이 5, 마지막 인덱스 4)
    
    def pop(self): # 맨 위에 요소를 반환하고, 자식들 중 하나와 위치를 바꿔가며 제자리를 찾아감. (minheapq -> 더 작은 자식과 교환, Maxheapq -> 더 큰 자식과 교환)
        if self.empty(): # 최소값을 꺼낸 후, 힙 성질을 유지하게끔 아래로 정렬
            return IndexError("empty heapqueue")
        self.swap(0,len(self.heap)-1) # 루트와 마지막 값을 바꾼 뒤, 마지막 값을 제거
        min_val = self.heap.pop()
        self.heap_down(0) # 루트에서부터 아래러 정렬(힙 속성 유지)
        return min_val
    
    def peek(self):
        if self.empty(): # 최소값 조회 (삭제하지 않음)
            raise IndexError("empty heapqueue")
        return self.heap[0]
    
    def heap_up(self,index): # 자식 노드가 부모보다 작으면 교환하며 위로 올라감. push 연산과 관련. index는 기준이 되는 인덱스
        parent = (index - 1) // 2 # Inde는 현재 인덱스이자 기준이 되는 인덱스
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.swap(index, parent)
            self.heap_up(parent) # 재귀 호출로 계속 위로 올라감
    
    def heap_down(self, index):
        smallest = index # 부모 노드가 자식 노드보다 크면 아래로 내려가며 교환. pop 연산과 관련. index는 기준이 되는 인덱스
        left = index * 2 + 1
        right = index * 2 + 2
        size = len(self.heap)
        
        if left < size and self.heap[left] < self.heap[smallest]: # 왼쪽 자식과 비교
            smallest = left
        if right < size and self.heap[right] < self.heap[smallest]: # 오른쪽 자식과 비교
            smallest = right
            
        if smallest != index: # 현재 노드가 가장 작지 않다면 자식 중 더 작은 쪽과 교환
            self.swap(index, smallest)
            self.heap_down(smallest) # 재귀 호출로 계속 아래로
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i] # i와 j위치의 요소를 교환
    
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push(5)
    pq.push(2)
    pq.push(8)
    
    while not pq.empty():
        print(pq.pop()) # 1, 2, 5, 8 순으로 출력