import sys
import heapq

def max_steal_value(N, K, jewels, bags):
    jewels.sort()
    bags.sort() 

    result = 0
    heap = []
    jewel_index = 0

    for bag in bags:
        while jewel_index < N and jewels[jewel_index][0] <= bag: # 가방이 오름차순 정렬 -> 가방마다 보석을 순회할 필요 없음 -> 마지막 가방 보석인덱스부터 순회하면 됨 : while을 사용하는 이윤
            heapq.heappush(heap, -jewels[jewel_index][1])  
            jewel_index += 1
        
        if heap:
            result += -heapq.heappop(heap)

    return result

if __name__ == "__main__":
    input = sys.stdin.readline
    N, K = map(int, input().split())
    jewels = [tuple(map(int, input().split())) for _ in range(N)]
    bags = [int(input()) for _ in range(K)]

    print(max_steal_value(N, K, jewels, bags))
