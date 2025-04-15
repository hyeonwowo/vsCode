# 중복없이 세 자연수 조합하기
lst = [1,2,3,4,5]

for i in lst:
    for j in lst:
        if i >= j: continue # 중요 !
        for k in lst:
            if j >= k: continue # 중요 !
            print(i,j,k)
print()


# 자릿수 모두 더하기
n = "3569"
result = sum(map(int, str(n)))
print(result)


# 2차원배열 초기화
lst = [[] for _ in range(5)]
print(lst)

lst = [] * 5 # 이 방법은 안됨
print(lst)


# 최소값 갱신문제 : 최소값은 무한대로, 최대값은 0으로 초기화 시키고 시작해야함. 그러지 않으면 영원히 갱신되지 않음
minValue = float('inf') 
maxValue = 0


# 무한대정수 초기화 : float('inf)
a = float('inf')
print(a)            # 출력: inf
print(a > 1000000)  # 출력: True
