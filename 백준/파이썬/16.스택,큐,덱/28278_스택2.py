import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            return -1
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        return 1 if not self.stack else 0

    def top(self):
        if not self.stack:
            return -1
        return self.stack[-1]

if __name__ == "__main__":
    input = sys.stdin.readline
    myStack = Stack()
    n = int(input())
    result = []

    for _ in range(n):
        cmd = input().split()
        if cmd[0] == '1':
            myStack.push(int(cmd[1]))
        elif cmd[0] == '2':
            result.append(str(myStack.pop()))
        elif cmd[0] == '3':
            result.append(str(myStack.size()))
        elif cmd[0] == '4':
            result.append(str(myStack.empty()))
        elif cmd[0] == '5':
            result.append(str(myStack.top()))

    print('\n'.join(result))
