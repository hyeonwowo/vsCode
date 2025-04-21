import sys
import math

def main(n):
    lst = []
    for _ in range(n):
        lst.append(int(sys.stdin.readline().strip()))
        
    maxk = max(lst)
    prime = [True] * (maxk + 1)
    prime[0] = prime[1] =  False
    for i in range(2, math.isqrt(maxk)+1):
        if prime[i]:
            for j in range(i*i, maxk+1, i):
                prime[j] = False    
    
    for idx, k in enumerate(lst):
        count = 0
        for i in range(2,(k//2+1)):
            if prime[i] and prime[k - i]:
                count += 1
        lst[idx] = count
        
    return '\n'.join(map(str,lst))

if __name__ == "__main__":
    print(main(int(sys.stdin.readline().strip())))