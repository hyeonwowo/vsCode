# heapq에 여러가지 요소 저장 : 각 heapq 인덱스 데이터 삽입시, 수 제한 없음 (a,b), (c,d), (e,f) ...
# heapq 인덱스 비교는 각 튜플의 첫번째 요소로 정렬됨

import heapq

heap = []
heapq.heappush(heap, (3,'a'))
heapq.heappush(heap, (1,'b'))
heapq.heappush(heap, (3,'c'))

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))

# 비교 순서:
# 첫 번째 요소(3, 1, 3)를 먼저 비교
# 같으면 두 번째 요소 'a', 'c' 등을 비교

# 출력 순서:
# (1, 'b')
# (3, 'a')
# (3, 'c')
