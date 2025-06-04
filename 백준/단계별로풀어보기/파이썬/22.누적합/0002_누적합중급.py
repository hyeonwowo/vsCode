import sys # 슬라이싱 윈도우 태크닉 사용

def totalsum(lst):
    slicewindow = sum(lst[:m])
    maxval = slicewindow
    for i in range(1,n-m+1):
        slicewindow = slicewindow - lst[i-1] + lst[i+m-1]
        if maxval < slicewindow:
            maxval = slicewindow
    return maxval

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    print(totalsum(lst))