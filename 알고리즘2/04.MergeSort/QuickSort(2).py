import random

def partition(a, lo, hi):  
    return j

def divideNPartition(a, lo, hi):
    pass

def quickSort(a):
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
