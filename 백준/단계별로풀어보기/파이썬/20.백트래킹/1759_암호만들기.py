import sys

def isok(word):
    aeiou = 0
    remain  = 0
    
    for ch in word:
        if ch in lst: aeiou += 1
        else: remain += 1

        if aeiou >= 1 and remain >= 2:
            return True
    return False

def password(start):
    if len(word) == L:
        res = isok(word)
        if res:
            print(*word, sep='')
            return
        else:
            return
    else:
        for i in range(start, C):
            word.append(st[i])
            password(i+1)
            word.pop()

if __name__ == "__main__":
    L, C = map(int, sys.stdin.readline().split())
    st = sorted(list(map(str, sys.stdin.readline().split())))
    
    lst = ['a','e','i','o','u']
    
    
    word = []
    password(0)