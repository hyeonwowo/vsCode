# 3. 스택(Stack)과 큐(Queue) 활용 문제
# 문제:

# push(), pop(), is_empty() 기능을 가진 스택 클래스를 작성하세요.
# enqueue(), dequeue(), is_empty() 기능을 가진 큐 클래스를 작성하세요.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def print(self):
        print(self.stack)

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def print(self):
        print(self.queue)

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

if __name__=="__main__":
    myStack = Stack()

    myStack.push(1)
    myStack.print()
    myStack.push(2)
    myStack.print()
    myStack.push(3)
    myStack.print()

    print(myStack.pop())
    myStack.print()
    print(myStack.is_empty())

    print()

    myQueue = Queue()

    myQueue.enqueue(1)
    myQueue.print()
    myQueue.enqueue(2)
    myQueue.print()
    myQueue.enqueue(3)
    myQueue.print()

    print(myQueue.dequeue())
    myQueue.print()
    print(myQueue.dequeue())
    myQueue.print()

