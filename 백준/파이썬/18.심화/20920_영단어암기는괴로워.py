import sys

def engword(n, m):
    wordlst = []
    for _ in range(n):
        word = sys.stdin.readline().strip()
        if len(word) >= m:
            wordlst.append(word)
    
    dictword = {}
    for word in wordlst:
        dictword[word] = dictword.get(word, 0) + 1
    
    sortword = sorted(dictword.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    
    return '\n'.join(word for word, _ in sortword)

if __name__ == "__main__":
    print(engword(*map(int, sys.stdin.readline().split())))
