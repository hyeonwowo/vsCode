# 초기화 되지 않은 리스트 처리 오류
lst = []
for i in range(5):
    lst[i] = i # error 발생! (lst의 크기 초기화가 되지 않음)
    
    
# 방법1)
lst = []
for i in range(5):
    lst.append(i)
    
# 방법2)
lst = [None for _ in range(5)]
lst = [None] * 5
for i in range(5):
    lst[i] = i
    

# 벌집문제 점화식 / 알고리즘을 풀 때, 점화식 작성이 매우 중요함.
# a1 = i
# a2 = a1 + 2i
# a3 = a2 + 3i
# an = a(n-1) + n(n+1)/2