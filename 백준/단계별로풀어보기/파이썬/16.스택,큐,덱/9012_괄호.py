import sys

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if not self.empty():
            self.stack.pop()
    def empty(self):
        if len(self.stack) == 0: return 1
        else: return 0

def findsolution(str):
    myStack = Stack()
    for element in str:
        if element == '(':
            myStack.push(element)
        elif element == ')':
            if myStack.empty(): return "NO"
            myStack.pop()
    return "YES" if myStack.empty() else "NO"

if __name__ == "__main__":
    result = []
    n = int(input())
    for _ in range(n):
        solution = findsolution(sys.stdin.readline().strip())
        result.append(solution)
    print('\n'.join(result))