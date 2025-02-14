import random

# Partition a[lo~hi] using a[lo] as the partitioning (pivot) item
def partition(a, lo, hi):
    return j    # Return the index of item in place    

# Find k-th smallest element, where k = 0 ~ len(a)-1
def quickSelect(a, k):
    return a[k]

if __name__ == "__main__":
    print(quickSelect(["k","r","a","t","e","l","e","p","u","i","m","q","c","x","o","s"], 0))
    print(quickSelect(["k","r","a","t","e","l","e","p","u","i","m","q","c","x","o","s"], 4))
    print(quickSelect(["k","r","a","t","e","l","e","p","u","i","m","q","c","x","o","s"], 10))
    print(quickSelect(["k","r","a","t","e","l","e","p","u","i","m","q","c","x","o","s"], 15))
    print(quickSelect(["k","k","k","k","k","k","k","k"], 5))
    print(quickSelect([1,2,3,4,5,6,7,8,9,10], 7))
    print(quickSelect([1,2,3,4,5,6,7,8,9], 3))
    print(quickSelect([10,9,8,7,6,5,4,3,2,1], 2))    
