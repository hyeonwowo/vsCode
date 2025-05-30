import sys

def printlst(lst):
    lst.sort()
    for element in lst:
        sys.stdout.write(f"{element}\n")

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = [int(sys.stdin.readline()) for _ in range(n)]
    printlst(lst)
