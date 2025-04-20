import sys

def main(n):
    lst = []
    for _ in range(n):
        lst.append(int(sys.stdin.readline().strip()))
    resultlst = []
    for element in lst:
        resultlst.append(numnum(element))
    return '\n'.join(map(str,resultlst))
        
def findnum(k):
    for i in range(2,k):
        if k % i == 0:
            return False
    return True

def numnum(i):
    if findnum(i): return i
    elif not findnum(i): return numnum(i+1)
            
if __name__ == "__main__":
    print(main(int(input())))