# sys.stdin.readline() 입력을 통해 런타임에러 오류 해결
import sys

def bucket(N, M):
    arr = [0 for _ in range(N)]
    for _ in range(M):
        x, y, z = map(int, sys.stdin.readline().split())
        x -= 1
        arr[x:y] = [z] * (y - x)
    return arr

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    result = bucket(N, M)
    print(*result)
