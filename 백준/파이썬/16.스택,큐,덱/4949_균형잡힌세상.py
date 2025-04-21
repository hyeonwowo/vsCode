import sys

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if self.empty(): return None
        return self.stack.pop() 
    def empty(self):
        if len(self.stack) == 0: return 1
        else: return 0

def balance(str):
    myStack = Stack()
    for ch in str:
        if ch in "({[":
            myStack.push(ch)
        elif ch in ")}]":
            popelement = myStack.pop()
            if popelement == None: return "no"
            if popelement != ch: return "no"
    return "yes"

if __name__ == "__main__":
    result = []
    while True:
        ipt = sys.stdin.readline().rsplit()
        if ipt == ".": break
        result.append(balance(ipt))
    print('\n'.join(result))