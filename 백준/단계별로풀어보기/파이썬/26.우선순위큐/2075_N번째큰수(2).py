import sys
import heapq  # 최소힙 사용

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    heap = []

    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        for num in row:
            if len(heap) < n:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)

    print(heap[0])  # n번째 큰 수
