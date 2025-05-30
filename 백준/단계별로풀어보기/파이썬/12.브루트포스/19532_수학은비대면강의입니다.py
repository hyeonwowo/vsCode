import sys

def mathOnline(lst):
    a,b,c,d,e,f = lst
    for x in range(-999,1000):
        for y in range(-999,1000):
            if c == a*x + b*y and f == d*x + e*y:
                return x,y

if __name__ == "__main__":
    print(*mathOnline(list(map(int, sys.stdin.readline().split()))))