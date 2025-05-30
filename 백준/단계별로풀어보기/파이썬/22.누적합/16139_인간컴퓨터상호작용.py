import sys
input = sys.stdin.readline

alphaPrev = [[0] for _ in range(26)] 

def wordcount():
    for i in range(wordlen):
        for j in range(26):
            alphaPrev[j].append(alphaPrev[j][-1])
        idx = ord(word[i]) - ord('a')
        alphaPrev[idx][-1] += 1 

if __name__ == "__main__":
    word = input().strip()
    wordlen = len(word)
    inputcount = int(input())
    result = []

    wordcount()

    for _ in range(inputcount):
        ch, a, b = input().split()
        a = int(a)
        b = int(b)
        idx = ord(ch) - ord('a')
        res = alphaPrev[idx][b+1] - alphaPrev[idx][a]
        result.append(str(res))

    print('\n'.join(result))
