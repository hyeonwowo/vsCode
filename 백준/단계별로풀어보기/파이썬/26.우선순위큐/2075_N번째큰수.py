import sys # 모든 수를 하나하나 다 넣고, n번 pop 수행 -> 메모리 초과
import heapq

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    heap = []
    for row in lst:
        for element in row:
            heapq.heappush(heap, -element)
            
    for _ in range(n-1):
        heapq.heappop(heap)
    print(-heapq.heappop(heap))