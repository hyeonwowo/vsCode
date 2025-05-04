import sys
input = sys.stdin.readline

def totalsum():
    current_sum = sum(lst[:M])
    max_sum = current_sum

    for i in range(M, N):
        current_sum = current_sum + lst[i] - lst[i - M]
        max_sum = max(max_sum, current_sum)

    return max_sum
        
if __name__ == "__main__":
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    print(totalsum())
