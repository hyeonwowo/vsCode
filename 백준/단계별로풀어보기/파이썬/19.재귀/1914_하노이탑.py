import sys

def hanoi(n, start, end, temp, result):
    if n == 1:
        result.append((start, end))
    else:
        hanoi(n-1, start, temp, end, result)
        result.append((start, end))
        hanoi(n-1, temp, end, start, result)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    result = []
    hanoi(n, 1, 3, 2, result)
    print(len(result))
    for move in result:
        print(*move)
