import sys
sys.setrecursionlimit(10**6) # 시간초과 발생

def alpabet(cnt, x, y):
    global max
    if cnt > max:
        max = cnt

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] not in load:
                load.append(board[nx][ny])
                alpabet(cnt+1, nx, ny)
                load.pop()
                
if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(n)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    max = 0
    load = [board[0][0]]
    alpabet(1, 0, 0)
    print(max)
