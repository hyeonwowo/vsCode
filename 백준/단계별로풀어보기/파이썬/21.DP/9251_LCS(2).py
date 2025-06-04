import sys

def LCS(str1, str2):
    a = len(str1)
    b = len(str2)
    dp = [[0] * a for _ in range(b)]
    
    return dp

if __name__ == "__main__":
    str1 = ' ' + sys.stdin.readline().strip()
    str2 = ' ' + sys.stdin.readline().strip()
    print(LCS(str1, str2))