class Digraph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
    
    def addEdge(self, v, w):
        self.adj[v].append(w)
        
# 전체구조
'''
    모든 정점에 대해 DFS 시도
    이미 방문한 정점은 건너뛰고, 아직 방문하지 않은 정점에서 DFS 시작
    만약 그 DFS 안에서 사이클을 발견했다면, 바로 True 리턴
    끝까지 다 돌았는데 사이클 미발견시, False 리턴
'''  
'''
    MST를 구하기 위해서 사이클 탐지 필요 -> 해당 사이클 탐지 알고리즘이 아닌, union-find 기능 사용
    항목	현재 DFS 기반 사이클 탐지	MST용 사이클 탐지 (Union-Find)
    그래프   유향 그래프	          무향 그래프
    탐지	DFS 경로 도중	         간선 추가 전
    목적	사이클 존재 여부만 판단	    간선 추가 여부 결정
    방식	DFS + 재귀 + onStack	Union-Find (Disjoint Set)

'''
def hasCycle(g): 
    def dfs(v):
        visited[v] = True # DFS를 통해 한번이라도 방문한 정점 여부 확인
        onStack[v] = True # 현재 재귀호출 경로 내부에 v가 있는지 확인.
        for w in g.adj[v]: # 인접한 정점들 순회
            if not visited[w]:
                if dfs(w): return True # 해당 DFS 경로로 더 진행해나가다가, 사이클 발견시 즉시 True 리턴
            elif onStack[w]: # 이미 현재 경로 상에 있는 정점을 다시 만난다면 -> 사이클 발견 !
                return True # 사이클 발견 ! - True 리턴
        onStack[v] = False # 이 정점은 더이상 현재 DFS 경로에 없음.
        return False  # 이 정점에서는 사이클 탐색 불가 -> 다른 경로로 이동
    
    visited = [False] * g.v
    onStack = [False] * g.v
    
    for v in range(g.V):
        if not visited[v]:
            if dfs(v): return True # True 반환시 사이클 발견
    
    return False # False 반환시 사이클 미발견

if __name__ == "__main__":
    g = Digraph(4)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 0)  # cycle!
    g.addEdge(2, 3)

    print("Cycle exists?" , hasCycle(g))  # 출력: True
