# 다익스트라, 벨만포드 모두 start지점에서 모든 vertex까지의 모든 거리를 구함

# 특별한 제약 조건 X -> 다익스트라
# 음수간선 -> 벨만포드


# 클래스 요소 빼내기
class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V+1)]
    
    def addEdge(self, v, w, weight):
        self.adj[v].append(Edge(v, w, weight))
        
V = 5
graph = Graph(V)
dist = [[float('inf')] * (V+1) for _ in range(V+1)]

for i in range(1, V+1):
    for edge in graph.adj[i]: # 클래스를 하나씩 순회한다
        dist[edge.v][edge.w] = min(dist[edge.v][edge.w], edge.weight) # 해당클래스에서 요소를 . 연산자를 통해 빼낸다
        

# float('inf') / int(1e9)
# https://letalearns.tistory.com...
# 이 블로그에 해답이 있습니다.
# 저도 방금까지 맞왜틀 하다가 저 블로그를 보고 inf를 쓰면 안되는 이유를 알았는데
# inf에 음수 가중치를 더해도 inf 그대로이기 때문에 inf를 쓰면 안된다고 합니다! :)