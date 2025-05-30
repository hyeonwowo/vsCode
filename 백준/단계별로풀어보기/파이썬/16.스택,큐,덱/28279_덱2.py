import sys
from collections import deque

class Deque:    
    def __init__(self):
        self.dq = deque()

    def empty(self):
        return 0 if self.dq else 1

    def pushleft(self, x):
        self.dq.appendleft(x)

    def pushright(self, x):
        self.dq.append(x)

    def popleft(self):
        if self.empty(): return -1
        return self.dq.popleft()

    def popright(self):
        if self.empty(): return -1
        return self.dq.pop()

    def size(self):
        return len(self.dq)

    def peekleft(self):
        if self.empty(): return -1
        return self.dq[0]

    def peekright(self):
        if self.empty(): return -1
        return self.dq[-1]

if __name__ == "__main__":
    input = sys.stdin.readline
    myDeque = Deque()
    n = int(input())
    result = []

    for _ in range(n):
        cmd = input().split()
        if cmd[0] == "1":
            myDeque.pushleft(cmd[1])
        elif cmd[0] == "2":
            myDeque.pushright(cmd[1])
        elif cmd[0] == "3":
            result.append(myDeque.popleft())
        elif cmd[0] == "4":
            result.append(myDeque.popright())
        elif cmd[0] == "5":
            result.append(myDeque.size())
        elif cmd[0] == "6":
            result.append(myDeque.empty())
        elif cmd[0] == "7":
            result.append(myDeque.peekleft())
        elif cmd[0] == "8":
            result.append(myDeque.peekright())

    print('\n'.join(map(str, result)))
