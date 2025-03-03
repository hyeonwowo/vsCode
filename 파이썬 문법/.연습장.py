word = "hello world this is python world"
words = word.split()
print(word)
print(words)

dicta = {}

for ch in word:
    if ch not in dicta:
        dicta[ch] = 1
    else:
        dicta[ch] += 1

print(dicta)