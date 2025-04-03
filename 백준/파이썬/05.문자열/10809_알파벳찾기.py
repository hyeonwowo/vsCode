import sys

def findChar(st):
    stList = [-1] * (ord('z') - ord('a') + 1)
    for i in range(len(st)):
        asch = ord(st[i]) - 97
        if stList[asch] == -1:
            stList[asch] = i
    return stList
        

if __name__ == "__main__":
    st = sys.stdin.readline().strip()
    print(*findChar(st))