import sys

def wordStudy(st):
    upperst = st.upper()
    word = {}
    for ch in upperst:
        if ch not in word:
            word[ch] = 1
        elif ch in word:
            word[ch] += 1 
    sortedWord = sorted(word.items(), key = lambda x:x[1], reverse=True)
    if len(word) > 1 and sortedWord[0][1] == sortedWord[1][1]: return "?"
    return sortedWord[0][0]
 
if __name__ == "__main__":
    st = sys.stdin.readline().strip()
    print(wordStudy(st))