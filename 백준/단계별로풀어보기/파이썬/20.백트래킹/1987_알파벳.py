import sys
sys.setrecursionlimit(10**6)

def alpabet(cnt, x, y):
    global max
    if cnt > max:
        max = cnt

    for dx, dy in directions:
        if 0 <= x+dx < n and 0 <= y+dy < m:
            if board[x+dx][y+dy] not in load:
                load.append(board[x+dx][y+dy])
                alpabet(cnt+1, x+dx, y+dy)
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
    