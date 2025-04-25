import sys

def binocoff(n,k):
    cache = [[0 for _ in range(i)] for i in range(1,n+1)]
    
    for i in range(n+1):
        cache[i][0] = 1
    for i in range(k+1):
        cache[i][i] = 1
        
    for i in range(1,n+1):
        for j in range(1,k+1):
            cache[i][j] = cache[i-1][j] + cache[i-1][j-1]
    return cache[n][k]

if __name__ == "__main__":
    print(binocoff(5,2))