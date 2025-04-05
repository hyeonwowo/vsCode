# st.count() : 문자열 st에 대해 .count("부분문자열") 호출시, 해당 부분문자열이 몇 번 등장했는지 정수로 반환
# count()는 내부적으로 문자열을 처음부터 끝까지 왼쪽에서 오른쪽으로 탐색하면서, 주어진 substring이 있는 모든 위치를 확인해 겹치지 않게 카운팅

# 1. 예제
s = "a b c d"
print(s.count(" "))  # 출력: 3 (공백이 3번 등장함)


# 2. 예제
s = "banana"
print(s.count("a"))      # 출력: 3
print(s.count("na"))     # 출력: 2
print(s.count("x"))      # 출력: 0 (없는 문자열은 0 반환)


# 3. count() 의 동작방식 (슬라이딩 윈도우)
s = "aaa"
print(s.count("aa"))  # 출력: 1 (겹치지 않게 "aa"는 한 번만 셈)
