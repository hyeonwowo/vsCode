class Edge:
    def __init__(self, v, w, weight):
        self.v, self.w, self.weight = v, w, weight
    def __str__(self):
        return f"{self.v}----{self.weight}----{self.w}"

if __name__ == "__main__":
    edge1 = Edge(1,2,0.1)
    edge2 = Edge(2,3,0.4)
    edge3 = Edge(4,1,0.3)
    edge4 = Edge(7,3,0.1)
    edge5 = Edge(5,3,0.9)
    
    print(edge1)
    print(edge2)   
    print(edge3)   
    print(edge4)   
    print(edge5)   
    print()
    
    edgeList = []
    
    for i in range(5):
        edgeList.append(globals()[f"edge{i+1}"]) # Edge class를 리스트에 통체로 넣음 (v, w, weight)
    
    print(edgeList)
    print()
    
    for element in edgeList:
        print(element)
    print()
    
    # 리스트에 통체로 담긴 클래스를 다루기
    print(edgeList[0])
    print(edgeList[0].v)
    print(edgeList[0].w)
    print(edgeList[0].weight)