class Edge:
    def __init__(self, v, w, weight):
        self.v, self.w, self.weight = v, w, weight

    def __lt__(self, other):
        print(f"__lt__ called: comparing {self.weight} < {other.weight}")
        return self.weight < other.weight

a = Edge(0, 1, 3)
b = Edge(1, 2, 5)

# 아래는 언제 호출될까?
print(a < b)  # 여기서 __lt__ 호출됨
