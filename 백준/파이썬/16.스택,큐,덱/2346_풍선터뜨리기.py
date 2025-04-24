import sys
from collections import deque

def Boom(n):
    mydeque = deque()
    lst = list(map(int, sys.stdin.readline().split()))
    for i, element in enumerate(lst):
        mydeque.append((i,element))
        
    result = []
    ball, paper = mydeque.popleft()
    result.append(ball)
    while len(result) < len(lst):
        for _ in range(paper):
            mydeque.append(mydeque.popleft())
        ball,paper = mydeque.popleft()
        result.append(ball)
    return ' '.join(map(str, result))
        
if __name__ == "__main__":
    print(Boom(int(input())))