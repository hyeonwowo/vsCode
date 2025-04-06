import sys

def initSquare():
    return [[0] * 10 for _ in range(10)]                                            # 100으로 변경
 
def fillSquare(page,x,y): # x,y 는 사각형 시작점. 사각형의 길이는 10 고정
    weight = x + 1                                                                  # 10으로 변경
    height = y + 1                                                                  # 10으로 변경
    for i in range(x, weight):
        for j in range(y,height):
            if page[i][j] == 1:
                continue
            page[i][j] = 1
    return page

def countSquare(page):
    count = 0
    for i in range(100):
        for j in range(100):
            if page[i][j] == 1:
                count += 1
    return count

def printSquare(page):
    for row in range(len(page)):
        print(page[row])

if __name__ == "__main__":
    page = initSquare()
    n = int(input())
    for _ in range(n):
        x,y = map(int,sys.stdin.readline().split())
        page = fillSquare(page,x,y)
    printSquare(page)
    #print(countSquare(page))