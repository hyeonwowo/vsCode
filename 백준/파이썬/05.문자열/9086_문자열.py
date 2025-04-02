import sys

def STstr(st):
    print(st[0]+st[-1])

def NST(N):
    strList = []
    for _ in range(N):
        st = sys.stdin.readline().strip()
        strList.append(st)

    for element in strList:
        STstr(element)
            
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    NST(N)
    