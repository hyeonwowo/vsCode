import sys

class PriorityQueue:
    def __init__(self):
        self.heap = [None]  # 1-based index
    
    def empty(self):
        return len(self.heap) == 1
 
    def push(self, value):
        self.heap.append(value)
        self.heap_up(len(self.heap) - 1)  # 수정

    def pop(self):
        if self.empty():
            return "empty heapqueue"
        self.swap(1, len(self.heap) - 1)  # 수정
        minval = self.heap.pop()
        self.heap_down(1)
        return minval
        
    def peek(self):
        if self.empty():
            return "empty heapqueue"
        return self.heap[1]
    
    def heap_up(self, index):
        parent = index // 2
        if index > 1 and self.heap[index] < self.heap[parent]:  # index > 1 로 조건 변경
            self.swap(index, parent)
            self.heap_up(parent)
    
    def heap_down(self, index):
        smallest = index
        left = index * 2
        right = index * 2 + 1
        size = len(self.heap)
        
        if left < size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < size and self.heap[right] < self.heap[smallest]:
            smallest = right
            
        if smallest != index:
            self.swap(smallest, index)
            self.heap_down(smallest)  # 수정
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push(5)
    pq.push(2)
    pq.push(8)

    while not pq.empty():
        print(pq.pop())
