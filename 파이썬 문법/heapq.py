# heapq : 힙(heap) 자료구조를 제공하며, 우선순위 큐를 효율적으로 구현 가능
# 힙(heap) : 완전 이진 트리 기반의 자료구조이며, 파이썬의 heapq는 최소힙을 기본적으로 제공

# heapq
# 1) 최소 힙(min-heap) 기본 제공 → 가장 작은 값이 먼저 나옴.
# 2) 리스트 기반으로 동작 → list와 함께 사용.
# 3) O(log N) 시간 복잡도 → 삽입, 삭제 연산이 빠름.
# 4) 최대 힙(max-heap)도 구현 가능 (음수 변환 기법 활용).

import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)

print(heap)  # [1, 2, 5, 3] (내부적으로 정렬됨)

print(heapq.heappop(heap))  # 1 (최소값 제거)
print(heapq.heappop(heap))  # 2
print(heapq.heappop(heap))  # 3
