import sys

def cantoa(n):
    length = len(n)
    if length == 1:
        return n
    else:
        left = cantoa(n[:length//3])
        right = cantoa(n[2*length//3:])
        return left + ' ' * (length//3) + right

if __name__ == "__main__":
    for line in sys.stdin:
        n = int(line)
        st = '-' * (3 ** n) # 기본 세팅을 하고, 날리는 방식으로 집합 생성
        print(cantoa(st))

