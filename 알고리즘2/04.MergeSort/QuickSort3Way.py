import random

# Partition a[lo~hi] into 3-sections and then continue to partition each half recursively
def partition3Way(a, lo, hi):
    if (hi <= lo): return
    v = a[lo] # v는 기준점
    lt, gt = lo, hi  # lt : 피벗보다 작은 값들의 끝을 가르킴. gt : 피벗보다 큰 값들의 시작을 가르킴
    i = lo # i 는 움직일 포인터
    while i <= gt: # i가 오른쪽 영역에 도달시 검사 중단
        if a[i] < v:
            a[lt], a[i] = a[i], a[lt]  # Swap
            lt, i = lt+1, i+1
        elif a[i] > v:
            a[gt], a[i] = a[i], a[gt]  # Swap
            gt = gt-1
        else: i = i+1

    print(a)

    partition3Way(a, lo, lt-1) # 피벗보다 작은 부분 정렬
    partition3Way(a, gt+1, hi) # 피벗보다 큰 부분 정렬

def quickSort3Way(a):
    # Randomly shuffle a, so that the partitioning item is chosen randomly
    random.shuffle(a)

    partition3Way(a, 0, len(a)-1)
    return a

if __name__ == "__main__":
    print(quickSort3Way(["k","r","a","t","e","l","e","p","u","i","m","q","c","x","o","s"]))
    print(quickSort3Way(["k","k","k","k","k","k","k","k"]))
    print(quickSort3Way([1,2,3,4,5,6,7,8,9,10]))
    print(quickSort3Way([1,2,3,4,5,6,7,8,9]))
    print(quickSort3Way([10,9,8,7,6,5,4,3,2,1]))

    print(quickSort3Way(['R','B','W','W','R','W','B','R','R','W','B','R']))

