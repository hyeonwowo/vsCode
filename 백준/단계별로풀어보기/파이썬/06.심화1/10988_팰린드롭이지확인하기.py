import sys

def reverseWord(st):
    reverseSt = st[::-1]
    return 1 if reverseSt == st else 0

if __name__ == "__main__":
    st = sys.stdin.readline().strip()
    print(reverseWord(st))