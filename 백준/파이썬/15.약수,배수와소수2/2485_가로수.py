import sys

def gcd(a,b):
    while b>0:
        a,b = b, a%b
    return a

def lcm(a,b):
    return (a*b) // gcd(a,b)

def loadTree(n):
    lst = []
    for _ in range(n): # 거리 정보
        lst.append(int(sys.stdin.readline().strip()))
    
    lst_blank = []
    for i in range(1,n): # 간격 정보
        lst_blank.append(lst[i] - lst[i-1])
        
    g = lst_blank[0]
    for element in lst_blank[1:]:
        g = gcd(g,element)
        
    lstb = [i for i in range(lst[0],n,g)]
    return len(lst) - len(lstb)
    
if __name__ == "__main__":
    print(loadTree(int(input())))