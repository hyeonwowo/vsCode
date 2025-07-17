import sys

def conseqSum(N, lst):
    left = 0
    right = 0
    count = 0
    total = 0
    
    # 커서를 먼저 옮기고, 더함
    while True:
        if total >= N:
            total -= lst[left]
            left += 1
        elif right == len(lst):
            break
        else: # total < N
            total += lst[right]
            right += 1
            
        if total == N:
            count += 1            
    
    return count
            

# 소수 만들기 알고리즘 (에라토스테네스의 체 알고리즘)
def prime_numbers(n):
    lst = [i for i in range(n+1)]
    end = int(n**(1/2))
    for i in range(2, end + 1):
        if lst[i] == 0:
            continue
        for j in range(i*i, n+1, i):
            lst[j] = 0
            
    return [i for i in lst[2:] if lst[i]] 

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    lst = prime_numbers(N)
    print(conseqSum(N, lst))