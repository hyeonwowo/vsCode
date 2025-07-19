import sys

def rotto(start, lst):
    if len(lst) == 6:
        print(*path)
        return
    else:
        for i in range(start, len(lst)):
            path.append(lst[i])
            rotto(i, lst)
            path.pop()

if __name__ == "__main__":
    query = []
    
    while True:
        lstt = list(map(int, sys.stdin.readline().split()))
        if lstt[0] == 0:
            break
        query.append(lstt)
    
    path = []
    for element in query:
        rotto(0, element)