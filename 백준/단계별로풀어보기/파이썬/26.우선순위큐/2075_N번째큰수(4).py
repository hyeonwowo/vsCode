import sys
import heapq

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    heap = []

    for _ in range(n):
        for num in map(int, sys.stdin.readline().split()):
            heapq.heappush(heap, num)
            if len(heap) > n:
                heapq.heappop(heap)

    print(heap[0])
