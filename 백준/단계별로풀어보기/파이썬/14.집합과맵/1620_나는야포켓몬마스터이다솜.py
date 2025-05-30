import sys

def pocketmon(n, m):
    numtoname = {}
    nametonum = {}
    
    for i in range(1,n+1):
        name = sys.stdin.readline().strip()
        numtoname[i] = name
        nametonum[name] = i
    
    result = []
    for _ in range(m):
        query = sys.stdin.readline().strip()
        if query.isdigit():
            result.append(numtoname[int(query)])
        elif query.isalpha():
            result.append(nametonum[query])
    return '\n'.join(map(str,result))

if __name__ == "__main__":
    print(pocketmon(*map(int, sys.stdin.readline().split())))
