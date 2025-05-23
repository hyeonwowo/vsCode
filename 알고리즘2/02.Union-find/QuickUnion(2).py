N = 10

ids = [i for i in range(N)]

def root(i):
    while ids[i] != i:
        i = ids[i]
    return i

def connected(p,q):
    return root(p) == root(q)

def union(p,q):
    if connected(p,q):
        return None
    else:
        root_p, root_q = root(p), root(q)
        ids[root_p] = root_q

if __name__ == "__main__":
    union(6,5)
    print("union(6,5)",ids)
    union(5,0)
    print("union(5,0)",ids)
    union(2,1)
    print("union(2,1)",ids)
    union(7,1)
    print("union(7,1)",ids)
    union(4,3)
    print("union(4,3)",ids)
    union(4,8)
    print("union(4,8)",ids)
    union(6,7)
    print("union(6,7)",ids)
    union(9,8)
    print("union(9,8)",ids)
    union(7,3)
    print("union(7,3)",ids)
    print(connected(5,4))
    print(connected(7,9))
    