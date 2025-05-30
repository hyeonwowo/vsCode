import sys

def findNum(N):
    count = 0
    lst = list(map(int, sys.stdin.readline().split()))
    for element in lst:
        if element == 1: continue
        if element == 2: count += 1
        elif findnumber(element): count += 1
    return count
        
def findnumber(element):
    for i in range(2,element):
        if element % i == 0: return False
    return True
    
if __name__ == "__main__":
    print(findNum(int(input())))