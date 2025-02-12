import statistics
import math
import random
import timeit

def simulate(n, t):  # n*n 격자, t의 시뮬레이션 횟수
    results = []  # 각 실험에서 percolation이 발생하는 비율 저장

    for _ in range(t):
        ids = list(range(n * n + 2))  # Union-Find 배열 (0: 가상의 top, n*n+1: 가상의 bottom)
        size = [1] * (n * n + 2)  # 각 집합의 크기 추적
        grid = [[False] * n for _ in range(n)]  # 사이트 열림 상태

        # ids가 for문 내부에 선언돼있어서, UF도 반복문 내부에 선언..
        def root(i):
            while i != ids[i]:
                ids[i] = ids[ids[i]]  # 경로 압축 (Path Compression)
                i = ids[i]
            return i
        
        def connected(p, q):
            return root(p) == root(q)

        def union(p, q):
            root_p, root_q = root(p), root(q)
            if root_p == root_q:
                return
            if size[root_p] < size[root_q]:
                ids[root_p] = root_q
                size[root_q] += size[root_p]
            else:
                ids[root_q] = root_p
                size[root_p] += size[root_q]

        # 상단 가상 노드와 하단 가상 노드를 0, n*n+1에 배정
        virtual_top = 0
        virtual_bottom = n * n + 1

        # 상단 행을 가상 top에 연결
        for i in range(n):
            union(virtual_top, i + 1)

        # 하단 행을 가상 bottom에 연결
        for i in range(n):
            union(virtual_bottom, (n - 1) * n + i + 1)

        # 무작위로 사이트를 열기 시작
        opened_sites = 0
        indices = list(range(n * n))
        random.shuffle(indices)

        for site in indices:
            row, col = divmod(site, n)
            if grid[row][col]:  # 이미 열린 사이트면 스킵
                continue
            grid[row][col] = True # 닫힌곳이라면 True로 업데이트
            opened_sites += 1
            index = site + 1  # 1-based index 사용

            # 인접한 열린 사이트와 연결
            if row > 0 and grid[row - 1][col]:  # 위쪽
                union(index, index - n)
            if row < n - 1 and grid[row + 1][col]:  # 아래쪽
                union(index, index + n)
            if col > 0 and grid[row][col - 1]:  # 왼쪽
                union(index, index - 1)
            if col < n - 1 and grid[row][col + 1]:  # 오른쪽
                union(index, index + 1)

            # percolation 발생 여부 확인
            if connected(virtual_top, virtual_bottom):
                results.append(opened_sites / (n * n))
                break

    mean_result = statistics.mean(results)
    std_dev = statistics.stdev(results) if len(results) > 1 else 0
    return mean_result, std_dev


'''
Simulate the performance of Quick Union
'''
def simulateQU(n, t):
    def root(i):
        nonlocal ids
        while i != ids[i]: i = ids[i]
        return i

    def connected(p, q):
        return root(p) == root(q)

    def union(p, q):
        nonlocal ids
        id1, id2 = root(p), root(q)
        ids[id1] = id2
    
    for _ in range(t):
        ids = [i for i in range(n*n + 2)]
        for _ in range(math.floor(n*n*2)):
            connected(0, len(ids)-1)
            union(random.randint(0, len(ids)-1), random.randint(0, len(ids)-1))

'''
Simulate the performance of Quick Find
'''
def simulateQF(n, t):
    def connected(p, q):
        nonlocal ids
        return ids[p] == ids[q]

    def minMax(a, b):
        if a < b: return a, b
        else: return b, a

    def union(p, q):
        nonlocal ids
        id1, id2 = minMax(ids[p], ids[q])
        for idx, _ in enumerate(ids):
            if ids[idx] == id2: ids[idx] = id1
    
    for _ in range(t):
        ids = [i for i in range(n*n + 2)]
        for _ in range(math.floor(n*n*2)):
            connected(0, len(ids)-1)
            union(random.randint(0, len(ids)-1), random.randint(0, len(ids)-1))


'''
Unit Test
'''
if __name__ == "__main__":

    print("Correctness test for simulate()")
    print("For each test case, if your answer does not appear within 10 seconds, then consider that you failed the case")
    correct = True
    
    input = 1, 100
    rt_val = simulate(*input)
    print(f"simulate{input}: {rt_val} ", end="")
    if rt_val[0] == 1: print("Pass ", end="")
    else:
        print("Fail ", end="")
        correct = False
    if rt_val[1] == 0: print("Pass ", end="")
    else:
        print("Fail ", end="")
        correct = False
    print()    

    input = 2, 10000
    rt_val = simulate(*input)
    print(f"simulate{input}: {rt_val} ", end="")
    if math.floor(rt_val[0]*100) == 66: print("Pass ", end="")
    else:
        print("Fail ", end="")
        correct = False
    if round(rt_val[1]*10) == 1: print("Pass ", end="")
    else:
        print("Fail ", end="")
        correct = False
    print()

    input = 200, 100
    rt_val = simulate(*input)
    print(f"simulate{input}: {rt_val} ", end="")
    if math.floor(rt_val[0]*100) == 59: print("Pass ", end="")
    else:
        print("Fail ", end="")
        correct = False
    if round(rt_val[1]*100) == 1: print("Pass ", end="")
    else:
        print("Fail ", end="")
        correct = False
    print()
