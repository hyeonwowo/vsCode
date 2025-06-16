import sys
import heapq

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        M = int(input())
        numbers = []
        while len(numbers) < M:
            numbers.extend(map(int, input().split()))
        
        max_heap = []  # 왼쪽 (중앙값 이하), 최대 힙 -> -값 사용
        min_heap = []  # 오른쪽 (중앙값 초과), 최소 힙
        result = []

        for i in range(M):
            num = numbers[i]
            
            if len(max_heap) == len(min_heap):
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)

            # 힙 간 균형 조정 (max_heap의 최대값이 min_heap의 최소값보다 커야 함)
            if min_heap and -max_heap[0] > min_heap[0]:
                maxval = -heapq.heappop(max_heap)
                minval = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -minval)
                heapq.heappush(min_heap, maxval)

            # 홀수 번째 수마다 중앙값 기록
            if i % 2 == 0:
                result.append(-max_heap[0])

        # 출력
        print(len(result))
        for i in range(0, len(result), 10):
            print(' '.join(map(str, result[i:i+10])))

if __name__ == "__main__":
    solve()
