import sys

def recursion(s, l, r, count):
    if l >= r: return 1, count
    elif s[l] != s[r]: return 0, count
    else: return recursion(s, l+1, r-1, count+1)

def isPalindrome(s):
    count = 1
    return recursion(s, 0, len(s)-1, count)

def main(n):
    result = []
    for _ in range(n):
        word = sys.stdin.readline().strip()
        result.append(isPalindrome(word))
    return '\n'.join(*map(str, result))

if __name__ == "__main__":
    print(main(int(input())))