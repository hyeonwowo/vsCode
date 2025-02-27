class UnorderedMinPq:
    def __init__(self):
        self.pq=[]
    def print(self):
        print(self.pq)
    def insert(self,key):
        self.pq.append(key)
    def delMin(self):
        min, minidx = self.pq[0], 0
        for index, value in enumerate(self.pq):
            if min > value:
                min, minidx = value, index
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