from queue import PriorityQueue
import math

def dijkstra(g, s):
    distance = 0
    reversePath = []
    distTo = [None for _ in range(len(g))]
    edgeTo = [(math.inf) for _ in range(len(g))]
    
    pq = PriorityQueue()
    pq.put(s)
    
    while not pq.empty() and len(reversePath) < len(g) - 1:
        current_vertex = pq.get() 
    
    path = reversePath.reverse()
    return distance, path

def bellmanFord(g, s):
    distance = 0
    reversePath = []
    distTo = [None for _ in range(len(g))]
    edgeTo = [(math.inf) for _ in range(len(g))]
    
    path = reversePath.reverse()
    return distance, path

g = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}



result = dijkstra(g, 'A')
print(result)

result = bellmanFord(g, 'A')
print(result)
# 출력 예시: {'A': 0, 'B': 1, 'C': 3
