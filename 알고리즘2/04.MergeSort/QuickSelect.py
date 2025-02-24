import random

def partition(a, lo, hi):
    i, j = lo+1, hi

    while True:
        while i <= hi and a[i] < a[lo]: i = i+1
        while j >= lo+1 and a[j] > a[lo]: j = j-1

        if (j <= i): break # 해당 조건을 j < i 로 바꿔도 되는지 -> 불필요한 swap이 발생할 가능성이 있음. i,j가 같은 위치에서 swap를 수행시 결국 같은값끼리 바꾸는 것이므로 불필요한 연산이 추가. + 실행 결과에 큰 문제는 없지만, 불필요한 1회의 연산이 추가됨을 방지
        a[i], a[j] = a[j], a[i] 
        i, j = i+1, j-1 # swap후 한칸씩 이동 (해당 코드 누락시, 첫번째 swap이후 그 위치에 갖혀있음)

    a[lo], a[j] = a[j], a[lo] # 기준점과 j간 위치 변경 
    return j # j위치 반환 (quickSelect시 사용)

def quickSelect(a, k):
    random.shuffle(a)

    lo, hi = 0, len(a)-1
    while (lo < hi):
        j = partition(a, lo, hi) # 여기서 선택 정렬 호출.
        if j < k: lo = j+1 # 오른쪽 파티션 호출
        elif k < j: hi = j-1 # 왼쪽 파티션 호출
        else: return a[k] # 연산 끝
    
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
