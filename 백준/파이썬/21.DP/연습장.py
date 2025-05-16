import sys

def triangle(n):
    if board[n] != -1:
        return board[n]
    board[n] = triangle(n-3) + triangle(n-2)
    return board[n]

if __name__ == "__main__":
    board = [-1 for _ in range(101)]
    board[1], board[2], board[3] = 1, 1, 1
    
    n = int(sys.stdin.readline())
    result = []
    for _ in range(n):
        k = int(sys.stdin.readline())
        result.append(triangle(k))
    print('\n'.join(map(str, result)))