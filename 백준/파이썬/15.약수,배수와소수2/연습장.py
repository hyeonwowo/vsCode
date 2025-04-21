def goldpartion(k):
    count = 0
    for i in range(2,(k//2)+1):
        if findnum(i) and findnum(k-i):
            count += 1
    return count
        
def findnum(k):
    prime = [True] * (k+1)
    prime[0] = prime[1] = False
    for i in range(2, math.isqrt(k) + 1):
        if prime[i]:
            for j in range(i*i, k+1, i):
                prime[j] = False
    return prime[k]
