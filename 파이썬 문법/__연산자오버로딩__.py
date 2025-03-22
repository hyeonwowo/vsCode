# 연산자 오버로딩 : 기존의 연산자(+, <, == ..)을 사용자 정의 클래스에서 원하는 방식으로 작동하도록 정의함
# 주요 비교 연산자 메서드
# <     __lt__()    less than
# <=    __le__()    less than or equal
# >     __gt__()    greater than
# >=    __ge__()    greater than or equal
# ==    __eq__()    equal
# !=    __ne__()    not equal

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
    
    def __lt__(self, other): # '<' 연산자가 호출 시, 자동으로 실행
        return self.weight < other.weight
    
    def __gt__(self, other): # '>' 연산자 호출 시, 자동으로 실행
        return self.weight < other.weight
    
    def __eq__(self, other): # '==' 연산자 호출 시, 자동으로 실행
        return self.v == other.v and self.w == other.w and self.weight == other.weight
    
    def __str__(self):
        return f"{self.v}-{self.w} ({self.weight})"
    
    
e1 = Edge(0, 1, 3)
e2 = Edge(1, 2, 5)
e3 = Edge(0, 1, 3)

print(e1 < e2)   # True → weight 비교
print(e1 > e2)   # False
print(e1 == e3)  # True → 모든 필드가 같으면 같다고 판단
print(e1 == e2)  # False

