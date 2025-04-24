import sys
from collections import deque

def Boom(n):
    mydeque = deque()
    lst = list(map(int, sys.stdin.readline().split()))
    for i, element in enumerate(lst):
        mydeque.append((i+1, element))
        
    result = []
    ball, paper = mydeque.popleft()
    result.append(ball)

    while mydeque:
        if paper > 0:
            mydeque.rotate(-(paper - 1))
        else:
            mydeque.rotate(-paper)

        ball, paper = mydeque.popleft()
        result.append(ball)
        
    return ' '.join(map(str, result))

if __name__ == "__main__":
    print(Boom(int(input())))
