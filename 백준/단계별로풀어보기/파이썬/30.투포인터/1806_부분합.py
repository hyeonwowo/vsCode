import sys

# 합이 S 이상이면, 길이를 기록하고 start를 증가시켜 구간을 줄여보고
# 합이 S 미만이면, end를 증가시켜 구간을 늘려보자

def twoPointer(S, lst):
    left = 0
    right = 0
    count = 0
    
    while left < right:
        

if __name__ == "__main__":
    N, S = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    print(twoPointer(S, lst))