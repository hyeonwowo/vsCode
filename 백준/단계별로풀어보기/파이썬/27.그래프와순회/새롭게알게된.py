# recursion 깊이 제한
import sys
sys.setrecursionlimit(10**6)


# 덱 사용
from collections import deque

mydeque = deque([1,2,3])
mydeque.append(4)
mydeque.extend([5,6,7])
print(mydeque)
print(mydeque.popleft())
print(mydeque.pop())
print(mydeque)


# DFS 카운트 누적
def DFS(x, y):
    count = 1
    
    count += DFS(x,y) # 카운트 누적시 사용
    return count


# grid입력시 strip
n = 5
grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)] # strip : "10010" -> [1,0,0,1,0] : 입력이 붙어있을 때 사용
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # split : "10010" -> [1001] "공백"이 없기 때문에, 내가 원하는 결과가 나오지 않음 : 입력이 공백과 함꼐 주어졌을 때 사용


# DFS, BFS 탐색시 grid[x][y] == 1 고려 안할시, 갈 수 없는 길로 탐색을 수행하여 원하지 않는 값이 나오게 된다
visited = [[]]
grid = [[]]

x, y = 1, 2
if visited[x][y] == False and grid[x][y] == 1:
    print("True")