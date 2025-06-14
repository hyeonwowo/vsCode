# 우선순위 큐 : 일반적인 큐와 달리 각 요소에 우선순위가 부여되어, 우선순위가 높은 요소가 먼저 나오는 자료구조.
# 특징
# 삽입 (logN) / 삭제 연산 (logN) 이 효율적으로 이루어짐
# Heap 자료구조를 사용하여 구현됨
#   Min-Heap(최소힙) : 값이 작을수록 우선순위가 높음
#   Max-Heap(최대힙) : 값이 클수록 우선순위가 높음


# 파이썬 구현
import heapq

minheap = []
heapq.heappush(minheap, 5)
heapq.heappush(minheap, 3)
heapq.heappush(minheap, 7)

print(heapq.heappop(minheap)) # 3 : 가장 작은 값부터 나옴

maxheap = []
heapq.heappush(maxheap, -5)
heapq.heappush(maxheap, -3)
heapq.heappush(maxheap, -7)
print(-heapq.heappop(maxheap)) # 7 : 가장 큰 값부터 나옴
