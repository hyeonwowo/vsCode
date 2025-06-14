import sys
import heapq

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    minheap = []
    result = []
    for _ in range(n):
        query = int(sys.stdin.readline())
        if query == 0:
            if len(minheap) == 0:
                result.append(0)
            else:
                result.append(heapq.heappop(minheap))
        else:
            heapq.heappush(minheap,query)
    
    print('\n'.join(map(str, result)))