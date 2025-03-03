word = "hello world this is python world"
words = word.split()
print(word)
print(words)


# case1
dicta = {}

for ch in word:
    if ch not in dicta:
        dicta[ch] = 1
    else:
        dicta[ch] += 1
print(dicta)
print()

# case2
word = "hello world this is python world"
dicta = {}

for ch in word:
    dicta[ch] = dicta.get(ch, 0) + 1 # dict.get(key, default) : 딕셔너리에서 해당하는 key의 value값 반환, key 없을 시 default 값 반환

print(dicta)


# case3
from collections import Counter

word = "hello world this is python world"
dicta = Counter(word)

print(dicta)