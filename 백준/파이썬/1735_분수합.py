import sys

def gcd(a,b):
    while b>0:
        a,b = b, a%b
    return a

def lcm(a,b):
    return (a*b) // gcd(a,b)

def sumfountain():
    a,b = map(int, sys.stdin.readline().split())
    c,d = map(int, sys.stdin.readline().split())
    parent = lcm(b,d)
    child1 = a * (parent // b)
    child2 = c * (parent // d)
    g = gcd(child1 + child2, parent)
    return (child1 + child2) // g, parent // g 

if __name__ == "__main__":
    print(*sumfountain())