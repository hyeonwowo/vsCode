# 문자열의 모든 조합 + 정렬
lst = []
str = "acdeb"
for start in range(len(str)):
    for end in range(start,len(str)):
        lst.append(str[start:end+1])
resultlst = sorted(lst, key=lambda x:(len(x),x)) # 출력 : ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abc', 'bcd', 'abcd']

# + 정렬
resultlst = sorted(lst, key=lambda x:(len(x))) # 출력 : ['a', 'c', 'd', 'e', 'b', 'ac', 'cd', 'de', 'eb', 'acd', 'cde', 'deb', 'acde', 'cdeb', 'acdeb']
resultlst = sorted(lst, key=lambda x:(len(x),x)) # 출력 : ['a', 'b', 'c', 'd', 'e', 'ac', 'cd', 'de', 'eb', 'acd', 'cde', 'deb', 'acde', 'cdeb', 'acdeb']