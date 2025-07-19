import sys
sys.setrecursionlimit(10000) # 비트마스킹 방식

def dfs(x, y, bitmask, cnt):
    global answer
    answer = max(answer, cnt)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            ch = board[nx][ny]
            ch_bit = 1 << (ord(ch) - 65)
            if not (bitmask & ch_bit):
                dfs(nx, ny, bitmask | ch_bit, cnt + 1)

if __name__ == "__main__":
    R, C = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(R)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    start_ch = board[0][0]
    start_bitmask = 1 << (ord(start_ch) - 65)

    answer = 0
    dfs(0, 0, start_bitmask, 1)
    print(answer)
