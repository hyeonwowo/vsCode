import sys
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        N = int(input())
        parent = [0] * (N + 1)

        for _ in range(N - 1):
            p, c = map(int, input().split())
            parent[c] = p

        q1, q2 = map(int, input().split())

        # q1의 모든 조상 저장
        ancestors = set()
        cur = q1
        while cur != 0:
            ancestors.add(cur)
            cur = parent[cur]

        # q2에서 위로 올라가며 첫 공통 조상 찾기
        cur = q2
        while cur not in ancestors:
            cur = parent[cur]

        print(cur)
