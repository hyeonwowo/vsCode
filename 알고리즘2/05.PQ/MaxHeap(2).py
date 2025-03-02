class MaxHeap:
    def __init__(self):
        self.pq = ['']

    def insert(self, key):
        self.pq.append(key)
        idx = len(self.pq)-1

        while idx > 1 and self.pq[idx//2] < key:
            self.pq[idx], self.pq[idx//2] =  self.pq[idx//2],self.pq[idx]
            idx = idx//2

    def delMax(self):
        idx = len(self.pq)-1
        self.pq[1],self.pq[idx] = self.pq[1],self.pq[idx]
        max = self.pq.pop()

        idx = 1
        while idx*2 <= len(self.pq)-1:
            if self.pq[idx*2] < self.pq[idx*2+1]:
                self.pq[idx*2],self.pq[idx] = self.pq[idx],self.pq[idx*2]
                idx = idx*2
            else:
                self.pq[idx*2+1],self.pq[idx] = self.pq[idx],self.pq[idx*2+1]
                idx = idx*2+1
            
            if self.pq[idx//2] > self.pq[idx]:
                break
        return max


    def size(self):
        return len(self.pq)-1
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


    