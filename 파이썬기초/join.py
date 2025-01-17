# "구분자".join(리스트 or 이터러블) - 문자열 내의 요소들을 툭정 구분자로 연결하여 하나의 문자열로 리턴
# 요소는 반드시 문자열 !
# 숫자 등 문자열이 아닌 요소 존재시 오류 발생.
# map을 사용해 문자열로 변환

wordList = ["Test","Message","Fun"]
result = " ".join(wordList)
print(result)