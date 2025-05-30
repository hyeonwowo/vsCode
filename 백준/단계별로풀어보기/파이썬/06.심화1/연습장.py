import sys

def sumdata(lst):
    intSum = int(lst[0]) + int(lst[1]) - int(lst[2])
    A = int(lst[0] + lst[1])
    B = int(lst[2])
    strSum = A - B
    print(intSum)
    print(strSum)

if __name__ == "__main__":
    lst = [sys.stdin.readline().strip() for _ in range(3)]
    sumdata(lst)
