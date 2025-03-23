class IndexedMinPQ:
    def __init__(self, maxN):
        self.maxN = maxN
        self.n = 0
        self.keys = [None] * maxN        # index i에 대한 key 값
        self.pq = []                     # heap: (key, index)
        self.index_pos = {}             # index → pq 내 위치

    def isEmpty(self):
        return self.n == 0

    def contains(self, i):
        return i in self.index_pos

    def insert(self, i, key):
        if self.contains(i):
            raise Exception(f"Index {i} already in PQ")
        self.keys[i] = key
        self.pq.append((key, i))
        self.index_pos[i] = self.n
        self._swim(self.n)
        self.n += 1

    def delMin(self):
        if self.isEmpty(): raise Exception("PQ is empty")
        min_key, min_index = self.pq[0]
        self._exchange(0, self.n - 1)
        self.pq.pop()
        self.n -= 1
        del self.index_pos[min_index]
        self._sink(0)
        return min_key, min_index

    def decreaseKey(self, i, new_key):
        if not self.contains(i): raise Exception(f"Index {i} not in PQ")
        if new_key > self.keys[i]: raise Exception("New key is greater than current key")
        self.keys[i] = new_key
        pos = self.index_pos[i]
        self.pq[pos] = (new_key, i)
        self._swim(pos)

    # --- 내부 유틸리티 (heap 유지용) ---
    def _swim(self, k):
        while k > 0 and self.pq[(k - 1)//2][0] > self.pq[k][0]:
            self._exchange(k, (k - 1)//2)
            k = (k - 1)//2

    def _sink(self, k):
        while 2 * k + 1 < self.n:
            j = 2 * k + 1
            if j + 1 < self.n and self.pq[j + 1][0] < self.pq[j][0]:
                j += 1
            if self.pq[k][0] <= self.pq[j][0]:
                break
            self._exchange(k, j)
            k = j

    def _exchange(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.index_pos[self.pq[i][1]] = i
        self.index_pos[self.pq[j][1]] = j

if __name__ == "__main__":
    pq = IndexedMinPQ(10)
    pq.insert(2, 9.5)
    pq.insert(4, 3.2)
    pq.insert(1, 6.7)

    print(pq.delMin())       # (3.2, 4)
    pq.decreaseKey(2, 2.1)   # 2의 우선순위 변경
    print(pq.delMin())       # (2.1, 2)
