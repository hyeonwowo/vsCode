import random

# Partition a[lo~hi] using a[lo] as the partitioning (pivot) item
def partition(a, lo, hi):
    i, j = lo+1, hi # 시작 포인트(1)(2) 설정, i가 기준점보다 큰 요소 담당, j는 기준점보다 작은 요소 담당. 해당하는 요소에 위치하면 대기, i-j 모두 대기상태일 때 스왑

    while True:
        while i <= hi and a[i] < a[lo]: i = i+1 # 기준점보다 작으면 맞는 위치에 있기에 그대로 두고, 우측 인덱스로
        while j >= lo+1 and a[j] > a[lo]: j = j-1 # 기준점보다 크면 맞는 위체에 있기에 그대로 두고, 좌측 인덱스로

        if (j <= i): break      # 두 포인트가 만나서 엇갈리면 종료
        a[i], a[j] = a[j], a[i]   # Swap a[i] and a[j]
        i, j = i+1, j-1 # 스왑 후, 한칸씩 이동

    a[lo], a[j] = a[j], a[lo]    # j가 기준점보다 작은 요소를 담당하므로 j와 lo(기준점) 스왑   
    return j    # 기준점이 자리잡은 위치 반환(j와 스왑한 자리 -> j값)

# Partition a[lo~hi] and then continue to partition each half recursively
def divideNPartition(a, lo, hi):
    if (hi <= lo): return
    j = partition(a, lo, hi)    
    divideNPartition(a, lo, j-1) # 반환된 j를 기준으로 hi값을 잡음
    divideNPartition(a, j+1, hi) # 반환된 j를 기주으로 lo값을 잡음

def quickSort(a):
    # Randomly shuffle a, so that the partitioning item is chosen randomly
    random.shuffle(a) # 만약, 요소들이 정렬된 상태에서 quickSort 수행시 n^2 -> random.shuffle(a)를 통해 이와 같은 상황 방지

    divideNPartition(a, 0, len(a)-1)
    return a

if __name__ == "__main__":
    a = ["k", "r", "a", "t", "e", "l", "e", "p", "u", "i", "m", "q", "c", "x", "o", "s"]
    print(partition(a, 0, len(a)-1))
    print(a)

    print(quickSort(["k", "r", "a", "t", "e", "l", "e", "p", "u", "i", "m", "q", "c", "x", "o", "s"]))
    print(quickSort(["k", "k", "k", "k", "k", "k", "k", "k"]))
    print(quickSort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(quickSort([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(quickSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

    a = ["E", "C", "A", "I", "E"]
    print(partition(a, 0, 4), a)
