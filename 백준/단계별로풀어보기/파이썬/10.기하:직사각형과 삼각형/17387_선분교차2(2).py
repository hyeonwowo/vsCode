import sys

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

def is_cross(A, B, C, D): # CCW ?
    ccw1 = ccw(*A, *B, *C) * ccw(*A, *B, *D)
    ccw2 = ccw(*C, *D, *A) * ccw(*C, *D, *B)

    if ccw1 == 0 and ccw2 == 0:
        return (min(A[0], B[0]) <= max(C[0], D[0]) and
                min(C[0], D[0]) <= max(A[0], B[0]) and
                min(A[1], B[1]) <= max(C[1], D[1]) and
                min(C[1], D[1]) <= max(A[1], B[1]))
    return ccw1 <= 0 and ccw2 <= 0

if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
    A, B, C, D = (x1, y1), (x2, y2), (x3, y3), (x4, y4)

    print(1 if is_cross(A, B, C, D) else 0)
