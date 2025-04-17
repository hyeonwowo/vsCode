# lst.reverse()
# 리스트 전용 메서드
# 리스트를 제자리에서 거꾸로 뒤집음
# 리턴값은 None

lst = [1,2,3]
lst.reverse()
print(lst)


# reversed(lst)
# 모든 반복 가능한 객체에서 사용 가능
# 원본을 변경하지 않고, 역순 반복자 리턴
# 출력 혹은 리스트 변환 후 사용

lst = [1,2,3]
revlst = reversed(lst)
print(list(revlst)) # [3,2,1]
print(lst) # [1,2,3] : 원본은 그대로