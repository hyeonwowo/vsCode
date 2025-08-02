import sys
sys.setrecursionlimit(10**6)

def solution(start, end):
    if start >= end:
        return

    mid = arr[start]
    idx = start + 1

    # 오른쪽 서브트리의 시작점을 찾음 (처음으로 mid보다 큰 값)
    while idx < end and arr[idx] < mid:
        idx += 1

    solution(start + 1, idx)  # 왼쪽 서브트리
    solution(idx, end)        # 오른쪽 서브트리
    print(mid)

if __name__ == "__main__":
    arr = []
    while True:
        try:
            x = int(sys.stdin.readline())
            arr.append(x)
        except:
            break

    solution(0, len(arr))
