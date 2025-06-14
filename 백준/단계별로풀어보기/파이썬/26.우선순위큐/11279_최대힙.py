import sys
import heapq

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    maxheap = []
    result = []
    for _ in range(n):
        query = int(sys.stdin.readline())
        if query == 0:
            if len(maxheap) == 0:
                result.append(0)
            else:
                result.append((-heapq.heappop(maxheap)))
        else:
            heapq.heappush(maxheap,-query)
            
    for i in range(len(result)):
        print(result[i])