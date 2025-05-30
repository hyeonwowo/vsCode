import sys

DP = [None for _ in range(16)]

def dotPoint(N):
    return DP[N]
    
def initdotPoint():
    DP[0] = None
    prev = 2
    for i in range(1,15+1):
        DP[i] = (prev + (prev - 1)) ** 2
        prev = (prev + prev - 1)

if __name__ == "__main__":
    N = int(input())
    initdotPoint()
    print(dotPoint(N))