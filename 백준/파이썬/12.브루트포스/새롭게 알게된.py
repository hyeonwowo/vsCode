# 중복없이 세 자연수 조합하기
lst = [1,2,3,4,5]

for i in lst:
    for j in lst:
        if i >= j: continue # 중요 !
        for k in lst:
            if j >= k: continue # 중요 !
            print(i,j,k)