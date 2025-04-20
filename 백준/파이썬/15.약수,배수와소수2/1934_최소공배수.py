import sys

def gcd(a,b):
    while b>0:
        a, b = b, a%b
    return a

def lcm(a,b):
    return a*b / gcd(a,b)

def main(n):
    lst = []
    for _ in range(n):
        lst.append(int(lcm(*map(int,sys.stdin.readline().split()))))
    return '\n'.join(str(element) for element in lst)

if __name__ == "__main__":
    print(main(int(input())))