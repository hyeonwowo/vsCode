import sys # 슬라이싱 제거로 코드 성능 향상
sys.setrecursionlimit(10**6)

numcount = {-1: 0, 0: 0, 1: 0}

def isColor(lst, sr, sc, size):
    base = lst[sr][sc]
    for i in range(sr, sr + size):
        for j in range(sc, sc + size):
            if lst[i][j] != base:
                return False
    return True

def paperCount(lst, sr, sc, size):
    if isColor(lst, sr, sc, size):
        numcount[lst[sr][sc]] += 1
        return
    third = size // 3
    for i in range(3):
        for j in range(3):
            paperCount(lst, sr + i * third, sc + j * third, third)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    paperCount(lst, 0, 0, n)
    print(numcount[-1])
    print(numcount[0])
    print(numcount[1])
