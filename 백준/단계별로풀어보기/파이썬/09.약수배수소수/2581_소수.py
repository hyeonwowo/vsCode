import sys

def MinSum(n,m):
    lst = []
    for i in range(n,m+1):
        if i == 1: continue
        elif findnum(i): lst.append(i)
        
    if len(lst) == 0: print("-1")
    else:
        print(sum(lst))
        print(min(lst))

def findnum(element):
    for i in range(2,element):
        if element % i == 0: return False
    return True
    
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    MinSum(n,m)