from queue import PriorityQueue

# 우선순위 큐 생성
pq = PriorityQueue()
pq = PriorityQueue(maxsize = 3) # maxsize 저장가능한 수 제한

# put() : 요소 추가 (자동 정렬됨, 작은 값이 우선)
pq.put(5)
pq.put(1)
pq.put(3)

# qsize() : 큐 크기 확인
print("큐 크기:", pq.qsize())  # 출력: 큐 크기: 3

# get() : "가장 작은" 값부터 꺼내기
print("꺼낸 값:", pq.get())  # 출력: 1
print("꺼낸 값:", pq.get())  # 출력: 3
print("꺼낸 값:", pq.get())  # 출력: 5

# empty() : 큐가 비어 있으면 True, 그렇지 않으면 False
print(pq.empty())

# full() : 큐가 가득 차 있으면 True, 그렇지 않으면 False
print(pq.full())


