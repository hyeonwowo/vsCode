import sys

def cantoa(n):
    length = len(n)
    if length == 1:
        return n
    else:
        left = cantoa(n[:length//3])
        right = cantoa(n[2*length//3:])
        return left + ' ' * (length//3) + right

def main():
    for line in sys.stdin:
        n = int(line)
        st = '-' * (3 ** n)
        print(cantoa(st))

if __name__ == "__main__":
    main()
