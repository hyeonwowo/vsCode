class MaxHeap:
    def __init__(self):
        self.pq = ['']

    def insert(self, key):
        self.pq.append(key)
        idx = len(self.pq) - 1

        while idx > 1 and self.pq[idx // 2] < key:
            self.pq[idx], self.pq[idx // 2] = self.pq[idx // 2], self.pq[idx]
            idx = idx // 2

    def delMax(self):
        if len(self.pq) <= 1:
            raise IndexError("Heap is empty")

        self.pq[1], self.pq[-1] = self.pq[-1], self.pq[1]
        max_val = self.pq.pop()

        idx = 1
        while 2 * idx < len(self.pq):
            left = 2 * idx
            right = 2 * idx + 1

            if right < len(self.pq) and self.pq[right] > self.pq[left]:
                larger_child = right
            else:
                larger_child = left

            if self.pq[idx] >= self.pq[larger_child]:
                break

            self.pq[idx], self.pq[larger_child] = self.pq[larger_child], self.pq[idx]
            idx = larger_child

        return max_val

    def size(self):
        return len(self.pq) - 1

    def isEmpty(self):
        return len(self.pq) <= 1


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
