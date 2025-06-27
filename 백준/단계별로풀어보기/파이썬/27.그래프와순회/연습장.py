from collections import deque

queue = deque([(0,0)])
x, y = queue.popleft()
print(x, y)