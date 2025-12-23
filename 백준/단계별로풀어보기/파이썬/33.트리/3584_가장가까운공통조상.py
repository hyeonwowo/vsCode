import sys

def findroot(q1, q2):
    lst1 = lst2 = []
    lst1.append(q1)
    lst2.append(q2)
    
    flag1 = flag2 = 0
    while True:
        cur1, cur2 = idx[q1], idx[q2]
        lst1.append(cur1)
        lst2.append(cur2)
        cur1, cur2 = idx[cur1], idx[cur2]
        
        if cur1 == idx[cur1]:
            flag1 = 1
        elif cur2 == idx[cur2]:
            flag2 = 1
        elif flag1 + flag2 == 2:
            return lst1, lst2
        
if __name__ == "__main__":
    T = int(sys.stdin.readline())
    res = []
    for _ in range(T):
        N = int(sys.stdin.readline())
        idx = [i for i in range(N)]
        for _ in range(N):
            p, c = map(int, sys.stdin.readline().split())
            idx[c] = p
            q1, q2 = map(int, sys.stdin.readline().split())
            lst1, lst2 = findroot(q1, q2)
            st = list(set(lst1) & set(lst2))
            
            
            
            
            res.append()
    
    print(res)   
            
        