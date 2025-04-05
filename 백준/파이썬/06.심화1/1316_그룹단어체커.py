import sys

def groupWord(N):
    count = 0
    for _ in range(N):    
        dictWord = {}
        st = sys.stdin.readline().strip()
        
        for i, ch in enumerate(st):
            if ch not in dictWord:
                dictWord[ch] = [i]
            elif ch in dictWord:
                dictWord[ch].append(i)
        
        if isGroupWord(dictWord):
            count += 1
    return count

def isGroupWord(dictWord):
    for element in dictWord.values():
        if len(element) >= 2:
            for i in range(1,len(element)):
                if element[i] - element[i-1] != 1:
                    return False
    return True

if __name__ == "__main__":
    N = int(input())
    print(groupWord(N))