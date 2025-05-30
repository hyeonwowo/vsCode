N,M = map(int, input().split())
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