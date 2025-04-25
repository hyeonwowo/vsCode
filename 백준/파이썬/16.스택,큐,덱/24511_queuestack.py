import sys
from collections import deque

class Stack:
    def __init__(self):
        self.stack = []
    def empty(self):
        if self.stack: return 0
        return 1
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        if self.empty(): return None
        return self.stack[-1]

class Queue:
    def __init__(self):
        self.queue = deque()
    def empty(self):
        if self.queue: return 0
        return 1
    def enqueue(self,x):
        self.queue.append(x)
    def dequeue(self):
        if self.empty(): return None
        return self.queue.popleft()

def insertdata():
    N = int(input())
    DS = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    M = int(input())
    C = list(map(int, sys.stdin.readline().split()))
    return N,DS,B,M,C

def main(N,DS,B,M,C):
    for i in range(1,N+1):
        if DS[i] == 0:
            mystack[i] = Stack()
            mystack.append(B[i-1])
        else:
            myqueue[i] = Queue()
            myqueue.append(B[i-1])

if __name__ == "__main__":
    print(main(insertdata()))