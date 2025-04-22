import sys
from collections import deque

def card(n):
    myCard = deque()
    for i in range(1,n+1):
        myCard.append(i)
        
    while len(myCard) > 1:
        myCard.popleft()
        myCard.append(myCard.popleft())
    return myCard.pop()

if __name__ == "__main__":
    print(card(int(input())))