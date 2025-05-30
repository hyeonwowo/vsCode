import sys

def findCount(lst):
    standard = [1, 1, 2, 2, 2, 8]  # King, Queen, Rook, Bishop, Knight, Pawn 순
    return [s - x for s, x in zip(standard, lst)]

if __name__ == "__main__":
    lst = list(map(int, sys.stdin.readline().split()))
    print(*findCount(lst))
