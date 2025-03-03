st = {} # 딕셔너리 생성

# st[key] = value : 키 - value 삽입
st["www.knu.ac.kr"] = "155.230.11.1"
st["www.naver.com"] = "223.130.200.107"
st["dns.google"] = "8.8.8.8"

# key 값에 따른 value 값 출력
print(st["dns.google"])
print(len(st)) # 딕셔너리 내부 key 갯수 출력

# 딕셔너리 내부에 키가 있는지 없는지 : in 연산자 사용
if "dns.google" in st: 
    print("dns.google is in st")
else: 
    print("dns.google is NOT in st")

del st["dns.google"] # 딕셔너리 key 삭제 : del dictA["key"]

# 딕셔너리 내부에 키가 있는지 없는지 확인 : in 연산자 이용
if "dns.google" in st: 
    print("dns.google is in st")
else: 
    print("dns.google is NOT in st")
print(len(st)) # 딕셔너리 내부 key 갯수 출력

def frequencyCounter(sentences, minFrequency): # 문자 구분 함수
    st = {} # 딕셔너리 생성 
    for s in sentences: # 문자열 순회
        words = s.split() # 기본 사용법 : split() - 공백 기준   # 특정 구분자로 분할 : split("구분자") - 구분자 기준
        for w in words: # 분리된 문자들 순회
            if w not in st:  # 처음 등장한 단어
                st[w] = 1 # count : 1
            else: # 이미 등장한 단어
                st[w] += 1 # count : + 1
    
    # sorted()를 사용하여 빈도수 기준 내림차순(reverse=True) 정렬.
    # st.items() → [(단어, 빈도수), (단어, 빈도수), ...] 형태의 리스트를 반환.
    for k, v in sorted(st.items(), key=lambda x:x[1], reverse=True): 
        if (v >= minFrequency): # 빈도수가 minFrequency 이상이면 단어 빈도수를 출력.
            print(k, v)

frequencyCounter(["it was the best of times",\
    "it was the worst of times",\
    "it was the age of wisdom",\
    "it was the age of foolishness",\
    "it was the epoch of belief",\
    "it was the epoch of incredulity",\
    "it was the season of light",\
    "it was the season of darkness",\
    "it was the spring of hope",\
    "it was the winter of despair",\
    ], 5)

st2 = {}
st2["a"] = 1
st2["a"] = 2
st2["a"] = 3
st2["a"] = 4
print(st2["a"], len(st2))

