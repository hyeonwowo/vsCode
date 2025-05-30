import sys

def inputdate(n):
    return list(map(int, sys.stdin.readline().split()))

def outputdate(m,resin):
    resout = list(map(int, sys.stdin.readline().split()))
    dupresout = resout
    setresult = set(resin) & set(resout)
    
    for i in range(len(resout)):
        if dupresout[i] in setresult:
            dupresout[i] = 1
        else:
            dupresout[i] = 0
    return ' '.join(list(map(str,dupresout)))

if __name__ == "__main__":
    resin = inputdate(int(input()))
    m = int(input())
    print(outputdate(m,resin))