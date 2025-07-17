import sys # n개의 자연수 중 m개를 고른 수열

def backtracking():
    if len(path) == M:
        print(*path)
        return
    else:
        for element in Nnum:
            if not vistied[element]:
                vistied[element] = True
                path.append(element)
                backtracking()
                path.pop()
                vistied[element] = False

if __name__ == "__main__":
    N,M = map(int, sys.stdin.readline().split())
    Nnum = sorted(list(map(int, sys.stdin.readline().split())))
    
    path = []
    vistied = [False] * (max(Nnum)+1)
    backtracking()
    
# 입력
# 4 2
# 9 8 7 1 

# 출력
# 1 7
# 1 8
# 1 9
# 7 1
# 7 8
# 7 9
# 8 1
# 8 7
# 8 9
# 9 1
# 9 7
# 9 8