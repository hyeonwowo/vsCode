import sys

def sortnum(lst):
    lst.sort()
    for element in lst:
        sys.stdout.write(f"{element}\n")

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    lst = [int(sys.stdin.readline()) for _ in range(n)]
    sortnum(lst)