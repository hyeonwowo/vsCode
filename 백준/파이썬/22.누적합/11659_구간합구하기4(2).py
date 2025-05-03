import sys
input = sys.stdin.readline

def main():
    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = prefix[i - 1] + num[i - 1]

    result = []
    for a, b in typelst:
        result.append(prefix[b] - prefix[a - 1])
    return '\n'.join(map(str, result))

if __name__ == "__main__":
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    typelst = [tuple(map(int, input().split())) for _ in range(M)]
    print(main())
