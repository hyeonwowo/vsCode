import sys # depth를 사용해서 작성해보기

def backtracking(depth,start):
    if depth == M:
        print(*path)
        return
    else:
        for i in range(start,N+1):
            path.append(i)
            backtracking(depth+1,i)
            path.pop()
            
if __name__ == "__main__":
    N,M = map(int, sys.stdin.readline().split())
    path = []
    backtracking(0,1)