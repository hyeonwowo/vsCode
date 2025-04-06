import sys

def initSquare():
    return [[0] * 100 for _ in range(100)]  # 100x100 배열

def fillSquare(page, x, y):
    for dx in range(10):           # 오른쪽으로 10칸
        for dy in range(10):       # 위쪽으로 10칸
            row = 99 - (y + dy)    # y좌표는 위로 갈수록 작아지므로 99 - y
            col = x + dx
            if 0 <= row < 100 and 0 <= col < 100:
                page[row][col] = 1
    return page

def countSquare(page):
    return sum(cell for row in page for cell in row)

def printSquare(page):
    for row in page:
        print(row)

if __name__ == "__main__":
    page = initSquare()
    n = int(input())
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        page = fillSquare(page, x, y)
    #printSquare(page)
    print(countSquare(page))
