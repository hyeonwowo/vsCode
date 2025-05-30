import sys

def shotPoint(n):
    lst = list(map(int, sys.stdin.readline().split()))
    sortlst = sorted(lst)
    count = 0
    worddict = {}
    for ch in sortlst:
        if ch not in worddict:
            worddict[ch] = count
            count += 1
    for element in lst:
        print(worddict[element],end=' ')


if __name__ == "__main__":
    shotPoint(int(input()))