import sys

def OX(n):
    result = []
    for _ in range(n):
        result.append(str(findsolution(sys.stdin.readline().strip())))
    return '\n'.join(result)
    
def findsolution(lst):
    count = 0
    temp = 1
    for ch in lst:
        if ch == 'O':
            count += temp 
            temp += 1
        elif ch == 'X': 
            temp = 1
    return count

if __name__ == "__main__":
    print(OX(int(input())))