import sys

n, m, k = map(int, sys.stdin.readline().split())
board = [[0] + list(sys.stdin.readline().strip()) for _ in range(m)]
board.insert(0,[0]*(m+1))
for row in board:
    print(*row)