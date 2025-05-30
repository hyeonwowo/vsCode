import sys

def Ascii(ch):
    return ord(ch)

if __name__ == "__main__":
    ch = sys.stdin.readline().strip()
    print(Ascii(ch))