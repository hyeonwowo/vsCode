import sys
sys.setrecursionlimit(10**6)

def alpabet(cnt, x, y):
    global max
    if cnt > max:
        max = cnt

    for dx, dy in directions:
        if 0 <= dx < n and 0 <= dy < m:
            if board[dx][dy] not in load:
                load.append(board[x][y])
                alpabet(cnt+1, x, y)
                load.pop()
            else:
                return
        
if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    board = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    max = 0
    load = []
    alpabet(1, 0, 0)
    print(max)
    