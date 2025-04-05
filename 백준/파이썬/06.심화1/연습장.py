def isGroupWord(word):
    st = set()
    prev = ''
    for ch in word:
        if prev != ch:
            if ch in st:
                return False
            st.add(ch)
        prev = ch

def groupWordCount(N):
    return sum(1 for _ in range(N) if isGroupWord(input().strip()))

if __name__ == "__main__":
    N = int(input())
    print(groupWordCount(N))