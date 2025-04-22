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
    dictch ={
        ")":"(",
        "}":"{",
        "]":"["
    }
    for ch in str:
        if ch in "({[":
            myStack.push(ch)
        elif ch in ")}]":
            popelement = myStack.pop()
            if popelement == None: return "no"
            if popelement != dictch[ch]: return "no"
    return "yes" if myStack.empty() else "no"

if __name__ == "__main__":
    result = []
    while True:
        str = sys.stdin.readline().rstrip()
        if str == ".": break
        result.append(balance(str))
    print('\n'.join(result))