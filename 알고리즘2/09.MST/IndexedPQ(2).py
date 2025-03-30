class IndexedMinPQ:
    def __init__(self, maxN):
        self.maxN = maxN
        self.n = 0                                     # 현재 PQ에 들어 있는 원소 수
        self.keys = [None for _ in range(maxN)]        # index i 에 해당하는 key 값을 저장하는 배열
        self.pq = []                                   # 최소 힙 역할: (key, index) 튜플 저장
        self.index_pos = {}                            # index → pq에서의 위치 (배열 상 위치 추적용)

    def isEmpty(self):
        return self.n == 0                             # PQ가 비어있는지 확인

    def contains(self, i):
        return i in self.index_pos                     # index i가 현재 PQ에 포함되어 있는지 확인

    def insert(self, i, key):
        if self.contains(i):                           # 이미 존재하는 index라면 에러
            raise Exception(f"Index {i} already in PQ")
        self.keys[i] = key                             # 해당 index에 key 저장
        self.pq.append((key, i))                       # 힙에 (key, index) 추가
        self.index_pos[i] = self.n                     # pq에 추가시, 맨 아래 넣으니까 self.n -> 그 다음 _swim(self.n) 연산을 통해 index_pos[i] = x(위치)를 업데이트 해줌
        self._swim(self.n)                             # 최소 힙 조건을 만족하도록 위로 올림
        self.n += 1                                    # PQ 크기 증가

    # 실행 예시
    # self.keys[2] = 9.5
    # self.pq.append((9.5, 2))         # 현재 self.n == 0 → pq[0]에 저장됨
    # self.index_pos[2] = self.n       # index 2는 pq[0] 위치에 있다!
    # self._swim(0)
    # self.n += 1                      # 다음 삽입은 pq[1]로

    def delMin(self):
        if self.isEmpty(): raise Exception("PQ is empty")
        min_key, min_index = self.pq[0]                # 루트가 최소값
        self._exchange(0, self.n - 1)                  # 마지막 원소와 루트 교환
        self.pq.pop()                                  # 마지막 원소(최소값) 제거
        self.n -= 1
        del self.index_pos[min_index]                  # index → 위치 정보도 제거
        self._sink(0)                                  # 새로운 루트 원소를 아래로 내림
        return min_key, min_index                      # 최소 key와 index 반환

    def decreaseKey(self, i, new_key):
        if not self.contains(i): raise Exception(f"Index {i} not in PQ")
        if new_key > self.keys[i]: raise Exception("New key is greater than current key")
        self.keys[i] = new_key                         # key 값 갱신
        pos = self.index_pos[i]                        # index i가 현재 pq에서 몇 번째 위치인지
        self.pq[pos] = (new_key, i)                    # key 변경 반영
        self._swim(pos)                                # 최소 힙 유지 위해 위로 올림

    # --- 내부 유틸리티 (heap 유지용 메서드들) ---

    def _swim(self, k):
        # 힙 조건을 유지하며 위로 올라감
        while k > 0 and self.pq[(k - 1)//2][0] > self.pq[k][0]: # [key][index]
            self._exchange(k, (k - 1)//2)
            k = (k - 1)//2

    def _sink(self, k):
        # 힙 조건을 유지하며 아래로 내려감
        while 2 * k + 1 < self.n:                  # 왼쪽 자식이 있는 동안 반복
            j = 2 * k + 1                          # 왼쪽 자식 인덱스
            if j + 1 < self.n and self.pq[j + 1][0] < self.pq[j][0]:
                j += 1                             # 오른쪽 자식이 더 작으면 선택
            if self.pq[k][0] <= self.pq[j][0]: # [key][index]
                break                              # 현재 위치가 자식보다 작으면 종료
            self._exchange(k, j)
            k = j

    def _exchange(self, i, j):
        # pq[i]와 pq[j]를 스왑하고, index_pos도 함께 갱신
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.index_pos[self.pq[i][1]] = i # pq[key][index]
        self.index_pos[self.pq[j][1]] = j # pq[key][index]

# 테스트 코드
if __name__ == "__main__":
    pq = IndexedMinPQ(10)
    pq.insert(2, 9.5)             # index 2 에 key 9.5 삽입
    pq.insert(4, 3.2)             # index 4 에 key 3.2 삽입
    pq.insert(1, 6.7)             # index 1 에 key 6.7 삽입

    print(pq.delMin())            # (3.2, 4) 출력 (가장 작은 key를 가진 index 4 제거)
    pq.decreaseKey(2, 2.1)        # index 2의 key를 9.5 → 2.1로 감소시킴
    print(pq.delMin())            # (2.1, 2) 출력
