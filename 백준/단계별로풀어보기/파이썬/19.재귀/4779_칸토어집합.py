import sys
sys.setrecursionlimit(10**6)

def cantoa(st):
    length = len(st)
    if length == 1: # 쪼개지다보면 결국에 - or ' ' 둘중에 하나로 결정. 이거를 반환하고 조합해 최종 결과 생성
        return st
    else:
        return cantoa(st[:length//3]) + " " * (length // 3) + cantoa(st[2*length//3:])

if __name__ == "__main__":
    for line in sys.stdin:
        n = int(line)
        st = '-' * (3 ** n)
        print(cantoa(st))