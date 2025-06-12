# 1 ~ maxcand 중 최적값을 어떻게 찾을까 ?

import sys

def binary_search():
    pass

def lanline(n, k, lst): # n = 4, k = 11, lst = [802, 742, 457, 539]
    maxcand = sum(lst) // k # maxcand == 231
    candlst = [i for i in range(1,maxcand)]
    return candK(candlst, lst)
    
def candK(candlst,lst):
    remain = []
    for cand in candlst:
        for element in lst:
            result += element // cand
        remain.append(result)
    return remain

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    lst = [int(sys.stdin.readline()) for _ in range(n)] 
    print(lanline(lst))