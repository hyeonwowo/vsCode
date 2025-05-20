import sys

def findsum(lst):
    sum = [None] * len(lst) # 빈칸에서 None로 초기화했더니, 정상작동 : [] * len(lst) 빈칸을 반복하므로 결국엔 []
    sum[0] = lst[0]
    for i in range(1,n):
        sum[i] = max(lst[i], sum[i-1] + lst[i])
    return max(sum)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    print(findsum(lst))