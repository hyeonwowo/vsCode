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


# 1 - based 구현을 위한 [] 초기화
heap = [None] # 어떤 자료형과도 비교가 가능하기에 오류 발생 적음
heap = [0] # 숫자와 비교 가능하지만 주의
heap = [-1] # 숫자와 비교 가능하지만 주의
heap = [-float('inf')] # 숫자 비교 초기화 방법 중 가장 안정적
heap = [""] # 문자열 초기화이기 때문에 만약, 숫자형과 비교시 오류 발생 확률 큼


# len(self.heap) - 1 : 0-based, 1-based 인덱스에서 마지막 요소의 인덱스를 구하는 "공통적인" 공식

based0 = [10,20,30] # 마지막 요소 인덱스 : len(lst) - 1 = 3 - 1 = 2
based1 = [None,10,20,30] # 마지막 요소 인덱스 : len(lst) - 1 = 4 - 1 = 3

    # 리스트 맨 끝에 접근하려면 언제나 -1이 필요함, 인덱스 방식(0-based, 1-based)과는 무관.
    # len(lst) - 1 : 마지막 인덱스 접근 공식