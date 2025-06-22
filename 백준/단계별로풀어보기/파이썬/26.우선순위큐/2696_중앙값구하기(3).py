import sys
import heapq

def findmiddle(n, lst):
    maxheap = []  # 중앙값 이하 (음수로 저장)
    minheap = []  # 중앙값 초과

    result = []

    for i in range(n):
        num = lst[i]

        if not maxheap or num <= -maxheap[0]:
            heapq.heappush(maxheap, -num)
        else:
            heapq.heappush(minheap, num)

        # 균형 조정
        if len(maxheap) > len(minheap) + 1:
            heapq.heappush(minheap, -heapq.heappop(maxheap))
        elif len(minheap) > len(maxheap):
            heapq.heappush(maxheap, -heapq.heappop(minheap))

        # 홀수번째 수일 때만 중앙값 저장
        if i % 2 == 0:
            result.append(-maxheap[0])

    return len(result), result


if __name__ == "__main__":
    input = sys.stdin.readline
    t = int(input())
    result = []

    for _ in range(t):
        n = int(input())
        lst = []
        while len(lst) < n:
            lst.extend(map(int, input().split()))
        result.append(findmiddle(n, lst))

    for cnt, mids in result:
        print(cnt)
        for i in range(cnt):
            print(mids[i], end=' ')
            if (i + 1) % 10 == 0:
                print()
        if cnt % 10 != 0:
            print()
