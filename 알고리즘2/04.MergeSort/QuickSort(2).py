import random

def partition(a, lo, hi):
    i,j = lo+1, hi
    
    while True:
        while i<=hi and a[lo] > a[i]: i += 1
        while j>=lo+1 and a[lo] < a[j]: j -= 1

        if (j<=i): break
        a[i],a[j] = a[j],a[i]
        i,j = i+1,j-1
    a[lo],a[j] = a[j],a[lo]
    return j

def divideNPartition(a, lo, hi):
    if lo>=hi: return
    j=partition(a,lo,hi)
    divideNPartition(a,lo,j-1)
    divideNPartition(a,j+1,hi)

def quickSort(a):
    random.shuffle(a)
    divideNPartition(a,0,len(a)-1)
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
