import sys

def findCount(lst):
    resultList = []
    Chess = {
        "King":1,
        "Queen":1,
        "Rook":2,
        "Bishop":2,
        "Knight":2,
        "Phone":8
    }
    resultList.append(Chess["King"] - lst[0])
    resultList.append(Chess["Queen"] - lst[1])
    resultList.append(Chess["Rook"] - lst[2])
    resultList.append(Chess["Bishop"] - lst[3])
    resultList.append(Chess["Knight"] - lst[4])
    resultList.append(Chess["Phone"] - lst[5])
    return resultList

if __name__ == "__main__":
    lst = list(map(int, sys.stdin.readline().split()))
    print(*findCount(lst))