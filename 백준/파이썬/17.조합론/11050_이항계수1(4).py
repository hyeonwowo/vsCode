import sys

def binocoff(n,k):
    binotree = [[0 for _ in range(1,i+1)] for i in range(1,n+1)]
    print(binotree)

if __name__ == "__main__":
    print(binocoff(5,2))