import sys

class Stack:
    def __init__(self):
        self.stack = []
    def empty(self):
        if len(self.stack) == 0: return 1
        else: return 0
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if self.empty(): return None
        return self.stack.pop()
    def peek(self):
        if self.empty(): return None
        return self.stack[-1]

def dokidoki():
    student = list(map(int,sys.stdin.readline().split()))
    studentlen = len(student)
    emptySpace = Stack()
    count = 1
    resultlst = []
    
    while len(resultlst) < studentlen:
        if student and student[0] == count:
            resultlst.append(student.pop(0))
            count +=1 
        elif emptySpace.peek() == count:
            count += 1
            resultlst.append(emptySpace.pop())        
        elif student and student[0] != count:
            emptySpace.push(student.pop(0))
        else:
            return "Sad"
    return "Nice"

if __name__ == "__main__":
    _ = int(input())
    print(dokidoki())