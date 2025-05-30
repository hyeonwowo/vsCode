import sys

# 매 층마다 2가지 선택지가 있음(왼쪽 or 오른쪽)
# 매 층마다 선택하므로 N번의 선택 : 2 ** n

def greentower(n):
    return 2 ** n

if __name__ == "__main__":
    print(greentower(int(input())))