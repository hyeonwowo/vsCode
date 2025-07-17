import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    lst = [2,3]
    
    for i in range(3, N+1):
        for j in range(2, i):
            if i % j == 0:
                continue
        lst.append(i)
                
    print(lst)