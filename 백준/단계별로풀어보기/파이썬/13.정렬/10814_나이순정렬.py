import sys

def sortage(n):
    lst = [tuple(sys.stdin.readline().split()) for _ in range(n)]
    sortlst = sorted(lst, key=lambda x:int(x[0]))
    print('\n'.join(f"{age} {name}" for age, name in sortlst))

if __name__ == "__main__":
    sortage(int(input()))