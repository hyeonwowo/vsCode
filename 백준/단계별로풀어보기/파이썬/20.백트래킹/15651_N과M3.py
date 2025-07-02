N,M = map(int,input().split()) # 중복 가능 수열
path = [] 
visited = [False] * (N+1)

def backtrack():
    if len(path) == M:
        print(*path)
        return
    else:
        for i in range(1,N+1):
            if not visited[i]:
                path.append(i)
                backtrack()
                path.pop()
                
if __name__ == "__main__":
    backtrack()
    
# 입력
# 4 2

# 출력
# 1 1
# 1 2
# 1 3
# 1 4
# 2 1
# 2 2
# 2 3
# 2 4
# 3 1
# 3 2
# 3 3
# 3 4
# 4 1
# 4 2
# 4 3
# 4 4