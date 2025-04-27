import sys

def draw_star(arr, r, c, size):
    if size == 1:
        return
    unit = size // 3
    for i in range(r + unit, r + 2 * unit):
        for j in range(c + unit, c + 2 * unit):
            arr[i][j] = ' '
    for dr in range(0, size, unit):
        for dc in range(0, size, unit):
            if dr == unit and dc == unit:
                continue
            draw_star(arr, r + dr, c + dc, unit)

def main():
    n = int(sys.stdin.readline())
    arr = [['*' for _ in range(n)] for _ in range(n)]
    draw_star(arr, 0, 0, n)
    for line in arr:
        print(''.join(line))

if __name__ == "__main__":
    main()
