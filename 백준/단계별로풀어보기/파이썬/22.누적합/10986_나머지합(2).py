import sys

def remainsum(lst):
    remainlst = [0] * len(lst)
    remainlst[0] = lst[0] % m
    for i in range(1, len(lst)):
        remainlst[i] = (remainlst[i-1] + lst[i]) % m
        
    remaindict = {0: 1}  # ✅ 중요: 누적합이 0인 구간 고려
    for element in remainlst:
        if element not in remaindict:
            remaindict[element] = 1
        else:
            remaindict[element] += 1
    
    def foundation(n):
        return n * (n - 1) // 2

    result = 0
    for count in remaindict.values():
        result += foundation(count)
        
    return result

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    print(remainsum(lst))
