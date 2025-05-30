import sys

def findBlackJack(m,lst):
    # 삼중포문 세가지 선택지 가짓수 (n) * (n-1) * (n-2)의 삼중 for문으로 수행해야할듯
    max = 0
    for n1 in lst:
        for n2 in lst:
            if n2 <= n1: continue
            for n3 in lst:
                if n3 <= n2: continue
                if max < n1 + n2 + n3 <= m:
                    max = n1 + n2 + n3
    return max

if __name__ == "__main__":
    n,m = map(int,sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    print(findBlackJack(m,lst))