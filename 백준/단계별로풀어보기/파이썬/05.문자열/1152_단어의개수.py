import sys

def countWord(lst):
    return len(lst)

if __name__ == "__main__":
    lst = sys.stdin.readline().split()
    print(countWord(lst))