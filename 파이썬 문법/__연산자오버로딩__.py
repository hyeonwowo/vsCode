# 연산자 오버로딩 : 기존의 연산자(+, <, ==, [], (), ...)을 사용자 정의 클래스에서 원하는 방식으로 작동하도록 정의함
# 주요 연산자 메서드 : 요소가 여러가지인(ex) v, w, weight) 클래스 구성요소들 중 기준점을 정해주기 위해 설정함

# 비교 연산자
# <     __lt__()        less than
# <=    __le__()        less than or equal
# >     __gt__()        greater than
# >=    __ge__()        greater than or equal
# ==    __eq__()        equal
# !=    __ne__()        not equal

# 산술 연산자
# +     __add__()       덧셈
# -     __sub__()       뺄셈
# *     __mul__()       곱셈

# 기타 연산자
# []    __getitem__()   인덱스로 속성 접근 (리스트처럼 사용)
# ()    __call__()      객체를 함수처럼 호출
# str() __str__()       print(e) 시 사용되는 출력 문자열
# repr() __repr__()     리스트, 디버깅 출력 등 내부 표현
# hash() __hash__()     set/dict의 key로 사용 가능하게 해줌

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    # < 연산자 : 가중치 기준 비교 (오름차순 정렬 시 사용)
    def __lt__(self, other):
        return self.weight < other.weight
        # e1.weight < e2.weight
        # e1.v < e2.v 로 변경 시 weight가 아닌 v를 기준으로 비교

    # > 연산자 : 가중치 기준 비교 (내림차순 정렬 시 사용)
    def __gt__(self, other):
        return self.weight > other.weight
        # e1.weight > e2.weight

    # == 연산자 : 모든 속성(v, w, weight)이 같을 때만 True
    def __eq__(self, other):
        return self.v == other.v and self.w == other.w and self.weight == other.weight
        # e1.v == e2.v and e1.w == e2.w and e1.weight == e2.weight

    # + 연산자 : 가중치만 더해서 새로운 Edge 반환
    def __add__(self, other):
        return Edge(self.v, self.w, self.weight + other.weight)

    # - 연산자 : 가중치만 빼서 새로운 Edge 반환
    def __sub__(self, other):
        return Edge(self.v, self.w, self.weight - other.weight)

    # * 연산자 : 가중치에 스칼라 값을 곱함
    def __mul__(self, scalar):
        return Edge(self.v, self.w, self.weight * scalar)

    # [] 연산자 : 인덱스를 이용해 속성에 접근 (e[0] → v, e[1] → w, e[2] → weight)
    def __getitem__(self, index):
        if index == 0: return self.v
        elif index == 1: return self.w
        elif index == 2: return self.weight
        else: raise IndexError("Index out of range")

    # () 연산자 : 객체를 함수처럼 호출 가능
    def __call__(self):
        print(f"Calling edge: {self}")

    # print(e) 시 호출되는 메서드
    def __str__(self):
        return f"{self.v}-{self.w} ({self.weight})"

    # 리스트나 디버깅 출력 시 호출됨
    def __repr__(self):
        return self.__str__()

    # set이나 dict의 key로 사용되도록 해줌
    def __hash__(self):
        return hash((self.v, self.w, self.weight))
    
e1 = Edge(0, 1, 3)
e2 = Edge(0, 1, 2)
e3 = Edge(1, 2, 4)

print(e1 < e3)     # True → __lt__ 호출 (3 < 4)
print(e1 > e2)     # True → __gt__ 호출 (3 > 2)
print(e1 == e2)    # False → __eq__ 호출
print(e1 == Edge(0, 1, 3))  # True

print(e1 + e2)     # 0-1 (5) → __add__
print(e1 - e2)     # 0-1 (1) → __sub__
print(e1 * 2)      # 0-1 (6) → __mul__

print(e1[0])       # 0 → v
print(e1[1])       # 1 → w
print(e1[2])       # 3 → weight

e1()               # 객체 호출 → Calling edge: 0-1 (3)

print([e1, e2])    # 리스트 출력 시 → __repr__ 사용

edges = {e1, e2, Edge(0, 1, 3)}
print(edges)       # set 중복 제거 → __eq__ + __hash__ 호출


# 왜 굳이, 일일히 코드를 작성해줘야 할까?

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

e1 = Edge(0, 1, 3.0)
e2 = Edge(1, 2, 5.0)
print(e1 < e2)  # ❌ 에러 발생!

# ❌ 결과: TypeError: '<' not supported between instances of 'Edge' and 'Edge'

# 파이썬은 객체끼리 비교하려면 "기준이 무엇인지 명시적으로 설정" 필요. ex) 기준이 v인지, w인지, weight인지


