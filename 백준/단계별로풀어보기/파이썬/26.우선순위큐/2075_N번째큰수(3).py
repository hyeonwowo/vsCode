import sys
import heapq

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    heap = []
    
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        for element in row:
            if len(heap) < n:
                heapq.heappush(heap,element)
            else:
                minval = heapq.heappop(heap)
                if minval < element:
                    heapq.heappush(heap, element)
                else:
                    heapq.heappush(heap, minval)
                    
    print(heap[0])
                    