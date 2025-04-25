# 파이썬에서의 조건분기
#  False로 평가되는 것들:
# None
# False
# 숫자 0 (정수형 0, 실수형 0.0, 복소수 0j 등)
# 빈 시퀀스/컨테이너 ('', [], {}, set(), dict(), range(0) 등)

# 🟢 그 외의 모든 값은 True로 평가됩니다:
# 양의 정수 2, 3, 4, 음수 -1, -5 등: ✅ 참
# "hello", [1, 2], { "key": "value" }: ✅ 참

if 3:
    print("참입니다")  # 출력됨

if None:
    print("거짓입니다")  # 출력 안 됨

if []:
    print("빈 리스트입니다")  # 출력 안 됨

if [1]:
    print("요소가 있는 리스트입니다")  # 출력됨

print()

# 리스트 인덱싱 처리와 조건문 : 리스트가 비어있는 경우를 고려
lst = [1,2,3,4,5]

while True:
    if lst: # lst 자체만으로 비어 있는 경우를 알 수 있음
        print(lst.pop())
    else:
        print("None..")
        break
    
# Deque의 연산
# ✅ 주요 연산 정리
# 메서드	설명	시간복잡도
# append(x)	오른쪽 끝에 x 추가	O(1)
# appendleft(x)	왼쪽 끝에 x 추가	O(1)
# pop()	오른쪽 끝 요소 제거 후 반환	O(1)
# popleft()	왼쪽 끝 요소 제거 후 반환	O(1)
# extend(iter)	오른쪽 끝에 iterable 추가	O(k)
# extendleft(iter)	왼쪽 끝에 iterable 추가 (순서 반대로 들어감)	O(k)
# clear()	모든 요소 제거	O(n)
# reverse()	순서를 반대로 뒤집음	O(n)
# rotate(n=1)	회전: 오른쪽으로 n칸 이동 (음수면 왼쪽으로)	O(k)
from collections import deque

dq = deque()

# 삽입
dq.append(1)        # dq: [1]
dq.appendleft(2)    # dq: [2, 1]

# 삭제
dq.pop()            # → 1, dq: [2]
dq.popleft()        # → 2, dq: []

# 확장
dq.extend([3, 4])         # dq: [3, 4]
dq.extendleft([1, 2])     # dq: [2, 1, 3, 4]

# 회전
dq.rotate(1)        # dq: [4, 2, 1, 3]
dq.rotate(-2)       # dq: [1, 3, 4, 2]

# 기타
dq.clear()          # dq: []
print()


# 문자열과 join의 + 연산
lst = [1,2,3,4,5,6,7]
print("<" + ', '.join(map(str,lst))+">")


# 클래스에서의 deque선언
class Deque:
    dq = deque()  # ❌ 클래스 변수 → 모든 인스턴스가 공유함
    # 메인함수에서 덱을 하나만 호출했다면 상관이 없지만, 여러개를 호출하고 연산 수행시 상호간섭이 발생함.

class Deque:
    def __init__(self):
        self.dq = deque()  # ✅ 인스턴스별로 독립된 덱을 호출하도록 코드 작성


# rotate : 리스트 회전 기능 제공
dq = deque([1,2,3,4,5])

dq.rotate(1)  # 오른쪽으로 1칸 회전 = 오른쪽으로 1칸 밀기
print(dq)     # 출력: deque([5, 1, 2, 3, 4])

dq.rotate(-2) # 왼쪽으로 2칸 회전 = 왼쪽으로 2칸 밀기
print(dq)     # 출력: deque([2, 3, 4, 5, 1])


# 일반 List에서는 rotate() 제공하지 않음. 리스트 회전 필요시 deque사용 혹은 슬라이싱 활용
lst = [1,2,3,4,5]
rotatedlst = lst[-1:] + lst[:-1] # 오른쪽으로 1칸 회전
print(rotatedlst) # 출력: [5, 1, 2, 3, 4]


# 절대값 : abs()
print(abs(-1))
print(abs(-2))
print(abs(-3))
print(abs(-4))



# empty()를 만들기보다, 스택 리스트 자체를 넣어 간편하게 비어있는지 아닌지 확인하기
class Stack:
    def __init__(self):
        self.stack = []
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop() if self.stack else None



# 자료구조를 사용자 입력 n개만큼 동적으로 생성하고 관리하는 방법 정리
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop() if self.stack else None
    def __repr__(self):
        return f"Stack: {self.stack}"

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, x):
        self.queue.append(x)
    def dequeue(self):
        return self.queue.pop(0) if self.queue else None
    def __repr__(self):
        return f"Queue: {self.queue}"


n = int(input("몇 개의 자료구조를 만들까요? "))
datestructurelst = []

for i in range(n):
    if i % 2 == 0:
        datestructurelst.append(Stack())
    else:
        datestructurelst.append(Queue())

datestructurelst[0].push(1)
datestructurelst[0].push(2)
datestructurelst[0].push(3)

datestructurelst[1].enqueue(1)
datestructurelst[1].enqueue(2)
datestructurelst[1].enqueue(3)

print("\n[Stack pops]")
print(datestructurelst[0].pop())  # 3
print(datestructurelst[0].pop())  # 2
print(datestructurelst[0].pop())  # 1

print("\n[Queue dequeues]")
print(datestructurelst[1].dequeue())  # 1
print(datestructurelst[1].dequeue())  # 2
print(datestructurelst[1].dequeue())  # 3

# 어떤 자료구조인지 확인 : isinstance 사용
for i, ds in enumerate(datestructurelst):
    if isinstance(ds, Stack):
        print(f"{i}번째는 Stack입니다.")
    elif isinstance(ds, Queue):
        print(f"{i}번째는 Queue입니다.")
