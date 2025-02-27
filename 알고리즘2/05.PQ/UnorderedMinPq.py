class UnorderedMinPq:
    def __init__(self):
        self.pq=[]
    def print(self):
        print(self.pq)
    def insert(self,key):
        self.pq.append(key)
    def delMin(self):
        min = self.pq[0]
        minidx = 0
        for i in range(len(self.pq)):
            if min > self.pq[i]:
                min = self.pq[i]
                minidx = i
        return self.pq.pop(minidx)
    

if __name__=="__main__":
    pq = UnorderedMinPq()
    pq.insert(5)
    pq.print()
    pq.insert(3)
    pq.print()
    pq.insert(4)
    pq.print()
    pq.insert(1)
    pq.print()
    pq.insert(2)
    pq.print()
    print()

    print(pq.delMin())
    pq.print()
    print()

    print(pq.delMin())
    pq.print()
    print()

    print(pq.delMin())
    pq.print()
    print()

    print(pq.delMin())
    pq.print()
    print()

    print(pq.delMin())
    pq.print()