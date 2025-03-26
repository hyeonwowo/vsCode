import heapq
from collections import deque

# --- 1. list ---
def list_operations():
    print("\n--- list ---")
    arr = [1, 2, 3]           # 리스트 생성
    arr.append(4)             # 맨 뒤에 요소 추가 → [1, 2, 3, 4]
    arr.insert(1, 10)         # 인덱스 1에 10 삽입 → [1, 10, 2, 3, 4]
    arr.pop()                 # 마지막 요소 제거 → [1, 10, 2, 3]
    arr.pop(1)                # 인덱스 1 (첫번째) 요소 제거 (10) → [1, 2, 3]
    arr.remove(3)             # 값이 3인 요소 제거 → [1, 2]
    arr[0] = 99               # 인덱스 0의 값 변경 → [99, 2]
    print("list result:", arr)

# --- 2. heapq (min-heap) ---
def heapq_operations():
    print("\n--- heapq ---")
    heap = []
    heapq.heappush(heap, 3)   # 요소 삽입
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 5)
    print("heap before pop:", heap)  # 내부적으로 정렬된 최소 힙
    print("heappop:", heapq.heappop(heap))  # 가장 작은 값 꺼냄
    print("heap after pop:", heap)

    arr = [7, 2, 6]
    heapq.heapify(arr)        # 일반 리스트를 힙으로 변환
    print("heapify result:", arr)

# --- 3. deque (양방향 큐) ---
def deque_operations():
    print("\n--- deque ---")
    dq = deque()
    dq.append(1)              # 오른쪽에 삽입
    dq.appendleft(2)          # 왼쪽에 삽입
    dq.pop()                  # 오른쪽에서 제거
    dq.popleft()              # 왼쪽에서 제거
    print("deque result:", dq)

# --- 4. set (중복 제거 집합) ---
def set_operations():
    print("\n--- set ---")
    s = set()
    s.add(1)                  # 요소 추가
    s.add(2)
    s.discard(1)              # 요소 제거 (없어도 에러 X)
    s.discard(999)            # 없는 요소 제거 시도해도 안전
    print("set result:", s)

# --- 5. dict (key-value 쌍) ---
def dict_operations():
    print("\n--- dict ---")
    d = {'a': 1}              # 딕셔너리 생성
    d['b'] = 2                # 새로운 키 추가
    d['a'] = 100              # 기존 키의 값 수정
    d.pop('b')                # 키 'b' 제거
    print("dict result:", d)

# --- 6. Indexed Min Priority Queue ---
# 특정 key의 우선순위를 직접 변경할 수 있는 구조
class IndexedMinPQ:
    def __init__(self):
        self.heap = []                     # heap: (priority, key)
        self.entry_finder = {}             # key -> [priority, key]
        self.REMOVED = "<REMOVED>"         # 삭제된 항목 표시

    def insert(self, key, priority):
        if key in self.entry_finder:
            self.remove(key)               # 기존 항목 삭제 표시
        entry = [priority, key]
        self.entry_finder[key] = entry
        heapq.heappush(self.heap, entry)

    def remove(self, key):
        entry = self.entry_finder.pop(key)
        entry[-1] = self.REMOVED           # key 대신 REMOVED로 마킹

    def pop(self):
        while self.heap:
            priority, key = heapq.heappop(self.heap)
            if key != self.REMOVED:
                del self.entry_finder[key]
                return key, priority
        raise KeyError("pop from empty priority queue")

    def change_priority(self, key, new_priority):
        self.insert(key, new_priority)     # 우선순위 변경 = 삭제 + 삽입

    def contains(self, key):
        return key in self.entry_finder

    def is_empty(self):
        return not self.entry_finder

# IndexedMinPQ 사용 예제
def indexed_pq_operations():
    print("\n--- IndexedMinPQ ---")
    ipq = IndexedMinPQ()
    ipq.insert("A", 5)
    ipq.insert("B", 3)
    ipq.insert("C", 7)
    ipq.change_priority("C", 1)  # C의 우선순위 낮춤
    while not ipq.is_empty():
        print("popped:", ipq.pop())  # 우선순위 작은 순서대로 pop

# --- 전체 실행 ---
if __name__ == "__main__":
    list_operations()
    heapq_operations()
    deque_operations()
    set_operations()
    dict_operations()
    indexed_pq_operations()
