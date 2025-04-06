import sys

def makeArr(n):
    return [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def findMax(arr):
    max_val = -1
    max_pos = (0, 0)
    
    for i, row in enumerate(arr):
        for j, val in enumerate(row):
            if val > max_val:
                max_val = val
                max_pos = (i + 1, j + 1)  # 1-based index
    
    print(f"{max_val}\n{max_pos[0]} {max_pos[1]}")

if __name__ == "__main__":
    N = 9
    arr = makeArr(N)
    findMax(arr)
