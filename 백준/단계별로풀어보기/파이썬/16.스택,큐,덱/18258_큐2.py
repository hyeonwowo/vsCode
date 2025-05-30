import sys

class Queue:
    def __init__(self):
        self.queue = []
    def empty(self):
        if self.queue: return 0
        else: return 1
    def push(self, x):
        self.queue.append(x)
    def pop(self):
        if self.empty(): return -1
        return self.queue.pop(0)
    def size(self):
        return len(self.queue)
    def front(self):
        if self.empty(): return -1
        return self.queue[0]
    def back(self):
        if self.empty(): return -1
        return self.queue[-1]
    
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    resultlst = []
    myQueue = Queue()
    for _ in range(n):
        cmd = sys.stdin.readline().split()
        if cmd[0] == "empty":
            resultlst.append(myQueue.empty())
        elif cmd[0] == "push":
            myQueue.push(cmd[1])
        elif cmd[0] == "pop":
            resultlst.append(myQueue.pop())
        elif cmd[0] == "size":
            resultlst.append(myQueue.size())
        elif cmd[0] == "front":
            resultlst.append(myQueue.front())
        elif cmd[0] == "back":
            resultlst.append(myQueue.back())
    print('\n'.join(map(str,resultlst)))