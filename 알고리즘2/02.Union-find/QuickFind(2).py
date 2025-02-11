N = 8

ids = [i for i in range(N)]

def connected(p, q):
    return ids[p] == ids[q]

def minMax(a, b):
    if ids[a] < ids[b]: return ids[a],ids[b] # a값을 기준으로 b -> a
    else: return ids[b],ids[a] # b값을 기준으로 a -> b

def union(p, q):
    min, max = minMax(p,q)
    for i in range(N):
        if ids[i] == max:
            ids[i] = min
'''
Unit Test
'''
if __name__ == "__main__":
    union(4,1)
    print("union(4,1)",ids)
    union(4,5)
    print("union(4,5)",ids)
    union(2,3)
    print("union(2,3)",ids)
    union(6,2)
    print("union(6,2)",ids)
    union(3,6)
    print("union(3,6)",ids)
    union(3,7)
    print("union(3,7)",ids)
    print(connected(1,7))
    union(5,2)
    print("union(5,2)",ids)
    print(connected(1,7))
    print(connected(0,6))
    union(0,3)
    print("union(0,3)",ids)
    print(connected(0,6))
