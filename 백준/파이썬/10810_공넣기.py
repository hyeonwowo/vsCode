# 이와 같은 방법은 런타임에러 발생 (input)
def bucket(N,M):
    arr = [0 for i in range(N)] # 바구니 생성
    for i in range(M): # 반복 횟수
        x, y, z = map(int, input("").split())
        x = x-1
        arr[x:y] = [z] * (y-x)
    return arr
    
print(bucket(5, 4))

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
