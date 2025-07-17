import sys

def partSum(s, lst):
    left = 0
    right = 0
    mincount = float('inf')
    total = 0
    
# total < s인 상황에서 right가 이미 끝까지 간 경우,
# lst[right]가 존재하지 않기 때문에 런타임 오류 발생

    while True: # if, elif, else 순서 중요함
        if total >= s: # > -> >=
            mincount = min(mincount, right - left)
            total -= lst[left]
            left += 1
            # mincount -> 상단으로 자리 변경
        elif right == N: # N-1 -> N
            break
        else:
            total += lst[right]
            right += 1
            
    if mincount >= float('inf'):
        return 0
    else:
        return mincount

if __name__ == "__main__":
    N, S = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    print(partSum(S, lst))