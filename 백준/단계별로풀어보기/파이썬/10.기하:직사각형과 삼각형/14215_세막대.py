import sys

def trilength(a,b,c):
    if a==b==c: return 3*a
    lst = [a,b,c]
    lst.remove(max(lst))
    new = sum(lst) - 1
    lst.append(new)
    return sum(lst)

if __name__ == "__main__":
    a,b,c = map(int, sys.stdin.readline().split())
    print(trilength(a,b,c))