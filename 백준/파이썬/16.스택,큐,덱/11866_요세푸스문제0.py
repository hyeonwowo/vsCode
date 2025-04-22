import sys
from collections import deque

def youspuss(n,k):
    myqueue = deque()
    for i in range(1,n+1):
        myqueue.append(i)
    result = []
    while len(myqueue) > 1:
        for _ in range(k-1):
            myqueue.append(myqueue.popleft())
        result.append(myqueue.popleft())
        
    result.append(myqueue.pop())
    return ("<" + ", ".join(map(str, result)) + ">")


if __name__ == "__main__":
    print(youspuss(*map(int,sys.stdin.readline().split())))