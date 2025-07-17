import sys

# 중복제거 1. set 자료구조 사용

def backtracking(start):
    if len(path) == m:
        # set에 추가시 .add + 리스트 형태 추가시 반드시 튜플형태 ! / list에 추가시 .append()
        res.add(tuple(path)) # append(path) : path의 원본 [] 이 저장되어 [[] [] []] 이와 같은 출력값이 나옴. 
                               # append(path[:]), append(list(path)) : path의 복사본 [a, b] 가 저장되어 [[a b] [a c] [b c]] 이와 같은 원하는 출력 값이 나옴.
        return
    else:
        for i in range(start, n):
            if not visited[i]:
                path.append(lst[i])
                visited[i] = True
                backtracking(i)
                path.pop()
                visited[i] = False
                

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lst = sorted(list(map(int, sys.stdin.readline().split())))
    
    res = set() # set() 선언
    visited = [False] * n
    path = []
    backtracking(0)
 
    sortlst = sorted(list(res)) # sorted() 복사본 반환, sort() 원본 수정
    
    for element in sortlst:
        print(*element)
    