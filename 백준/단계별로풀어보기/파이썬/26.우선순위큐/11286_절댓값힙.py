import sys
import heapq

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    result = []
    absheap = []
    
    for _ in range(n):
        query = int(sys.stdin.readline())
        if query == 0:
            if len(absheap) == 0:
                result.append(0)
            else:
                temp = heapq.heappop(absheap)
                result.append(temp[1])
        else:
            heapq.heappush(absheap, (abs(query), query))
            
    print('\n'.join(map(str, result)))