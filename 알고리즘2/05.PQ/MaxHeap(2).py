class MaxHeap:
    def __init__(self):
        self.pq = ['']
    def insert(self,key):
        self.pq.append(key)
        idx = len(self.pq) - 1
        
        while idx>1 and self.pq[idx//2] < key:
            self.pq[idx],self


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


    