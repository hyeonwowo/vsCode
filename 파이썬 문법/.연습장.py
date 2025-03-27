import heapq
from collections import deque

def list_operation():
    arr = [1,2,3]
    
    arr.append(4)
    arr.insert(0,0)
    arr.pop()
    arr.pop(0)
    arr.remove(3)
    
    return arr

arr = list_operation()
print(arr)
print()

def heapq_operation():
    heap = []
    heapq.heappush(heap,3)
    heapq.heappush(heap,1)
    heapq.heappush(heap,5)
    print(heap)
    print(heapq.heappop(heap))
    print(heap)
    
    arr = [7,2,4]
    heapq.heapify(arr)
    heapq.heappush(arr, 1)
    print(arr)
    
heapq_operation()
print()

def deque_operations():
    dq = deque()
    dq.append(1)
    dq.appendleft(0)
    dq.pop()
    dq.popleft()
    print(dq)
    
deque_operations()
print()

def set_operations():
    s = set()
    s.add(1)
    s.add(1)
    s.add(2)
    
    s.discard(1)
    s.discard(999)
    print(s)
    
set_operations()
print()

def dict_operations():
    d = {'A' : 1,
         'B' : 2,
         'C' : 3}
    
    d['d'] = 4
    d['a'] = 100
    d.pop('d')
    print(d)
    
dict_operations()
print()

