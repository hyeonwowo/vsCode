# 🚀 중간단계 — 백트래킹을 더 똑똑하게 만들자!
# visited배열	: 이미 사용한 요소를 체크해서 중복을 막는다
# 중복제거 : 같은 선택을 여러 번 하지 않도록 한다
# 순서고려 : (순열/조합 문제에서) 순서가 중요한지 생각한다
# 가지치기 : (Pruning) 아예 의미 없는 경우는 탐색하지 않고 잘라낸다


# visited를 사용한 중복 없는 수열 만들기
N = 3 # 1,2,3 사용
M = 2 # 2개 선택

path = []
visited = [False] * (N+1) # 1번 ~ N번까지 방문 기록 (0번은 쓰지 않음)

def backtrack():
    if len(path) == M:
        print(path)
        return
    
    for i in range(1,N+1): # 1,2,3 중에서
        if not visited[i]: # 아직 사용하지 않았으면
            visited[i] = True # 사용 표시 : 나 이 숫자 썼어 !
            path.append(i) # 선택
            backtrack() # 다음 선택
            path.pop() # 선택 취소
            visited[i] = False # 사용 취소 : 이제 이 숫자 다시 쓸 수 있어 !
            
backtrack()
print()


# 1,2,3,4 중에서 중복 없이 3개를 골라서 나열하기
N = 4
M = 3

path = []
visited = [False] * (N+1)

def backtrack():
    if len(path) == M: 
        print(path)
        return
    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = True # visited[i]로 중복만 잘 관리하기
            path.append(i)
            backtrack()
            path.pop()
            visited[i] = False
            
backtrack()
print()


# 1,2,3,4,5 중에서 중복 없이 2개를 골리서 나열하기

N = 5
M = 2

path = []
visited = [False] * (N+1)

def backtrack():
    if len(path) == M:
        print(path)
        return
    for i in range(1,N+1):
        visited[i] = True
        path.append(i)
        backtrack()
        path.pop()
        visited[i] = False
        
backtrack()
print()