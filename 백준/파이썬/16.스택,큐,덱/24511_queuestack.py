import sys
from collections import deque

input = sys.stdin.readline

class Stack:
    def __init__(self, val):
        self.stack = [val]
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop()

class Queue:
    def __init__(self, val):
        self.queue = deque([val])
    def push(self, x):
        self.queue.append(x)
    def pop(self):
        return self.queue.popleft()

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    M = int(input())
    C = list(map(int, input().split()))

    datastructures = []

    for i in range(N):
        if A[i] == 0:
            datastructures.append(Queue(B[i]))
        else:
            datastructures.append(Stack(B[i]))

    result = []
    for val in C:
        x = val
        for ds in datastructures:
            ds.push(x)
            x = ds.pop()
        result.append(x)

    print(*result)

if __name__ == "__main__":
    main()
