import sys
sys.setrecursionlimit(10000)

def is_good_sequence(seq):
    length = len(seq)
    for i in range(1, length // 2 + 1):
        if seq[-i:] == seq[-2*i:-i]:
            return False
    return True

def backtrack(seq):
    if len(seq) == n:
        print(''.join(seq))
        sys.exit(0) # 1 2 3 순으로 탐색하기에 첫번째 탐색 결과로 최소값이 나옴

    for ch in '123':
        seq.append(ch)
        if is_good_sequence(seq):
            backtrack(seq)
        seq.pop()

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    backtrack([])
