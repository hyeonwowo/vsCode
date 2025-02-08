# 튜플은 변경할 수 없는 자료형. 여러 값을 하나의 변수에 저장
# list와 상당히 유샇하지만, 한 번 생성하면 수정, 추가, 삭제 불가

# 튜플의 특징
# 1. 순서가 있다 - index 접근 가능
# 2. 변경할 수 없다 - 요소 추가, 삭제, 변경 불가
# 3. 중복을 혀용
# 4. 여러 자료형 포함

# 튜플 생성 방법 - ()
t1 = (1,2,3)
print(t1)

t1 = 1,2,3 # 소괄호 없이도 가능
print(t1)


# 단일 요소 튜플 생성 (쉼표 필수 ! - 없으면 정수로 인식)
t3 = (5,) # (5)는 그냥 정수 5지만, (5,)는 튜플이다
print(t3)


# tuple() 함수로 변환

t4 = tuple([1,2,3])
t5 = tuple("hello")
print(t4)
print(t5)


# 튜플 인덱싱 & 슬라이싱

    # 인덱싱
t = (10,20,30,40,50)
print(t[0])
print(t[-1])

    # 슬라이싱
t = (10,20,30,40,50)
print(t[1:4])
print(t[:3])
print(t[2:])
print(t[::-1]) # 튜플 뒤집기


# 튜플의 활용

# 1) 여러 변수 한번에 할당
a,b,c = (1,2,3)
print(a,b,c)


# 2) 값 교환
x=10
y=20
x,y = y,x
print(x,y)


# 3) 함수의 여러 값 반환
def get_coordinates():
    return (37.5665,126.9780) # 위도 경도

latitude, longitude = get_coordinates() # 여러 값을 한번에 반환
print(latitude, longitude)


# 4) 튜플을 딕셔너리 키로 사용
data = {
    (37.5665,126.9780):"seoul",
    (35.6885, 139.6917):"Tokyo"
}
print(data[(37.(37.5665,126.9780))]) # seoul

