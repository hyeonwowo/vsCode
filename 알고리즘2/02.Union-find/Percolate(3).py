import statistics
import math
import random
import timeit

def simulate(n, t):  # n*n 격자, t의 시뮬레이션 횟수
    result = []

    for _ in range(t):
        ids = [i for i in range(n*n+2)]
        size = [1 for i in range(n*n+2)]
        grid = [[False]*n for _ in range(n)]

        def root(i):
            while ids[i] != i:
                ids[i] = ids[ids[i]]  # 🚀 경로 압축 추가
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

        top = 0  # 🚀 top을 마지막 노드로 변경
        bottom = n * n + 1  # 🚀 bottom을 마지막 +1 노드로 변경

        for i in range(n):
            union(top, i+1)  # 🚀 i+1 → i로 변경
        for i in range(n*n - n, n*n):
            union(bottom, i+1)  # 🚀 i+1 → i로 변경

        open_sites = 0
        rand_list = random.sample(range(n * n), n * n)  # 🚀 0부터 n*n-1까지 선택

        for point in rand_list:
            row, col = divmod(point, n)  # 🚀 point를 0부터 사용

            if grid[row][col]:
                continue
            grid[row][col] = True
            open_sites += 1
            index = point + 1

            if row > 0 and grid[row-1][col]:
                union(index, index-n)
            if row < n-1 and grid[row+1][col]:
                union(index, index+n)
            if col > 0 and grid[row][col-1]:
                union(index, index-1)
            if col < n-1 and grid[row][col+1]:
                union(index, index+1)

            if connected(top, bottom):
                result.append(open_sites/(n*n))
                break

    mean_result = statistics.mean(result)
    std_dev = statistics.stdev(result) if len(result) > 1 else 0
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
